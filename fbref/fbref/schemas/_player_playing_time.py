from pydantic import BaseModel


class PlayingTimeStats(BaseModel):
    rk: str
    player: str
    nation: str | None
    pos: str | None
    squad: str
    comp: str
    season: str
    age: str | None
    born: str | None
    mp: str
    mins_played: str | None
    mins_per_match: str | None
    mins_played_pct: str | None
    ninety_mins_played: str | None
    starts: str
    mins_per_start: str | None
    complete_matches_played: str
    subs: str
    mins_per_sub: str | None
    unused_sub: str
    points_per_match: str | None
    team_goals_while_on_pitch: str | None
    team_goals_conceded_while_on_pitch: str | None
    goals_minus_conceded_while_on_pitch: str | None
    goals_minus_conceded_while_on_pitch_per_90: str | None
    net_goals_on_minus_off_pitch_per_90: str | None
    team_xg_while_on_pitch: str | None
    team_xg_conceded_while_on_pitch: str | None
    team_xg_minus_xga_while_on_pitch: str | None
    team_xg_minus_xga_while_on_pitch_per_90: str | None
    net_xg_on_minus_off_pitch_per_90: str | None
