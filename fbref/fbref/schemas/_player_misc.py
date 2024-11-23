from pydantic import BaseModel


class MiscStats(BaseModel):
    rk: str
    player: str
    nation: str | None
    pos: str
    squad: str
    comp: str
    season: str
    age: str | None 
    born: str | None
    ninety_mins_played: str
    yellow_cards: str
    red_cards: str
    second_yellow_cards: str
    fouls: str
    fouls_drawn: str
    offsides: str
    crosses: str
    interceptions: str
    tackles_won: str
    penalties_won: str
    penalties_conceded: str
    own_goals: str
    ball_recoveries: str
    aerials_won: str
    aerials_lost: str
    aerials_won_pct: str | None
