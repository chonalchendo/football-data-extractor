from pydantic import BaseModel


class WageStats(BaseModel):
    rk: int
    player: str
    nation: str | None
    pos: str | None
    squad: str
    age: int
    weekly_wages_euros: str
    annual_wages_euros: str
    season: str
