from pydantic import BaseModel


class PassingStats(BaseModel):
    rk: str
    player: str
    nation: str | None
    pos: str
    squad: str
    comp: str
    season: str
    age: str
    born: str
    ninety_mins_played: str
    passes_completed: str
    passes_attempted: str
    pass_completion_pct: str | None
    total_pass_distance: str
    progressive_pass_distance: str
    short_passes_completed: str
    short_passes_attempted: str
    short_pass_completion_pct: str | None
    medium_passes_completed: str
    medium_passes_attempted: str
    medium_pass_completion_pct: str | None
    long_passes_completed: str
    long_passes_attempted: str
    long_pass_completion_pct: str | None
    assists: str
    xag: str
    xa: str
    assists_minus_xag: str
    key_passes: str
    passes_into_final_third: str
    passes_into_penalty_area: str
    crosses_into_penalty_area: str
    progressive_passes: str
