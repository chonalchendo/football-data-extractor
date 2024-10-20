from pydantic import BaseModel


class KeeperStats(BaseModel):
    rk: str
    player: str
    nation: str
    pos: str
    squad: str
    comp: str
    age: str
    born: str
    mp: str
    starts: str
    min: str
    ninety_mins_played: str
    goals_against: str
    ga_per_90: str
    shots_on_target_against: str
    saves: str
    save_pct: str
    wins: str
    draws: str
    losses: str
    clean_sheets: str
    clean_sheet_pct: str
    penalties_faced: str
    penalties_allowed: str
    penalties_saved: str
    penalties_missed: str
    penalty_save_pct: str
