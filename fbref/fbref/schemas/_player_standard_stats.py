from pydantic import BaseModel


class StandardStats(BaseModel):
    rk: str
    player: str
    nation: str | None
    pos: str
    squad: str
    comp: str
    season: str
    age: str
    born: str
    mp: str
    starts: str
    min: str
    ninety_mins_played: str
    goals: str
    assists: str
    goals_assists: str
    non_penalty_goals: str
    penalty_kicks: str
    penalty_kicks_attempted: str
    yellow_cards: str
    red_cards: str
    xg: str
    non_penalty_xg: str
    xag: str
    non_pen_xg_plus_xag: str
    progressive_carries: str
    progressive_passes: str
    progressive_passes_received: str
    goals_per_90: str
    assists_per_90: str
    goals_assists_per_90: str
    non_penalty_goals_per_90: str
    non_penalty_goals_assists_per_90: str
    xg_per_90: str
    xag_per_90: str
    xg_plus_xag_per_90: str
    non_penalty_xg_per_90: str
    non_penalty_xg_plus_xag_per_90: str
