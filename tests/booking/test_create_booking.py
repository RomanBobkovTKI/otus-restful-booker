import allure
import pytest

from assertions.booking_assertions import BookingAssertions
from models.booking import CreateBookingResponse, BookingResponse
from utils.data_factory import generate_booking_payload


@allure.feature("CREATE booking")
@allure.story("Create booking")
class TestCreateBooking:
    @allure.title("Create booking")
    @pytest.mark.create_booking
    def test_create_booking(self, booking_client):
        with allure.step("Generate booking payload"):
            payload = generate_booking_payload()

        with allure.step("Create booking"):
            response = booking_client.create_booking(payload)

        with allure.step("Validate create booking response schema"):
            CreateBookingResponse.model_validate(response)

        with allure.step("Check created booking matches payload"):
            BookingAssertions.assert_created_booking_matches_payload(
                response,
                payload,
            )

    @allure.title("Created booking can be retrieved by id")
    @pytest.mark.create_booking
    def test_created_booking_can_be_retrieved_by_id(self, booking_client):
        with allure.step("Generate booking payload"):
            payload = generate_booking_payload()

        with allure.step("Create booking"):
            created = booking_client.create_booking(payload)

        with allure.step("Validate create booking response schema"):
            created_model = CreateBookingResponse.model_validate(created)

        with allure.step("Get created booking by id"):
            response = booking_client.get_booking(created_model.bookingid)

        with allure.step("Validate booking response schema"):
            BookingResponse.model_validate(response)

        with allure.step("Check retrieved booking matches payload"):
            BookingAssertions.assert_booking_matches_payload(
                response,
                payload,
            )

    @allure.title("Create booking with empty payload")
    @pytest.mark.create_booking
    @pytest.mark.negative
    def test_create_booking_with_empty_payload(self, booking_client):
        with allure.step("Create booking with empty payload"):
            with pytest.raises(Exception) as exc:
                booking_client.create_booking({})

        with allure.step("Check error status code"):
            assert "500" in str(exc.value) or "400" in str(exc.value)
