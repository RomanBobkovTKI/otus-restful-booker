import pytest

from models.booking import BookingResponse


@pytest.mark.get_booking_by_id
@pytest.mark.parametrize("booking_id", [5, 2, 3])
def test_get_booking_by_id(booking_client, booking_id):
    response = booking_client.get_booking(booking_id)
    BookingResponse.model_validate(response)


@pytest.mark.get_booking_by_id
def test_get_booking_not_found(booking_client):
    with pytest.raises(Exception) as exc:
        booking_client.get_booking(999999999)

    assert "404: Not Found" in str(exc.value)
