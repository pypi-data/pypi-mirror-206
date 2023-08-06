from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from gql import gql
from gql.transport.exceptions import TransportQueryError

from vectice.api.gql_api import GqlApi, Parser

if TYPE_CHECKING:
    from vectice.api.json.dataset_register import DatasetRegisterInput, DatasetRegisterOutput


_logger = logging.getLogger(__name__)

# TODO JobRun for lineages
_RETURNS = """
            datasetVersion {
                          id
                          name
                          dataSet {
                            name
                            projectId
                          }
            }
            useExistingDataset
            useExistingVersion
            __typename
            """


class GqlDatasetApi(GqlApi):
    def register_dataset(
        self,
        data: DatasetRegisterInput,
        project_id: int | None = None,
        phase_id: int | None = None,
        iteration_id: int | None = None,
    ) -> DatasetRegisterOutput:
        if phase_id and project_id and not iteration_id:
            variable_types = "$projectId:VecticeId!,$phaseId:VecticeId!,$data:DatasetRegisterInput!"
            kw = "projectId:$projectId,phaseId:$phaseId,data:$data"
            variables = {"projectId": project_id, "phaseId": phase_id, "data": data}
        elif project_id and phase_id and iteration_id:
            variable_types = (
                "$projectId:VecticeId!,$phaseId:VecticeId!,$iterationId:VecticeId!,$data:DatasetRegisterInput!"
            )
            kw = "projectId:$projectId,phaseId:$phaseId,iterationId:$iterationId,data:$data"
            variables = {"projectId": project_id, "phaseId": phase_id, "iterationId": iteration_id, "data": data}
        elif project_id:
            variable_types = "$projectId:VecticeId!,$data:DatasetRegisterInput!"
            kw = "projectId:$projectId,data:$data"
            variables = {"projectId": project_id, "data": data}
        else:
            raise RuntimeError("The provided parent child ids do not match.")

        query = GqlApi.build_query(
            gql_query="registerDataset",
            variable_types=variable_types,
            returns=_RETURNS,
            keyword_arguments=kw,
            query=False,
        )
        query_built = gql(query)
        try:
            response = self.execute(query_built, variables)
            dataset_output: DatasetRegisterOutput = Parser().parse_item(response["registerDataset"])
            return dataset_output
        except TransportQueryError as e:
            self._error_handler.handle_post_gql_error(e, "dataset", "register dataset")
