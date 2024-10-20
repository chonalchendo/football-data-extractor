from pydantic import BaseModel


class ShootingStats(BaseModel):
    rk: str
    player: str
    nation: str
    pos: str
    squad: str
    comp: str
    age: str
    born: str
    ninety_mins_played: str
    goals: str
    shots: str
    shots_on_target: str
    shots_on_target_pct: str
    shots_per_90: str
    shots_on_target_per_90: str
    goals_per_shot: str
    goals_per_shot_on_target: str
    avg_shot_distance: str
    free_kick_shots: str
    penalty_kicks: str
    penalty_kicks_attempted: str
    xg: str
    non_penalty_xg: str
    non_penalty_xg_per_shot: str
    goals_minus_xg: str
    non_penalty_goals_minus_xg: str
