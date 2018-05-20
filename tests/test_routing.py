import pytest

from mountapi.http.exceptions import Http404
from mountapi.http.request import Request
from tests.conftest import hello_param, hello_post, hello_static


@pytest.mark.asyncio
async def test_hello_static_is_resolved_correctly(router):
    result = await router.dispatch(path='/hello-static/', method='GET')
    assert result['handler'] == hello_static
    assert result['param_names'] == {}
    assert result['param_values'] == {}


@pytest.mark.asyncio
async def test_hello_post_is_resolved_correctly(router):
    result = await router.dispatch(path='/hello-post/', method='POST')
    assert result['handler'] == hello_post
    assert result['param_names'] == {Request: 'request'}
    assert result['param_values'] == {}


@pytest.mark.asyncio
async def test_hello_param_is_resolved_correctly(router):
    result = await router.dispatch(path='/hello/test/', method='GET')
    assert result['handler'] == hello_param
    assert result['param_names'] == {str: 'name'}
    assert result['param_values'] == {'name': 'test'}


@pytest.mark.asyncio
async def test_wrong_url_results_in_404_exception(router):
    with pytest.raises(Http404):
        await router.dispatch(path='/wrong-url/', method='GET')
