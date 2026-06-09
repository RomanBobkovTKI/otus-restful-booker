import pytest

from models.booking_id import BookingIdList


@pytest.mark.get_booking_id
def test_get_bookings(booking_client):
    response = booking_client.get_booking_ids()
    BookingIdList.model_validate(response)


@pytest.mark.get_booking_id
@pytest.mark.parametrize("firstname", ["Eric", "Susan", "Sally"])
def test_get_bookings_by_firstname(booking_client, firstname):
    response = booking_client.get_booking_ids(params={"firstname": firstname})
    BookingIdList.model_validate(response)


@pytest.mark.get_booking_id
@pytest.mark.parametrize("lastname", ["Smith", "Jackson", "Jones"])
def test_get_bookings_by_lastname(booking_client, lastname):
    response = booking_client.get_booking_ids(params={"lastname": lastname})
    BookingIdList.model_validate(response)


@pytest.mark.get_booking_id
def test_get_booking_by_firstname_and_lastname(booking_client):
    response = booking_client.get_booking_ids(
        params={"firstname": "Eric", "lastname": "Jackson"}
    )
    BookingIdList.model_validate(response)


@pytest.mark.get_booking_id
def test_search_returns_empty_list_when_no_matches(booking_client):
    response = booking_client.get_booking_ids(
        params={"firstname": "ThisNameDoesNotExist123"}
    )

    validated = BookingIdList.model_validate(response)

    assert validated.root == []


@pytest.mark.get_booking_id
@pytest.mark.parametrize("checkin", ["2019-12-17", "2015-02-02", "2025-01-20"])
def test_get_bookings_by_checkin(booking_client, checkin):
    response = booking_client.get_booking_ids(params={"checkin": checkin})
    BookingIdList.model_validate(response)


@pytest.mark.get_booking_id
@pytest.mark.parametrize("checkout", ["2025-03-19", "2021-11-14", "2024-03-02"])
def test_get_bookings_by_checkout(booking_client, checkout):
    response = booking_client.get_booking_ids(params={"checkout": checkout})
    BookingIdList.model_validate(response)
