import time
from wsgiref.handlers import format_date_time

from mountapi.http.exceptions import HttpClientError
from mountapi.http.status import Status, HTTP_200_OK
from mountapi.lib import json


class Response:
    def __init__(self, content=None, status: Status = None):
        if isinstance(content, str):
            self._content = content.encode()
        elif isinstance(content, dict):
            self._content = json.dumps(content).encode()
        elif content is not None:
            raise ValueError('Response can only be made using str or dict')
        else:
            self._content = None
        self._status: Status = status or HTTP_200_OK

    @classmethod
    def from_result(cls, result):
        if isinstance(result, Response):
            return result
        else:
            return Response(result)

    @classmethod
    def from_http_client_error(cls, e: HttpClientError):
        return Response(e.message, e.status)

    def to_bytes(self) -> bytes:
        return (
            b'HTTP/1.1 %i %b\r\n'
            b'Date: %b\r\n'
            b'Connection: closed\r\n'
            b'Content-Type: application/json\r\n\r\n'
            b'%b' % (
                self._status.code, self._status.reason,
                format_date_time(time.time()).encode(),
                self._content,
            )
        )
