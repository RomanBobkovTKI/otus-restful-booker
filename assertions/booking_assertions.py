class BookingAssertions:
    @staticmethod
    def assert_created_booking_matches_payload(response, payload):
        booking = response["booking"]

        assert booking["firstname"] == payload["firstname"]
        assert booking["lastname"] == payload["lastname"]
        assert booking["totalprice"] == payload["totalprice"]
        assert booking["depositpaid"] == payload["depositpaid"]
        assert booking["bookingdates"] == payload["bookingdates"]
        assert booking["additionalneeds"] == payload["additionalneeds"]

    @staticmethod
    def assert_booking_matches_payload(response, payload):
        assert response["firstname"] == payload["firstname"]
        assert response["lastname"] == payload["lastname"]
        assert response["totalprice"] == payload["totalprice"]
        assert response["depositpaid"] == payload["depositpaid"]
        assert response["bookingdates"] == payload["bookingdates"]
        assert response["additionalneeds"] == payload["additionalneeds"]

    @staticmethod
    def assert_booking_firstname_and_lastname_updated(
        response: dict,
        original_payload: dict,
        expected_firstname: str,
        expected_lastname: str,
    ):
        assert response["firstname"] == expected_firstname
        assert response["lastname"] == expected_lastname
        assert response["totalprice"] == original_payload["totalprice"]
        assert response["depositpaid"] == original_payload["depositpaid"]
        assert response["bookingdates"] == original_payload["bookingdates"]
        assert response["additionalneeds"] == original_payload["additionalneeds"]

    @staticmethod
    def assert_booking_firstname_updated(
        response: dict,
        original_payload: dict,
        expected_firstname: str,
    ):
        assert response["firstname"] == expected_firstname
        assert response["lastname"] == original_payload["lastname"]
        assert response["totalprice"] == original_payload["totalprice"]
        assert response["depositpaid"] == original_payload["depositpaid"]
        assert response["bookingdates"] == original_payload["bookingdates"]
        assert response["additionalneeds"] == original_payload["additionalneeds"]

    @staticmethod
    def assert_booking_additionalneeds_updated(
        response: dict,
        expected_additionalneeds: str,
    ):
        assert response["additionalneeds"] == expected_additionalneeds

    @staticmethod
    def assert_booking_firstname_equals(
        response: dict,
        expected_firstname: str,
    ):
        assert response["firstname"] == expected_firstname
