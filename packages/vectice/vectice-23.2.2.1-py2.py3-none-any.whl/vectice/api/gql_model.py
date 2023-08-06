from __future__ import annotations

from typing import TYPE_CHECKING

from gql import gql
from gql.transport.exceptions import TransportQueryError

from vectice.api.gql_api import GqlApi, Parser

if TYPE_CHECKING:
    from vectice.api.json.model_register import ModelRegisterInput, ModelRegisterOutput

_RETURNS = """
            modelVersion{
                          id
                          name
                          version
                          description
                          algorithmName
                          framework
                          modelId
                          model {
                            name
                            projectId
                          }
            }
            useExistingModel
            __typename
            """


class GqlModelApi(GqlApi):
    def register_model(
        self,
        data: ModelRegisterInput,
        project_id: int,
        phase_id: int | None = None,
        iteration_id: int | None = None,
    ) -> ModelRegisterOutput:
        variables = {"projectId": project_id, "data": data}
        kw = "projectId:$projectId,data:$data"
        variable_types = "$projectId:VecticeId!,$data:ModelRegisterInput!"
        if phase_id:
            variable_types += ",$phaseId:VecticeId!"
            kw += ",phaseId:$phaseId"
            variables["phaseId"] = phase_id
        if iteration_id:
            variable_types += ",$iterationId:VecticeId!"
            kw += ",iterationId:$iterationId"
            variables["iterationId"] = iteration_id
        query_name = "registerModel"
        query = GqlApi.build_query(
            gql_query=query_name,
            variable_types=variable_types,
            returns=_RETURNS,
            keyword_arguments=kw,
            query=False,
        )
        query_built = gql(query)
        try:
            response = self.execute(query_built, variables)
            model_output: ModelRegisterOutput = Parser().parse_item(response[query_name])
            return model_output
        except TransportQueryError as e:
            self._error_handler.handle_post_gql_error(e, "model", "register model")
