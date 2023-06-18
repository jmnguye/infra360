import pytest
import json
from app import create_app
from app.models.domain import DomainDAO
from typing import Callable, Iterable
from flask import Flask
from flask.testing import FlaskClient
from _pytest._py.path import LocalPath


def db_session(tmpdir_factory: Callable) -> LocalPath:
    DOMAINS = {
        "domains": [
            json.dumps(DomainDAO(1, "Compute", "Compute").__dict__),
            json.dumps(DomainDAO(2, "Network", "Network").__dict__),
            json.dumps(DomainDAO(3, "Storage", "Storage").__dict__),
        ]
    }
    tmp_file = tmpdir_factory.mktemp("temp").join("test.db")
    with tmp_file.open("w") as f:
        json.dump(DOMAINS, f)
    return tmp_file


@pytest.fixture(scope="session")
def app(tmpdir_factory: Callable) -> Iterable[Flask]:
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )
    db_session(tmpdir_factory)
    yield app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture
def db_init(tmpdir_factory: Callable) -> LocalPath:
    return db_session(tmpdir_factory)
