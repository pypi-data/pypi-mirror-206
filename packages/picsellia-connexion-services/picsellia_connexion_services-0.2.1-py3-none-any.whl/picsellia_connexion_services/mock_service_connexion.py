import re
from typing import IO, Any, Iterable, Mapping, Tuple, Union

from .abstract_service_connexion import AbstractServiceConnexion
from .exceptions import MockResponseNotDefinedError


class ResponseDictionary:
    def __init__(self) -> None:
        self.default_responses = {}
        self.responses = {
            "get": {},
            "xget": {},
            "patch": {},
            "put": {},
            "post": {},
            "delete": {},
        }

    @staticmethod
    def handle_keywords(path):
        return path.replace(
            "<uuid>",
            "[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
        )

    def set_default_response(self, method: str, response: Any) -> None:
        self.default_responses[method] = response

    def set_response(self, method: str, regex_path: str, response: Any) -> None:
        self.responses[method][self.handle_keywords(regex_path)] = response

    def get_response(self, method: str, path: str) -> Any:
        available_responses = self.responses[method]
        for regex_path, response in available_responses.items():
            if re.fullmatch(regex_path, path):
                return response

        if method in self.default_responses:
            return self.default_responses[method]
        else:
            raise MockResponseNotDefinedError(
                method=method, path=path, known_paths=available_responses.keys()
            )


class MockServiceConnexion(AbstractServiceConnexion):
    def __init__(self) -> None:
        """MockServiceConnexion can be used to answer fake requests"""
        self.response_dictionary = ResponseDictionary()

    def set_default_response(self, method: str, response: Any):
        self.response_dictionary.set_default_response(method, response)

    def set_response(self, method: str, regex_path: str, response: Any):
        self.response_dictionary.set_response(method, regex_path, response)

    def get(self, path: str, params: dict = None, stream=False):
        return self.response_dictionary.get_response("get", path)

    def xget(
        self,
        path: str,
        data: Union[
            None, str, bytes, Mapping[str, Any], Iterable[Tuple[str, str, None]], IO
        ] = None,
        params: dict = None,
        stream=False,
    ):
        return self.response_dictionary.get_response("xget", path)

    def post(
        self,
        path: str,
        data: Union[
            None, str, bytes, Mapping[str, Any], Iterable[Tuple[str, str, None]], IO
        ] = None,
        params: dict = None,
        files: Any = None,
    ):
        return self.response_dictionary.get_response("post", path)

    def patch(
        self,
        path: str,
        data: Union[
            None, str, bytes, Mapping[str, Any], Iterable[Tuple[str, str, None]], IO
        ] = None,
        params: dict = None,
    ):
        return self.response_dictionary.get_response("patch", path)

    def put(
        self,
        path: str,
        data: Union[
            None, str, bytes, Mapping[str, Any], Iterable[Tuple[str, str, None]], IO
        ] = None,
        params: dict = None,
    ):
        return self.response_dictionary.get_response("put", path)

    def delete(
        self,
        path: str,
        data: Union[
            None, str, bytes, Mapping[str, Any], Iterable[Tuple[str, str, None]], IO
        ] = None,
        params: dict = None,
    ):
        return self.response_dictionary.get_response("delete", path)
