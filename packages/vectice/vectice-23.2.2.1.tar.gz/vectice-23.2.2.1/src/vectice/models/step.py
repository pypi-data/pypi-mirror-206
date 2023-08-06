from __future__ import annotations

import logging
import pickle  # nosec
from io import IOBase
from typing import TYPE_CHECKING, Any

from PIL.Image import Image

import vectice
from vectice.api.json.dataset_register import DatasetRegisterOutput
from vectice.api.json.dataset_version import DatasetVersionOutput
from vectice.api.json.iteration import (
    IterationStatus,
    IterationStepArtifact,
    IterationStepArtifactInput,
    IterationStepArtifactType,
)
from vectice.api.json.model_register import ModelRegisterOutput
from vectice.api.json.model_version import ModelVersionOutput
from vectice.api.json.step import StepType
from vectice.models.attachment_container import AttachmentContainer
from vectice.utils.common_utils import _check_image_path, _get_image_variables
from vectice.utils.last_assets import _comment_or_image_logging, _register_dataset_logging, _register_model_logging

if TYPE_CHECKING:
    from vectice import Connection
    from vectice.models import Iteration, Phase, Project, Workspace
    from vectice.models.dataset import Dataset
    from vectice.models.model import Model
    from vectice.models.step_dataset import StepDataset
    from vectice.models.step_model import StepModel
    from vectice.models.step_number import StepNumber
    from vectice.models.step_string import StepString

_logger = logging.getLogger(__name__)

MISSING_DATASOURCE_ERROR_MESSAGE = "Cannot create modeling dataset. Missing %s data source."


