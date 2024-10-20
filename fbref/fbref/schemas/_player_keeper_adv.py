from pydantic import BaseModel


class KeeperAdvStats(BaseModel):
    rk: str
    player: str
    nation: str
    pos: str
    squad: str
    comp: str
    age: str
    born: str
    ninety_mins_played: str
    ga: str
    penalties_allowed: str
    free_kick_goals_allowed: str
    corner_goals_allowed: str
    own_goals: str
    post_shot_xg: str
    post_shot_xg_on_target: str
    post_shot_xg_minus_ga: str
    post_shot_xg_minus_ga_per_90: str
    passes_completed_plus_40_yards: str
    passes_attempted_plus_40_yards: str
    passes_pct_plus_40_yards: str
    total_passes_attempted: str
    throws_attempted: str
    launch_pct: str
    avg_pass_length: str
    goal_kicks_attempted: str
    goal_kick_launch_pct: str
    avg_goal_kick_length: str
    crosses_faced: str
    crosses_stopped: str
    crosses_stopped_pct: str
    defensive_actions_outside_penalty_area: str
    defensive_opa_per_90: str
    avg_defensive_action_distance: str
