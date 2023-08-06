from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, BinaryIO, NoReturn

from vectice.api.http_error_handlers import InvalidReferenceError
from vectice.api.json import AttachmentOutput, ModelVersionOutput, PagedResponse
from vectice.api.json.dataset_version import DatasetVersionOutput
from vectice.api.rest_api import HttpError, RestApi

if TYPE_CHECKING:
    from io import BytesIO

    from requests import Response


MODEL_VERSION = "model version"
DATASET_VERSION = "dataset version"


_logger = logging.getLogger(__name__)


class AttachmentApi(RestApi):
    def _generate_model_url_and_id(self, model_version: ModelVersionOutput) -> tuple[str, str | None]:
        try:
            model_name = model_version.model.name
            version_name = model_version.name
            url = self._build_url(model_version.model.project_id, model_version.id, "modelversion")
            model_repr = f"Model(name='{model_name}', version='{version_name}')"
            return url, model_repr
        except HttpError as e:
            self._handle_http_error(e, model_version)

    def _generate_dataset_url_and_id(self, dataset_version: DatasetVersionOutput) -> tuple[str, str | None]:
        try:
            dataset_name = dataset_version.dataset.name
            version_name = dataset_version.name
            url = self._build_url(dataset_version.dataset.project_id, dataset_version.id, "datasetversion")
            dataset_repr = f"Dataset(name='{dataset_name}', version='{version_name}')"
            return url, dataset_repr
        except HttpError as e:
            self._handle_http_error(e, dataset_version)

    def _generate_version_url_and_id(
        self, version: ModelVersionOutput | DatasetVersionOutput
    ) -> tuple[str, str | None]:
        if isinstance(version, ModelVersionOutput):
            return self._generate_model_url_and_id(version)

        return self._generate_dataset_url_and_id(version)

    @staticmethod
    def _build_url(project_id: int, version: int, type: str) -> str:
        return f"/metadata/project/{project_id}/entityfiles/{type}/{version}"

    def post_attachment(
        self, files: list[tuple[str, tuple[str, BinaryIO]]], version: ModelVersionOutput | DatasetVersionOutput
    ) -> list[dict]:
        entity_files = []
        try:
            url, repr = self._generate_version_url_and_id(version)
            if len(files) == 1:
                response = self._post_attachments(url, files)
                if response:
                    entity_files.append(response.json())
                _logger.debug(f"Attachment with name: {files[0][1][0]} successfully attached to {repr}.")
            elif len(files) > 1:
                for file in files:
                    response = self._post_attachments(url, [file])
                    if response:
                        entity_files.append(response.json())
                _logger.debug(f"Attachments with names: {[f[1][0] for f in files]} successfully attached to {repr}.")
            return entity_files
        except HttpError as e:
            self._handle_http_error(e, version)

    def post_model_predictor(self, model_type: str, model_content: BytesIO, model_version: ModelVersionOutput) -> None:
        url, model_repr = self._generate_model_url_and_id(model_version)
        url += f"?modelFramework={model_type}"
        attachment = ("file", ("model_pickle", model_content))
        self._post_attachments(url, [attachment])
        _logger.info(f"Model {model_type} successfully attached to {model_repr}.")

    def _identify_object(self, code_version_id: int | None = None, phase_id: int | None = None) -> tuple:
        if phase_id:
            return "phase", phase_id
        elif code_version_id:
            return "codeversion", code_version_id
        else:
            raise ValueError("No ID was provided for create attachment.")

    def create_attachments(
        self,
        files: list[tuple[str, tuple[str, Any]]],
        project_id: int,
        code_version_id: int | None = None,
        phase_id: int | None = None,
    ) -> list[dict]:
        parent_object, object_id = self._identify_object(code_version_id, phase_id)
        entity_files = []
        try:
            for file in files:
                response = self._post_attachments(
                    f"/metadata/project/{project_id}/entityfiles/{parent_object}/{object_id}", [file]
                )
                if response:
                    entity_files.append(response.json())
            _logger.debug(
                f"Attachments with names: {[f[1][0] for f in files]} successfully attached to {parent_object} {object_id}."
            )
            return entity_files
        except HttpError as e:
            self._handle_code_version_error(e, object_id)

    def get_code_version_attachment(self, code_version_id: int, project_id: int, file_id: int) -> Response:
        try:
            return self._get_attachment(
                f"/metadata/project/{project_id}/entityfiles/codeversion/{code_version_id}/{file_id}"
            )
        except HttpError as e:
            self._handle_code_version_error(e, code_version_id)

    def list_attachments(self, version: ModelVersionOutput | DatasetVersionOutput) -> PagedResponse[AttachmentOutput]:
        try:
            url, repr = self._generate_version_url_and_id(version)
            if url is None:
                raise InvalidReferenceError(MODEL_VERSION, version.id)
            attachments = self._list_attachments(url)
        except HttpError as e:
            self._handle_http_error(e, version)
        return PagedResponse(
            item_cls=AttachmentOutput,
            total=len(attachments),
            page={},
            items=attachments,
        )

    def list_object_attachments(
        self, project_id: int, code_version_id: int | None = None, phase_id: int | None = None
    ) -> PagedResponse[AttachmentOutput]:
        parent_object, object_id = self._identify_object(code_version_id, phase_id)
        try:
            attachments = self._list_attachments(
                f"/metadata/project/{project_id}/entityfiles/{parent_object}/{object_id}"
            )
        except HttpError as e:
            self._handle_code_version_error(e, object_id)
        return PagedResponse(
            item_cls=AttachmentOutput,
            total=len(attachments),
            page={},
            items=attachments,
        )

    def list_phase_attachments(self, phase_id: int, project_id: int) -> PagedResponse[AttachmentOutput]:
        try:
            attachments = self._list_attachments(f"/metadata/project/{project_id}/entityfiles/phase/{phase_id}")
        except HttpError as e:
            self._handle_code_version_error(e, phase_id)
        return PagedResponse(
            item_cls=AttachmentOutput,
            total=len(attachments),
            page={},
            items=attachments,
        )

    def _handle_http_error(self, error: HttpError, version: ModelVersionOutput | DatasetVersionOutput) -> NoReturn:
        ref_type = MODEL_VERSION if isinstance(version, ModelVersionOutput) else DATASET_VERSION
        self._httpErrorHandler.handle_get_http_error(error, ref_type, version.id)

    def _handle_code_version_error(self, error: HttpError, code_version_id: int) -> NoReturn:
        self._httpErrorHandler.handle_get_http_error(error, "code version", code_version_id)
