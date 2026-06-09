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
