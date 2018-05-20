import time
from wsgiref.handlers import format_date_time

from mountapi.http.exceptions import HttpClientError
from mountapi.http.status import OK_200
from mountapi.lib import json


class Response:
    def __init__(self, content, status=None):
        if isinstance(content, str):
            self._content = content.encode()
        else:
            self._content = json.dumps(content).encode()
        self._status = status or OK_200

    @classmethod
    def from_result(cls, result):
        if isinstance(result, Response):
            return result
        else:
            return Response(result)

    @classmethod
    def from_http_client_error(cls, e: HttpClientError):
        return Response(e.message, status=e.status)

    def to_bytes(self) -> bytes:
        return (
            b'HTTP/1.1 %i %b\r\n'
            b'Date: %b\r\n'
            b'Connection: closed\r\n'
            b'Content-Type: application/json\r\n\r\n'
            b'%b' % (
                self._status['code'], self._status['reason'],
                format_date_time(time.time()).encode(),
                self._content,
            )
        )
