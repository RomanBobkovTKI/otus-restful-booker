import allure
import pytest

from models.booking import BookingResponse


@allure.feature("GET booking")
@allure.story("Get booking by id")
class TestGetBookingById:
    @allure.title("Get booking by existing id")
    @pytest.mark.get_booking_by_id
    @pytest.mark.parametrize("booking_id", [5])
    @pytest.mark.skip #Тест не стабильный
    def test_get_booking_by_id(self, booking_client, booking_id):
        with allure.step(f"Get booking with id={booking_id}"):
            response = booking_client.get_booking(booking_id)

        with allure.step("Validate booking response schema"):
            BookingResponse.model_validate(response)

    @allure.title("Get booking by non-existing id")
    @pytest.mark.get_booking_by_id
    @pytest.mark.negative
    def test_get_booking_not_found(self, booking_client):
        with allure.step("Get booking with non-existing id"):
            with pytest.raises(Exception) as exc:
                booking_client.get_booking(999999999)

        with allure.step("Validate booking not found response"):
            assert "404: Not Found" in str(exc.value)
