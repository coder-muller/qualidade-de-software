import os

import pytest

pytest_plugins = ["tests.bdd.steps_comuns"]


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }


@pytest.fixture
def credenciais():
    return {
        "email": os.environ.get("LOCAL_EATS_EMAIL", "teste@teste.com"),
        "password": os.environ.get("LOCAL_EATS_PASSWORD", "123"),
    }
