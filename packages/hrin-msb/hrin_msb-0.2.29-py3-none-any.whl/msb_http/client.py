from typing import (List, Dict)

from requests.models import Response

from .dataclasses import (ApiRequestData, ApiResponseWrapper)
from .utils import make_api_request


class ApiRequestClient(ApiRequestData):

	@property
	def request_is_json(self) -> bool:
		return True

	def GET(self, query_params: [List | Dict] = None, endpoint: str = None):
		return self.set_query_params(params=query_params).set_request_method("GET").set_endpoint(endpoint)

	def POST(self, data: [List | Dict] = None, query_params: [List | Dict] = None, endpoint: str = None):
		return self.set_data(data=data).set_query_params(params=query_params).set_request_method("POST").set_endpoint(endpoint)

	def PUT(self, data: [List | Dict] = None, query_params: [List | Dict] = None, endpoint: str = None):
		return self.set_data(data=data).set_query_params(params=query_params).set_request_method("PUT").set_endpoint(endpoint)

	def DELETE(self, data: [List | Dict] = None, query_params: [List | Dict] = None, endpoint: str = None):
		return self.set_data(data=data).set_query_params(params=query_params).set_request_method("DELETE").set_endpoint(endpoint)

	def get_result(self) -> ApiResponseWrapper:
		try:
			_response = make_api_request(self)
		except Exception as e:
			_response = ApiResponseWrapper(Response())
		return _response
