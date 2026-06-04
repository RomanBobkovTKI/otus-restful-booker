import pytest
from config.settings import settings
from clients.auth_client import AuthClient
from clients.booking_client import BookingClient


@pytest.fixture
def auth_client():
    return AuthClient(settings.BASE_URL)


@pytest.fixture
def booking_client():
    return BookingClient(settings.BASE_URL)


@pytest.fixture
def token(auth_client):
    return auth_client.get_token(settings.USERNAME, settings.PASSWORD)
