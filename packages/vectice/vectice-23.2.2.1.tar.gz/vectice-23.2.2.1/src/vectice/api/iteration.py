from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from gql import gql
from gql.transport.exceptions import TransportQueryError

from vectice.api.gql_api import GqlApi, Parser

if TYPE_CHECKING:
    from vectice.api.json.iteration import IterationInput, IterationOutput

_logger = logging.getLogger(__name__)

_RETURNS = """id
            index
            status
            phase {
                    id
                    name
                    status
                    __typename
              }
            steps {
                    slug
                    id
                    name
                    stepType
                    artifacts {
                    type
                    datasetVersionId
                    }
            }
            __typename
            """

_RETURNS_LAST_ASSETS = """id
            index
            status
            phase {
                    id
                    name
                    status
                    __typename
                    parent {
                            id
                            name
                            __typename
                            workspace{
                                    id
                                    name
                                    __typename
                            }
                    }
              }
              steps{
                    slug
                    id
                    name
                    index
                    completed
                    updatedDate
                    __typename
              }
            __typename
            """


class IterationApi(GqlApi):
    def list_iterations(self, parent_id: int) -> list[IterationOutput]:
        alias_filter = {"phaseId": parent_id, "search": ""}
        returns = f"""items{{
                                    {_RETURNS}
                        }}"""
        variable_types = "$filters:IterationFiltersInput!"
        kw = "filters:$filters"
        variables = {"filters": alias_filter}
        query = GqlApi.build_query(
            gql_query="getIterationList",
            variable_types=variable_types,
            returns=returns,
            keyword_arguments=kw,
            query=True,
        )
        query_built = gql(query)
        try:
            response = self.execute(query_built, variables)
            iterations_output: list[IterationOutput] = Parser().parse_list(response["getIterationList"]["items"])
            return iterations_output
        except TransportQueryError as e:
            self._error_handler.handle_post_gql_error(e, "iteration", "list")

    def create_iteration(self, phase_id: int) -> IterationOutput:
        gql_query = "createIteration"
        variable_types = "$phaseId:VecticeId!"
        variables = {"phaseId": phase_id}
        kw = "phaseId:$phaseId"
        query = GqlApi.build_query(
            gql_query=gql_query, variable_types=variable_types, returns=_RETURNS, keyword_arguments=kw, query=False
        )
        query_built = gql(query)
        try:
            response = self.execute(query_built, variables)
            iteration_output: IterationOutput = Parser().parse_item(response[gql_query])
            return iteration_output
        except TransportQueryError as e:
            self._error_handler.handle_post_gql_error(e, "iteration", phase_id)

    def get_iteration(self, iteration_id: int) -> IterationOutput:
        gql_query = "getIterationById"
        variable_types = "$id:VecticeId!"
        variables = {"id": iteration_id}
        kw = "id:$id"
        query = GqlApi.build_query(
            gql_query=gql_query, variable_types=variable_types, returns=_RETURNS, keyword_arguments=kw, query=True
        )
        query_built = gql(query)
        try:
            response = self.execute(query_built, variables)
            iteration_output: IterationOutput = Parser().parse_item(response[gql_query])
            return iteration_output
        except TransportQueryError as e:
            self._error_handler.handle_post_gql_error(e, "iteration", iteration_id)

    def get_iteration_last_assets(self, iteration_id: int) -> IterationOutput:
        gql_query = "getIterationById"
        variable_types = "$id:VecticeId!"
        variables = {"id": iteration_id}
        kw = "id:$id"
        query = GqlApi.build_query(
            gql_query=gql_query,
            variable_types=variable_types,
            returns=_RETURNS_LAST_ASSETS,
            keyword_arguments=kw,
            query=True,
        )
        query_built = gql(query)
        try:
            response = self.execute(query_built, variables)
            iteration_output: IterationOutput = Parser().parse_item(response[gql_query])
            return iteration_output
        except TransportQueryError as e:
            self._error_handler.handle_post_gql_error(e, "iteration", iteration_id)

    def get_iteration_by_index(self, phase_id: int, index: int) -> IterationOutput:
        gql_query = "getIterationByIndex"
        variable_types = "$index:Float!,$phaseId:VecticeId!"
        variables = {"index": index, "phaseId": phase_id}
        kw = "index:$index,phaseId:$phaseId"
        query = GqlApi.build_query(
            gql_query=gql_query, variable_types=variable_types, returns=_RETURNS, keyword_arguments=kw, query=True
        )
        query_built = gql(query)
        try:
            response = self.execute(query_built, variables)
            iteration_output: IterationOutput = Parser().parse_item(response[gql_query])
            return iteration_output
        except TransportQueryError as e:
            self._error_handler.handle_post_gql_error(e, "iteration_index", index)

    def update_iteration(self, iteration: IterationInput, iteration_id: int) -> IterationOutput:
        variable_types = "$id:VecticeId!,$data:IterationUpdateInput!"
        kw = "id:$id,data:$data"
        variables = {"id": iteration_id, "data": iteration}
        query = GqlApi.build_query(
            gql_query="updateIteration",
            variable_types=variable_types,
            returns=_RETURNS,
            keyword_arguments=kw,
            query=False,
        )
        query_built = gql(query)
        try:
            response = self.execute(query_built, variables)
            iteration_output: IterationOutput = Parser().parse_item(response["updateIteration"])
            return iteration_output
        except TransportQueryError as e:
            self._error_handler.handle_post_gql_error(e, "iteration", "put")

    def delete_iteration(self, iteration_id: int) -> None:
        variable_types = "$id:VecticeId!"
        kw = "id:$id"
        variables = {"id": iteration_id}
        query = GqlApi.build_query(
            gql_query="removeIteration",
            variable_types=variable_types,
            keyword_arguments=kw,
            query=False,
        )
        query_built = gql(query)
        try:
            self.execute(query_built, variables)
        except TransportQueryError as e:
            self._error_handler.handle_post_gql_error(e, "iteration", iteration_id)
