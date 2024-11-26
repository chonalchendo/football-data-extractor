from pydantic import BaseModel


class KeeperStats(BaseModel):
    rk: str
    player: str
    nation: str
    pos: str
    squad: str
    comp: str
    season: str
    age: str | None
    born: str | None
    mp: str
    starts: str
    min: str | None
    ninety_mins_played: str
    goals_against: str | None
    ga_per_90: str | None
    shots_on_target_against: str | None
    saves: str | None
    save_pct: str | None
    wins: str | None
    draws: str | None
    losses: str
    clean_sheets: str | None
    clean_sheet_pct: str | None
    penalties_faced: str | None
    penalties_allowed: str | None
    penalties_saved: str | None
    penalties_missed: str | None
    penalty_save_pct: str | None
