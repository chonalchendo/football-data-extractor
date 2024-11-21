from ..cleaners.common import common_plus_xg_cleaners
from ..cleaners.playing_time import playing_time_rename_cols
from ..schemas import PlayingTimeStats
from .base import BasePlayerCollector, StatsParams
from ..constants import PLAYER_STATS_URL


def playing_time_collector() -> BasePlayerCollector:
    return BasePlayerCollector(
        url=PLAYER_STATS_URL,
        url_params=StatsParams(stat="playingtime", table="playing_time"),
        validator=PlayingTimeStats,
        cleaners=common_plus_xg_cleaners + [playing_time_rename_cols],
    )
