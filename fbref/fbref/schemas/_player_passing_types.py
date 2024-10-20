from pydantic import BaseModel


class PassingTypeStats(BaseModel):
    rk: str
    player: str
    nation: str
    pos: str
    squad: str
    comp: str
    age: str
    born: str
    ninety_mins_played: str
    passes_attempted: str
    live_ball_passes: str
    dead_ball_passes: str
    free_kick_passes: str
    through_balls: str
    switches: str
    crosses: str
    throw_ins: str
    corner_kicks: str
    inswinging_corners: str
    outswinging_corners: str
    straight_corners: str
    passes_completed: str
    passes_offside: str
    passes_blocked: str
    match: strs
