from collections import MutableMapping
from typing import Dict, List, NewType

from urllib.parse import parse_qs

import httptools

QueryDict = NewType('QueryDict', Dict[str, List[str]])


class CaseInsensitiveDict(MutableMapping):
    def __init__(self):
        self._store = {}

    def __contains__(self, item):
        return item.lower() in self._store

    def __delitem__(self, key):
        del self._store[key.lower()]

    def __getitem__(self, item):
        return self._store[item.lower()]

    def __iter__(self):
        return iter(self._store)

    def __len__(self):
        return len(self._store)

    def __setitem__(self, key, value):
        self._store[key.lower()] = value

    def __repr__(self):
        return self._store.__repr__()


class Request:
    def __init__(self):
        self.method: str = ''
        self.path: str = ''
        self.headers: CaseInsensitiveDict = CaseInsensitiveDict()
        self.handler = None

        self.GET: QueryDict = {}
        self.POST = {}

    def parse_url(self, url: bytes) -> None:
        parsed_url = httptools.parse_url(url)
        self.path = parsed_url.path.decode()

        query_params = parsed_url.query
        if query_params:
            self.GET.update(parse_qs(query_params.decode()))

    def parse_header(self, name: bytes, value: bytes) -> None:
        self.headers[name.decode()] = value.decode()

    async def handle(self):
        response = await self.handler()
        return response
