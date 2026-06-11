import allure
import pytest

from assertions.booking_assertions import BookingAssertions
from models.booking import CreateBookingResponse
from utils.data_factory import generate_booking_payload


@allure.feature("DELETE booking")
@allure.story("Delete booking")
class TestDeleteBooking:
    @allure.title("Delete booking")
    @pytest.mark.delete_booking
    def test_delete_booking(self, booking_client, token):
        with allure.step("Generate booking payload"):
            payload = generate_booking_payload()

        with allure.step("Create booking"):
            created = booking_client.create_booking(payload)

        with allure.step("Validate create booking response schema"):
            created_model = CreateBookingResponse.model_validate(created)

        with allure.step("Delete booking"):
            response = booking_client.delete_booking(
                booking_id=created_model.bookingid,
                token=token,
            )

        with allure.step("Validate delete booking response"):
            assert response == "Created"
