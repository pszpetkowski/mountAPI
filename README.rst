mountAPI
========

Installation
============

According to your preference you can either perform an installation with pip:

.. code-block:: text

    pip install mountapi

Or pipenv

.. code-block:: text

    pipenv install --pre mountapi

Example
=======

.. code-block:: python

    from mountapi.core.app import Application
    from mountapi.core.settings import DefaultSettings
    from mountapi.routing import Route


    async def hello_person(name: str):
        return {'message': f'Hello {name}!'}


    routes = [
        Route('/hello/<name:str>/', hello_person)
    ]

    if __name__ == '__main__':
        app = Application(settings=DefaultSettings, routes=routes)
        app.run()
