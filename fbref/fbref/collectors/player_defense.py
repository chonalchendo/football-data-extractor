from ..cleaners.common import common_cleaners
from ..cleaners.defense import defense_cleaners
from ..schemas import DefenseStats
from .base import BasePlayerCollector, StatsParams
from ..constants import PLAYER_STATS_URL


def defense_collector() -> BasePlayerCollector:
    return BasePlayerCollector(
        url=PLAYER_STATS_URL,
        url_params=StatsParams(stat="defense", table="defense"),
        validator=DefenseStats,
        cleaners=common_cleaners + defense_cleaners,
    )
