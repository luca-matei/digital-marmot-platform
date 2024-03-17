from pydantic import BaseModel
from bs4 import BeautifulSoup
from lxml import etree

import orjson
import aiohttp


class HTTPResponse(BaseModel):
    status: int
    headers: dict
    body: str

    @property
    def json(self) -> dict:  # noqa
        return orjson.loads(self.body)

    @property
    def tree(self) -> etree.HTML:
        return etree.HTML(self.content)

    @property
    def soup(self) -> BeautifulSoup:
        return BeautifulSoup(self.content, "lxml")


class HTTPClient:
    def __init__(self, base_url: str = None, headers: dict = None):
        self.base_url = base_url or ""
        self.headers = headers or {}
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(headers=self.headers)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    @staticmethod
    async def _http_response(raw: aiohttp.ClientResponse) -> HTTPResponse:
        body = await raw.text()
        return HTTPResponse(
            status=raw.status,
            headers=raw.headers,
            body=body,
        )

    async def get(self, url: str, params: dict = None):
        async with self.session.get(self.base_url + url, params=params) as response:
            return await self._http_response(response)

    async def post(self, url: str, data: dict = None):
        async with self.session.post(self.base_url + url, data=data) as response:
            return await self._http_response(response)

    async def put(self, url: str, data: dict = None):
        async with self.session.put(self.base_url + url, data=data) as response:
            return await self._http_response(response)

    async def delete(self, url: str):
        async with self.session.delete(self.base_url + url) as response:
            return await self._http_response(response)
