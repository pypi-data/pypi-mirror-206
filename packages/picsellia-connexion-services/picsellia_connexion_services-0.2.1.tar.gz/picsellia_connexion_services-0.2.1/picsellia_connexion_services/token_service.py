from typing import IO, Any, Iterable, Mapping, Tuple, Union
from urllib.parse import urljoin

import requests

from .abstract_service_connexion import AbstractServiceConnexion


class TokenServiceConnexion(AbstractServiceConnexion):
    def __init__(
        self,
        host: str,
        api_token: str,
        authorization_key: str = "Token",
        content_type: str = "application/json",
    ) -> None:
        """TokenServiceConnexion may be used to handle a Token authentication connexion with a service.
        You need to give an api token valid, recognized by the service called
        """
        self.host = host
        self.api_token = api_token
        self.headers = {
            "Authorization": authorization_key + " " + api_token,
            "Content-type": content_type,
        }
        self.session = requests.Session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session is not None:
            self.session.close()

    def add_header(self, key: str, value: str):
        if key is None or value is None:
            raise RuntimeError("Header key and value cannot be None")
        self.headers[key] = value

    def get(self, path: str, params: dict = None, stream=False):
        url = urljoin(self.host, path)
        return self.session.get(
            url=url, headers=self.headers, params=params, stream=stream
        )

    def xget(
        self,
        path: str,
        data: Union[
            None, str, bytes, Mapping[str, Any], Iterable[Tuple[str, str, None]], IO
        ] = None,
        params: dict = None,
        stream=False,
    ):
        url = urljoin(self.host, path)
        return self.session.request(
            method="XGET",
            url=url,
            data=data,
            headers=self.headers,
            params=params,
            stream=stream,
        )

    def post(
        self,
        path: str,
        data: Union[
            None, str, bytes, Mapping[str, Any], Iterable[Tuple[str, str, None]], IO
        ] = None,
        params: dict = None,
        files: Any = None,
    ):
        url = urljoin(self.host, path)
        return self.session.post(
            url=url, data=data, headers=self.headers, params=params, files=files
        )

    def patch(
        self,
        path: str,
        data: Union[
            None, str, bytes, Mapping[str, Any], Iterable[Tuple[str, str, None]], IO
        ] = None,
        params: dict = None,
    ):
        url = urljoin(self.host, path)
        return self.session.patch(
            url=url, data=data, headers=self.headers, params=params
        )

    def put(
        self,
        path: str,
        data: Union[
            None, str, bytes, Mapping[str, Any], Iterable[Tuple[str, str, None]], IO
        ] = None,
        params: dict = None,
    ):
        url = urljoin(self.host, path)
        return self.session.put(url=url, data=data, headers=self.headers, params=params)

    def delete(
        self,
        path: str,
        data: Union[
            None, str, bytes, Mapping[str, Any], Iterable[Tuple[str, str, None]], IO
        ] = None,
        params: dict = None,
    ):
        url = urljoin(self.host, path)
        return self.session.delete(
            url=url, data=data, headers=self.headers, params=params
        )
