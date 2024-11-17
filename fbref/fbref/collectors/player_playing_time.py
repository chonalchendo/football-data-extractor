from ..cleaners.common import common_plus_xg_cleaners
from ..cleaners.playing_time import playing_time_rename_cols
from ..schemas import PlayingTimeStats
from .base import BasePlayerCollector


def playing_time_collector() -> BasePlayerCollector:
    return BasePlayerCollector(
        stat="playingtime",
        table="playing_time",
        validator=PlayingTimeStats,
        cleaners=common_plus_xg_cleaners + [playing_time_rename_cols],
    )
