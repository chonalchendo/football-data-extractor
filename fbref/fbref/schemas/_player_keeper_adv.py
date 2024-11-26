from pydantic import BaseModel


class KeeperAdvStats(BaseModel):
    rk: str
    player: str
    nation: str
    pos: str
    squad: str
    comp: str
    season: str
    age: str | None 
    born: str | None
    ninety_mins_played: str
    ga: str | None
    penalties_allowed: str | None
    free_kick_goals_allowed: str | None
    corner_goals_allowed: str | None
    own_goals: str | None
    post_shot_xg: str
    post_shot_xg_on_target: str | None
    post_shot_xg_minus_ga: str | None
    post_shot_xg_minus_ga_per_90: str | None
    passes_completed_plus_40_yards: str | None
    passes_attempted_plus_40_yards: str
    passes_pct_plus_40_yards: str | None
    total_passes_attempted: str
    throws_attempted: str | None
    launch_pct: str | None
    avg_pass_length: str | None
    goal_kicks_attempted: str
    goal_kick_launch_pct: str | None
    avg_goal_kick_length: str | None
    crosses_faced: str
    crosses_stopped: str | None
    crosses_stopped_pct: str | None
    defensive_actions_outside_penalty_area: str | None
    defensive_opa_per_90: str | None
    avg_defensive_action_distance: str | None
