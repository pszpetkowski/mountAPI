import pytest

from mountapi.http.request import Request
from mountapi.routing import Route, Router
from mountapi.schema import Schema


async def hello_param(name: str):
    return {'message': f'Hello {name}!'}


async def hello_post(request: Request):
    return {'message': f'Hello {request.POST["name"]}'}


async def hello_static():
    return {'message': 'Hello'}


routes = [
    Route('/hello-post/', hello_post, methods=['POST']),
    Route('/hello-static/', hello_static),
    Route('/hello/<name:str>/', hello_param)
]


@pytest.fixture(scope='session')
def schema():
    schema = Schema(routes)
    schema.build()
    return schema


@pytest.fixture(scope='session')
def router(schema):
    return Router(schema)
