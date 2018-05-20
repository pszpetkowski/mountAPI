from mountapi.http import status as http_status


class HttpError(Exception):
    DEFAULT_MESSAGE = 'An error has occurred.'

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE


class HttpClientError(HttpError):
    status: dict


class Http404(HttpClientError):
    status: dict = http_status.NOT_FOUND_404
