from pydantic import BaseModel


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class BookingResponse(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str
