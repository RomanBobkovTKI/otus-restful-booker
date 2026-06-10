import pytest

from models.booking import CreateBookingResponse
from utils.data_factory import generate_booking_payload


@pytest.mark.delete_booking
def test_delete_booking(booking_client, token):
    payload = generate_booking_payload()

    created = booking_client.create_booking(payload)
    created_model = CreateBookingResponse.model_validate(created)

    response = booking_client.delete_booking(
        booking_id=created_model.bookingid,
        token=token,
    )

    assert response == "Created"
