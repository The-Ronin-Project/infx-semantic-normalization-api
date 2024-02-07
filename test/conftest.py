import pytest
from infx_mapping_api import app


@pytest.fixture()
def application():
    application = app.create_app()
    application.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield application

    # clean up / reset resources here


@pytest.fixture()
def client(application):
    return application.test_client()
