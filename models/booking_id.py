from pydantic import BaseModel, RootModel


class BookingId(BaseModel):
    bookingid: int


class BookingIdList(RootModel[list[BookingId]]):
    pass
