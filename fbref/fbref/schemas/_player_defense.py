from pydantic import BaseModel


class DefenseStats(BaseModel):
    rk: str
    player: str
    nation: str | None
    squad: str
    comp: str
    season: str
    age: str | None
    born: str | None
    pos: str
    ninety_mins_played: str
    tackles: str
    tackles_won: str
    def_third_tackles: str
    mid_third_tackles: str
    att_third_tackles: str
    dribblers_tackled: str
    dribblers_challenged: str
    tackle_pct: str | None
    challenges_lost: str
    blocks: str
    shots_blocked: str
    passes_blocked: str
    interceptions: str
    tackles_interceptions: str
    clearances: str
    errors: str
