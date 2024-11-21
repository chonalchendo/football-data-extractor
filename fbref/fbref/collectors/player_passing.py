from ..cleaners.common import common_plus_xg_cleaners
from ..cleaners.passing import passing_rename_cols
from ..schemas import PassingStats
from .base import BasePlayerCollector, StatsParams
from ..constants import PLAYER_STATS_URL


def passing_collector() -> BasePlayerCollector:
    return BasePlayerCollector(
        url=PLAYER_STATS_URL,
        url_params=StatsParams(stat="passing", table="passing"),
        validator=PassingStats,
        cleaners=common_plus_xg_cleaners + [passing_rename_cols],
    )
