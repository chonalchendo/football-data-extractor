from pydantic import BaseModel


class WageStats(BaseModel):
    rk: int
    player: str
    nation: str | None
    pos: str | None
    squad: str
    age: int
    weekly_wages: str
    annual_wages: str
    season: int
