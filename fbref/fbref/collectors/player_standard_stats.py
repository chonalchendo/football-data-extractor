from ..cleaners.common import common_cleaners
from ..cleaners.standard import standard_rename_cols
from ..schemas import StandardStats
from .base import BasePlayerCollector, StatsParams
from ..constants import PLAYER_STATS_URL


def standard_stats_collector() -> BasePlayerCollector:
    return BasePlayerCollector(
        url=PLAYER_STATS_URL,
        url_params=StatsParams(stat="stats", table="standard"),
        validator=StandardStats,
        cleaners=common_cleaners + [standard_rename_cols],
    )
