from pydantic import BaseModel


class PlayingTimeStats(BaseModel):
    rk: str
    player: str
    nation: str
    pos: str
    squad: str
    comp: str
    age: str
    born: str
    mp: str
    mins_played: str
    mins_per_match: str
    mins_played_pct: str
    ninety_mins_played: str
    starts: str
    mins_per_start: str
    complete_matches_played: str
    subs: str
    mins_per_sub: str
    unused_sub: str
    points_per_match: str
    team_goals_while_on_pitch: str
    team_goals_conceded_while_on_pitch: str
    goals_minus_conceded_while_on_pitch: str
    goals_minus_conceded_while_on_pitch_per_90: str
    net_goals_on_minus_off_pitch_per_90: str
    team_xg_while_on_pitch: str
    team_xg_conceded_while_on_pitch: str
    team_xg_minus_xga_while_on_pitch: str
    team_xg_minus_xga_while_on_pitch_per_90: str
    net_xg_on_minus_off_pitch_per_90: str
