from pydantic import BaseModel


class Player(BaseModel):
    name: str
    dob: str
    age: int
    country: str
    current_club: str | None
    height: str
    position: str
    value: str
    joined_date: str | None
    number: str
    signed_from: str | None
    signing_fee: str
    tm_id: str
    tm_name: str
    tm_squad: str
    foot: str
    season: int
    squad: str