from pydantic import BaseModel


class GcaStats(BaseModel):
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
    shot_creating_actions: str
    sca_per_90: str
    pass_live_sca: str
    pass_dead_sca: str
    take_on_sca: str
    shot_sca: str
    foul_drawn_sca: str
    defensive_action_sca: str
    goal_creating_actions: str
    gca_per_90: str
    pass_live_gca: str
    pass_dead_gca: str
    take_on_gca: str
    shot_gca: str
    foul_drawn_gca: str
    defensive_action_gca: str
