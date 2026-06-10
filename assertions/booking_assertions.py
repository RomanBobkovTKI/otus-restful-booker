class BookingAssertions:
    # @staticmethod
    # def assert_booking_matches_payload(response, payload):
    #     assert response["booking"]["firstname"] == payload["firstname"]
    #     assert response["booking"]["lastname"] == payload["lastname"]
    #     assert response["booking"]["totalprice"] == payload["totalprice"]
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
