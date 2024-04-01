# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
import grpc  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import path_template
from google.api_core import gapic_v1

from google.protobuf import json_format
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from requests import __version__ as requests_version
import dataclasses
import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore


from google.cloud.aiplatform_v1beta1.types import vertex_rag_service
from google.longrunning import operations_pb2  # type: ignore

from .base import (
    VertexRagServiceTransport,
    DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO,
)


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class VertexRagServiceRestInterceptor:
    """Interceptor for VertexRagService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the VertexRagServiceRestTransport.

    .. code-block:: python
        class MyCustomVertexRagServiceInterceptor(VertexRagServiceRestInterceptor):
            def pre_retrieve_contexts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_retrieve_contexts(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = VertexRagServiceRestTransport(interceptor=MyCustomVertexRagServiceInterceptor())
        client = VertexRagServiceClient(transport=transport)


    """

    def pre_retrieve_contexts(
        self,
        request: vertex_rag_service.RetrieveContextsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[vertex_rag_service.RetrieveContextsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for retrieve_contexts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VertexRagService server.
        """
        return request, metadata

    def post_retrieve_contexts(
        self, response: vertex_rag_service.RetrieveContextsResponse
    ) -> vertex_rag_service.RetrieveContextsResponse:
        """Post-rpc interceptor for retrieve_contexts

        Override in a subclass to manipulate the response
        after it is returned by the VertexRagService server but before
        it is returned to user code.
        """
        return response

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[locations_pb2.GetLocationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VertexRagService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the VertexRagService server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[locations_pb2.ListLocationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VertexRagService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the VertexRagService server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VertexRagService server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the VertexRagService server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VertexRagService server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the VertexRagService server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[iam_policy_pb2.TestIamPermissionsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VertexRagService server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the VertexRagService server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.CancelOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VertexRagService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the VertexRagService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VertexRagService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the VertexRagService server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.GetOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VertexRagService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the VertexRagService server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.ListOperationsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VertexRagService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the VertexRagService server but before
        it is returned to user code.
        """
        return response

    def pre_wait_operation(
        self,
        request: operations_pb2.WaitOperationRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[operations_pb2.WaitOperationRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for wait_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VertexRagService server.
        """
        return request, metadata

    def post_wait_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for wait_operation

        Override in a subclass to manipulate the response
        after it is returned by the VertexRagService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class VertexRagServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: VertexRagServiceRestInterceptor


class VertexRagServiceRestTransport(VertexRagServiceTransport):
    """REST backend transport for VertexRagService.

    A service for retrieving relevant contexts.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    NOTE: This REST transport functionality is currently in a beta
    state (preview). We welcome your feedback via an issue in this
    library's source repository. Thank you!
    """

    def __init__(
        self,
        *,
        host: str = "aiplatform.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[VertexRagServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        NOTE: This REST transport functionality is currently in a beta
        state (preview). We welcome your feedback via a GitHub issue in
        this library's repository. Thank you!

         Args:
             host (Optional[str]):
                  The hostname to connect to (default: 'aiplatform.googleapis.com').
             credentials (Optional[google.auth.credentials.Credentials]): The
                 authorization credentials to attach to requests. These
                 credentials identify the application to the service; if none
                 are specified, the client will attempt to ascertain the
                 credentials from the environment.

             credentials_file (Optional[str]): A file with credentials that can
                 be loaded with :func:`google.auth.load_credentials_from_file`.
                 This argument is ignored if ``channel`` is provided.
             scopes (Optional(Sequence[str])): A list of scopes. This argument is
                 ignored if ``channel`` is provided.
             client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                 certificate to configure mutual TLS HTTP channel. It is ignored
                 if ``channel`` is provided.
             quota_project_id (Optional[str]): An optional project to use for billing
                 and quota.
             client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                 The client info used to send a user-agent string along with
                 API requests. If ``None``, then default info will be used.
                 Generally, you only need to set this if you are developing
                 your own client library.
             always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                 be used for service account credentials.
             url_scheme: the protocol scheme for the API endpoint.  Normally
                 "https", but for testing or local servers,
                 "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(
                f"Unexpected hostname structure: {host}"
            )  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or VertexRagServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _RetrieveContexts(VertexRagServiceRestStub):
        def __hash__(self):
            return hash("RetrieveContexts")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {
                k: v
                for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items()
                if k not in message_dict
            }

        def __call__(
            self,
            request: vertex_rag_service.RetrieveContextsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> vertex_rag_service.RetrieveContextsResponse:
            r"""Call the retrieve contexts method over HTTP.

            Args:
                request (~.vertex_rag_service.RetrieveContextsRequest):
                    The request object. Request message for
                [VertexRagService.RetrieveContexts][google.cloud.aiplatform.v1beta1.VertexRagService.RetrieveContexts].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.vertex_rag_service.RetrieveContextsResponse:
                    Response message for
                [VertexRagService.RetrieveContexts][google.cloud.aiplatform.v1beta1.VertexRagService.RetrieveContexts].

            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{parent=projects/*/locations/*}:retrieveContexts",
                    "body": "*",
                },
            ]
            request, metadata = self._interceptor.pre_retrieve_contexts(
                request, metadata
            )
            pb_request = vertex_rag_service.RetrieveContextsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request["body"], use_integers_for_enums=False
            )
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=False,
                )
            )
            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = vertex_rag_service.RetrieveContextsResponse()
            pb_resp = vertex_rag_service.RetrieveContextsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_retrieve_contexts(resp)
            return resp

    @property
    def retrieve_contexts(
        self,
    ) -> Callable[
        [vertex_rag_service.RetrieveContextsRequest],
        vertex_rag_service.RetrieveContextsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RetrieveContexts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(VertexRagServiceRestStub):
        def __call__(
            self,
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> locations_pb2.Location:

            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*}",
                },
            ]

            request, metadata = self._interceptor.pre_get_location(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = locations_pb2.Location()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_get_location(resp)
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(VertexRagServiceRestStub):
        def __call__(
            self,
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> locations_pb2.ListLocationsResponse:

            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*}/locations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*}/locations",
                },
            ]

            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_list_locations(resp)
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(VertexRagServiceRestStub):
        def __call__(
            self,
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> policy_pb2.Policy:

            r"""Call the get iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featurestores/*}:getIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featurestores/*/entityTypes/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/models/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/endpoints/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/notebookRuntimeTemplates/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/publishers/*/models/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featureOnlineStores/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featurestores/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featurestores/*/entityTypes/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/models/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/endpoints/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/notebookRuntimeTemplates/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/publishers/*/models/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featureOnlineStores/*}:getIamPolicy",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:getIamPolicy",
                },
            ]

            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            body = json.dumps(transcoded_request["body"])
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = policy_pb2.Policy()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_get_iam_policy(resp)
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(VertexRagServiceRestStub):
        def __call__(
            self,
            request: iam_policy_pb2.SetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> policy_pb2.Policy:

            r"""Call the set iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featurestores/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featurestores/*/entityTypes/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/models/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/endpoints/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/notebookRuntimeTemplates/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featureOnlineStores/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featurestores/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featurestores/*/entityTypes/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/models/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/endpoints/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/notebookRuntimeTemplates/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featureOnlineStores/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:setIamPolicy",
                    "body": "*",
                },
            ]

            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            body = json.dumps(transcoded_request["body"])
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = policy_pb2.Policy()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_set_iam_policy(resp)
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    class _TestIamPermissions(VertexRagServiceRestStub):
        def __call__(
            self,
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> iam_policy_pb2.TestIamPermissionsResponse:

            r"""Call the test iam permissions method over HTTP.

            Args:
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featurestores/*}:testIamPermissions",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featurestores/*/entityTypes/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/models/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/endpoints/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/notebookRuntimeTemplates/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featureOnlineStores/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{resource=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featurestores/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featurestores/*/entityTypes/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/models/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/endpoints/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/notebookRuntimeTemplates/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featureOnlineStores/*}:testIamPermissions",
                },
                {
                    "method": "post",
                    "uri": "/ui/{resource=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:testIamPermissions",
                },
            ]

            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            body = json.dumps(transcoded_request["body"])
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(VertexRagServiceRestStub):
        def __call__(
            self,
            request: operations_pb2.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> None:

            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/extensions/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/deployments/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:cancel",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:cancel",
                },
            ]

            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(VertexRagServiceRestStub):
        def __call__(
            self,
            request: operations_pb2.DeleteOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> None:

            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*}/operations",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/extensions/*}/operations",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/deployments/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/solvers/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                },
            ]

            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(VertexRagServiceRestStub):
        def __call__(
            self,
            request: operations_pb2.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:

            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/edgeDeploymentJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/extensions/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/deployments/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/solvers/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}",
                },
            ]

            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = operations_pb2.Operation()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_get_operation(resp)
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(VertexRagServiceRestStub):
        def __call__(
            self,
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.ListOperationsResponse:

            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/endpoints/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/extensions/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/customJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/indexes/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/migratableResources/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/models/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/persistentResources/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/schedules/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/specialistPools/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                },
                {
                    "method": "get",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/deployments/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/solvers/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*}/operations",
                },
            ]

            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_list_operations(resp)
            return resp

    @property
    def wait_operation(self):
        return self._WaitOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _WaitOperation(VertexRagServiceRestStub):
        def __call__(
            self,
            request: operations_pb2.WaitOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> operations_pb2.Operation:

            r"""Call the wait operation method over HTTP.

            Args:
                request (operations_pb2.WaitOperationRequest):
                    The request object for WaitOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                operations_pb2.Operation: Response from WaitOperation method.
            """

            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/edgeDevices/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/endpoints/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/extensionControllers/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/extensions/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/customJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tuningJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/indexes/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/modelMonitors/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/migratableResources/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/persistentResources/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/schedules/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/specialistPools/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/ui/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/savedQueries/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/datasets/*/dataItems/*/annotations/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/edgeDevices/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/endpoints/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/evaluationTasks/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/exampleStores/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensionControllers/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/extensions/*/deployments/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featurestores/*/entityTypes/*/features/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/customJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/dataLabelingJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/hyperparameterTuningJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexes/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/indexEndpoints/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/artifacts/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/contexts/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/metadataStores/*/executions/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/modelMonitors/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/migratableResources/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/persistentResources/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/studies/*/trials/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/trainingPipelines/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/pipelineJobs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/schedules/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/specialistPools/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/tensorboards/*/experiments/*/runs/*/timeSeries/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/operations/*}:wait",
                },
                {
                    "method": "post",
                    "uri": "/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*/operations/*}:wait",
                },
            ]

            request, metadata = self._interceptor.pre_wait_operation(request, metadata)
            request_kwargs = json_format.MessageToDict(request)
            transcoded_request = path_template.transcode(http_options, **request_kwargs)

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]

            # Jsonify the query params
            query_params = json.loads(json.dumps(transcoded_request["query_params"]))

            # Send the request
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"

            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            resp = operations_pb2.Operation()
            resp = json_format.Parse(response.content.decode("utf-8"), resp)
            resp = self._interceptor.post_wait_operation(resp)
            return resp

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("VertexRagServiceRestTransport",)
