from pydantic import BaseModel


class PossessionStats(BaseModel):
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
    touches: str
    def_pen_area_touches: str
    def_third_touches: str
    mid_third_touches: str
    att_third_touches: str
    att_pen_area_touches: str
    live_ball_touches: str
    take_ons_attempted: str
    take_ons_successful: str
    take_on_succ_pct: str | None
    take_ons_tackled: str
    take_on_tackled_pct: str | None
    carries: str
    total_distance_carried: str
    progressive_carries_distance: str
    progressive_carries: str
    carries_into_final_third: str
    carries_into_penalty_area: str
    miscontrols: str
    dispossessed: str
    passes_received: str
    progressive_passes_received: str
