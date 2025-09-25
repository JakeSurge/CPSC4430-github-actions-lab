import pytest
from app import app

@pytest.fixture()
def client():
    return app.test_client()


def test_home(client):
    response = client.get("/")

    assert b"Best Calculator Site Ever" in response.data, "Home page is missing title"


def test_add(client):
    response = client.get("/add?a=1&b=2")

    assert b"The sum is 3" in response.data, "Adding page is not adding correctly"


def test_subtract(client):
    response = client.get("/subtract?a=1&b=2")

    assert b"The difference is -1" in response.data, "Subtracting page is not subtracting correctly"


def test_multiply(client):
    response = client.get("/multiply?a=1&b=2")

    assert b"The product is 2" in response.data, "Multiplying page is not multiplying correctly"


def test_divide(client):
    response = client.get("/divide?a=1&b=2")

    assert b"The quotient is 0.5" in response.data, "Dividing page is not dividing correctly"