class Step:
    """Model a Vectice step.

    Steps define the logical sequence of steps required to complete
    the phase along with their expected outcomes.

    Steps belong to an Iteration. The steps created under a Phase are
    Step Definitions that are then re-used in Iterations to iteratively
    complete the steps until a satisfactory result is obtained.

    ```tree
    phase 1
        step definition 1
        step definition 2
        step definition 3
    ```

    ```tree
    iteration 1 of phase 1
        step 1
        step 2
        step 3
    ```

    If steps are added to a phase after iterations have been created
    and completed, these steps won't appear in these iterations.

    NOTE: **Phases and Steps Definitions are created in the Vectice App,
    Iterations are created from the Vectice Python API.**

    To complete an iteration's step, you just need to assign a value to it.
    To access the step and assign a value, you can use the "slug" of the step:
    the slug is the name of the step, transformed to fit Python's naming rules,
    and prefixed with `step_`. For example, a step called "Clean Dataset" can
    be accessed with `my_iteration.step_clean_dataset`.

    Therefore, to complete a step:

    ```python
    my_clean_dataset = ...
    my_iteration.step_clean_dataset = my_clean_dataset
    ```

    Depending on the step, you can assign it a [`Model`][vectice.models.model.Model],
    a [`Dataset`][vectice.models.dataset.Dataset], code source, or attachments.
    """

    def __init__(
        self,
        id: int,
        iteration: Iteration,
        name: str,
        index: int,
        slug: str,
        description: str | None = None,
        artifacts: list[IterationStepArtifact] | None = None,
        step_type: StepType = StepType.Step,
        text: str | None = None,
    ):
        """Initialize a step.

        Vectice users shouldn't need to instantiate Steps manually,
        but here are the step parameters.

        Parameters:
            id: The step identifier.
            iteration: The iteration to which the step belongs.
            name: The name of the step.
            index: The index of the step.
            slug: The slug of the step.
            description: The description of the step.
            artifacts: The artifacts linked to the steps.
            step_type: The step type.
            text: The step text.
        """
        self._id = id
        self._iteration: Iteration = iteration
        self._name = name
        self._index = index
        self._description = description
        self._client = self._iteration._client
        self._artifacts = artifacts or []
        self._slug = slug
        self._type: StepType = step_type
        self._text = text
        self._model: Model | None = None

        self._iteration_read_only = self._iteration._status in {IterationStatus.Completed, IterationStatus.Abandoned}
        if self._iteration_read_only:
            _logger.debug(f"Step {self.name}, iteration is {self._iteration._status.name} and is read-only!")

    def __repr__(self):
        return f"Step(name={self.name!r}, slug={self.slug!r}, id={self.id!r})"

    def __eq__(self, other: object):
        if not isinstance(other, Step):
            return NotImplemented
        return self.id == other.id

    def __iadd__(self, value):
        # TODO cyclic import
        from vectice.models.dataset import Dataset
        from vectice.models.model import Model
        from vectice.models.step_dataset import StepDataset
        from vectice.models.step_model import StepModel

        if isinstance(value, Model):
            if self._type not in {StepType.StepModel, StepType.Step}:
                raise TypeError(f"A model can't be added to a step of type {self._type!r}.")
            code_version_id = self._get_code_version_id()
            model_data = self._client.register_model(
                model=value,
                project_id=self.project.id,
                phase_id=self.phase.id,
                iteration_id=self.iteration.id,
                code_version_id=code_version_id,
            )
            attachments_output = self._set_model_attachments(value, model_data.model_version)
            model_artifact = IterationStepArtifact(modelVersionId=model_data["modelVersion"]["id"], type="ModelVersion")
            copy_artifacts = self.artifacts.copy()
            self.artifacts += [model_artifact]
            attachments = (
                [
                    IterationStepArtifact(entityFileId=attach["fileId"], type="EntityFile")
                    for attach in attachments_output
                ]
                if attachments_output
                else []
            )
            self.artifacts += attachments

            self._keep_artifacts_and_update_step(StepType.StepModel, value)
            step = StepModel(self, model_artifact, value)
            _register_model_logging(self, model_data, value, self.name, attachments_output, _logger, copy_artifacts)
            self._iteration._steps[self.name] = step
        elif isinstance(value, Dataset):
            if self._type not in {StepType.StepDataset, StepType.Step}:
                raise TypeError(f"A dataset can't be added to a step of type {self._type!r}.")
            code_version_id = self._get_code_version_id()
            dataset_output = self._client.register_dataset_from_source(
                dataset=value,
                project_id=self.project.id,
                phase_id=self.phase.id,
                iteration_id=self.iteration.id,
                code_version_id=code_version_id,
            )
            attachments_output = self._set_dataset_attachments(value, dataset_output.dataset_version)
            dataset_artifact = IterationStepArtifact(
                datasetVersionId=dataset_output["datasetVersion"]["id"],
                type=IterationStepArtifactType.DataSetVersion.name,
            )
            copy_artifacts = self.artifacts.copy()
            self.artifacts.append(dataset_artifact)
            attachments = (
                [
                    IterationStepArtifact(entityFileId=attach["fileId"], type="EntityFile")
                    for attach in attachments_output
                ]
                if attachments_output
                else []
            )
            self.artifacts += attachments
            self._keep_artifacts_and_update_step(StepType.StepDataset, value)
            step = StepDataset(self, dataset_artifact)
            _register_dataset_logging(self, dataset_output, value, attachments_output, _logger, copy_artifacts)
            self._iteration._steps[self.name] = step
        else:
            raise TypeError(f"Expected Dataset or a Model, got {type(value)}")

    def _keep_artifacts_and_update_step(self, step_type: StepType, value) -> None:
        artifacts = self._client.get_step_by_name(self.name, self._iteration.id).artifacts

        def _get_artifact_id(artifact: IterationStepArtifact) -> int:
            if artifact.model_version_id:
                return artifact.model_version_id
            if artifact.dataset_version_id:
                return artifact.dataset_version_id
            if artifact.entity_file_id:
                return artifact.entity_file_id
            raise ValueError("No artifact ID.")

        def _maintain_and_add_artifacts(session_artifacts, existing_artifacts):
            # Ensure we don't keep adding an instances artifacts to the step
            maintain_artifacts = existing_artifacts
            for artifact in session_artifacts:
                match = any(filter(lambda x: x.id == artifact.id, existing_artifacts))
                if not match:
                    maintain_artifacts += [artifact]
            return maintain_artifacts

        # These are artifacts that exist in the current instance
        session_artifacts = [
            IterationStepArtifactInput(id=_get_artifact_id(artifact), type=artifact.type.value)
            for artifact in self.artifacts
        ]
        # These are artifacts in Vectice
        existing_artifacts = [
            IterationStepArtifactInput(id=_get_artifact_id(artifact), type=artifact.type.value)
            for artifact in artifacts
        ]
        # Ensure no crossover or duplicates
        maintain_artifacts = _maintain_and_add_artifacts(session_artifacts, existing_artifacts)
        self._client.update_iteration_step_artifact(self.id, step_type, artifacts=maintain_artifacts)
        self._warn_step_change(value)

    def _step_factory_and_update(
        self, value: Dataset | Model | int | float | str | None = None
    ) -> Step | StepString | StepNumber | StepDataset | StepModel:
        # TODO cyclic imports
        from vectice.models.dataset import Dataset
        from vectice.models.model import Model
        from vectice.models.step_dataset import StepDataset
        from vectice.models.step_image import StepImage
        from vectice.models.step_model import StepModel
        from vectice.models.step_number import StepNumber
        from vectice.models.step_string import StepString

        if isinstance(value, (int, float)):
            self._update_iteration_step(StepType.StepNumber, value)
            _comment_or_image_logging(self, _logger)
            return StepNumber(step=self, number=value)

        if (
            isinstance(value, Image)
            or isinstance(value, IOBase)
            or (isinstance(value, str) and _check_image_path(value))
        ):
            step_artifacts, filename = self._create_image_artifact(value)
            self._update_iteration_step(StepType.StepImage, value, step_artifacts)
            _comment_or_image_logging(self, _logger, filename)
            return StepImage(self, value)

        if isinstance(value, str):
            self._update_iteration_step(StepType.StepString, value)
            _comment_or_image_logging(self, _logger)
            return StepString(self, string=value)

        if isinstance(value, Model):
            code_version_id = self._get_code_version_id()
            data = self._client.register_model(
                model=value,
                project_id=self.project.id,
                phase_id=self.phase.id,
                iteration_id=self.iteration.id,
                code_version_id=code_version_id,
            )
            attachments_output = self._set_model_attachments(value, data.model_version)

            artifacts = self._get_version_artifacts(data, attachments_output)
            self._client.update_iteration_step_artifact(
                self.id,
                StepType.StepModel,
                None,
                artifacts,
            )
            _register_model_logging(self, data, value, self.name, attachments_output, _logger)
            self.artifacts = [IterationStepArtifact(modelVersionId=data["modelVersion"]["id"], type="ModelVersion")]
            self._warn_step_change(value)
            return StepModel(self, self.artifacts[0], value)

        if isinstance(value, Dataset):
            code_version_id = self._get_code_version_id()
            dataset = self._client.register_dataset_from_source(
                dataset=value,
                project_id=self.project.id,
                phase_id=self.phase.id,
                iteration_id=self.iteration.id,
                code_version_id=code_version_id,
            )
            attachments_output = self._set_dataset_attachments(value, dataset.dataset_version)
            artifacts = self._get_version_artifacts(dataset, attachments_output)
            self._client.update_iteration_step_artifact(
                self.id,
                StepType.StepDataset,
                None,
                artifacts,
            )
            _register_dataset_logging(self, dataset, value, attachments_output, _logger)
            self.artifacts = [
                IterationStepArtifact(datasetVersionId=dataset["datasetVersion"]["id"], type="DataSetVersion")
            ]
            self._warn_step_change(value)
            return StepDataset(self, dataset_version=self.artifacts[0])

        return self

    def _get_version_artifacts(
        self, data: ModelRegisterOutput | DatasetRegisterOutput, attachments_output: list[dict] | None = None
    ) -> list[IterationStepArtifactInput]:
        attachments = None
        if attachments_output:
            attachments = (
                [IterationStepArtifactInput(id=attach["fileId"], type="EntityFile") for attach in attachments_output]
                if attachments_output
                else None
            )
        if isinstance(data, ModelRegisterOutput):
            artifact = IterationStepArtifactInput(
                id=data["modelVersion"]["id"],
                type=IterationStepArtifactType.ModelVersion.name,
            )
        else:
            artifact = IterationStepArtifactInput(
                id=data["datasetVersion"]["id"],
                type=IterationStepArtifactType.DataSetVersion.name,
            )
        artifacts = [artifact]
        artifacts += attachments if attachments else []
        return artifacts

    def _create_image_artifact(self, value: str | IOBase | Image) -> tuple[list[IterationStepArtifactInput], str]:
        image, filename = _get_image_variables(value)
        try:
            attachments_output = self._client.create_phase_attachments(
                [("file", (filename, image))], self.phase.id, self.project.id
            )
            return [
                IterationStepArtifactInput(id=artifact["fileId"], type="EntityFile") for artifact in attachments_output
            ], filename
        except Exception as error:
            raise ValueError("Check the provided image.") from error

    def _keep_artifacts(self, artifacts: list[IterationStepArtifact]) -> list[IterationStepArtifactInput]:
        def _get_artifact_id(artifact: IterationStepArtifact) -> int:
            if artifact.model_version_id:
                return artifact.model_version_id
            if artifact.dataset_version_id:
                return artifact.dataset_version_id
            if artifact.entity_file_id:
                return artifact.entity_file_id
            raise ValueError("No artifact ID.")

        return [
            IterationStepArtifactInput(id=_get_artifact_id(artifact), type=artifact.type.value)
            for artifact in artifacts
        ]

    def _update_iteration_step(
        self, type: StepType, value, step_artifacts: list[IterationStepArtifactInput] | None = None
    ):
        # TODO: cyclic import
        from vectice.models.model import Model

        if type is StepType.StepImage:
            self._client.update_iteration_step_artifact(
                self.id,
                type,
                None,
                artifacts=step_artifacts or [],
            )
            self._warn_step_change(StepType.StepImage)
        elif isinstance(value, (str, int, float)):
            maintain_artifacts = self._keep_artifacts(
                self._client.get_step(self.id, self.phase.id, self.iteration.index).artifacts
            )
            self._client.update_iteration_step_artifact(
                self.id,
                type,
                str(value),
                maintain_artifacts,
            )

            self._warn_step_change(value)
        elif isinstance(value, Model) or type is StepType.StepModel:
            self._client.update_iteration_step_artifact(self.id, StepType.StepModel, artifacts=step_artifacts)
            self._warn_step_change(value)
            self._model = value
        elif type is StepType.StepDataset:
            self._client.update_iteration_step_artifact(self.id, StepType.StepDataset, artifacts=step_artifacts)
            self._warn_step_change(value)

    def _warn_step_change(self, value):
        # TODO: cyclic import
        from vectice.models.dataset import Dataset
        from vectice.models.model import Model

        if self._type is StepType.Step:
            return
        elif self._type is not StepType.StepModel and isinstance(value, Model):
            _logger.debug(f"Step type changed from {self._type.name} to StepModel")
        elif self._type is not StepType.StepDataset and isinstance(value, Dataset):
            _logger.debug(f"Step type changed from {self._type.name} to StepDataset")
        elif self._type is not StepType.StepImage and StepType.StepImage is value:
            _logger.debug(f"Step type changed from {self._type.name} to StepImage")
        elif self._type is not StepType.StepNumber and isinstance(value, (int, float)):
            _logger.debug(f"Step type changed from {self._type.name} to StepNumber")
        elif self._type is not StepType.StepString and isinstance(value, str):
            _logger.debug(f"Step type changed from {self._type.name} to StepString")

    @property
    def name(self) -> str:
        """The step's name.

        Returns:
            The step's name.
        """
        return self._name

    @property
    def id(self) -> int:
        """The step's id.

        Returns:
            The step's id.
        """
        return self._id

    @id.setter
    def id(self, step_id: int):
        """Set the step's id.

        Parameters:
            step_id: The id to set.
        """
        self._id = step_id

    @property
    def index(self) -> int:
        """The step's index.

        Returns:
            The step's index.
        """
        return self._index

    @property
    def slug(self) -> str:
        """The step's slug.

        Returns:
            The step's slug.
        """
        return self._slug

    @property
    def properties(self) -> dict:
        """The step's name, id, and index.

        Returns:
            A dictionary containing the `name`, `id` and `index` items.
        """
        return {"name": self.name, "id": self.id, "index": self.index}

    @property
    def artifacts(self) -> list[IterationStepArtifact]:
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts: list[IterationStepArtifact]):
        self._artifacts = artifacts

    @property
    def text(self) -> str | None:
        """The step's text.

        A string that is stored in the step.

        Returns:
            The step's text.
        """
        return self._text

    @property
    def connection(self) -> Connection:
        """The connection to which this step belongs.

        Returns:
            The connection to which this step belongs.
        """
        return self._iteration.connection

    @property
    def workspace(self) -> Workspace:
        """The workspace to which this step belongs.

        Returns:
            The workspace to which this step belongs.
        """
        return self._iteration.workspace

    @property
    def project(self) -> Project:
        """The project to which this step belongs.

        Returns:
            The project to which this step belongs.
        """
        return self._iteration.project

    @property
    def phase(self) -> Phase:
        """The phase to which this step belongs.

        Returns:
            The phase to which this step belongs.
        """
        return self._iteration.phase

    @property
    def iteration(self) -> Iteration:
        """The iteration to which this step belongs.

        Returns:
            The iteration to which this step belongs.
        """
        return self._iteration

    def _get_code_version_id(self):
        # TODO: cyclic imports
        from vectice.models.git_version import _check_code_source, _inform_if_git_repo

        if vectice.code_capture:
            return _check_code_source(self._client, self.project.id, _logger)
        else:
            _inform_if_git_repo()
            return None

    @property
    def model(self) -> Model | None:
        """The step's model.

        Returns:
            The step's model.
        """
        return self._model

    def _set_model_attachments(self, model: Model, model_version: ModelVersionOutput):
        logging.getLogger("vectice.models.attachment_container").propagate = True
        attachments = None
        if model.attachments:
            container = AttachmentContainer(model_version, self._client)
            attachments = container.add_attachments(model.attachments)
        if model.predictor:
            model_content = self._serialize_model(model.predictor)
            model_type_name = type(model.predictor).__name__
            container = AttachmentContainer(model_version, self._client)
            container.add_serialized_model(model_type_name, model_content)
        return attachments

    def _set_dataset_attachments(self, dataset: Dataset, dataset_version: DatasetVersionOutput):
        logging.getLogger("vectice.models.attachment_container").propagate = True
        attachments = None
        if dataset.attachments:
            container = AttachmentContainer(dataset_version, self._client)
            attachments = container.add_attachments(dataset.attachments)
        return attachments

    @staticmethod
    def _serialize_model(model: Any) -> bytes:
        return pickle.dumps(model)
