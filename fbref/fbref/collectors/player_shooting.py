from ..cleaners.common import common_cleaners
from ..cleaners.shooting import shooting_rename_cols
from ..schemas import ShootingStats
from .base import BasePlayerCollector, StatsParams
from ..constants import PLAYER_STATS_URL


def shooting_collector() -> BasePlayerCollector:
    return BasePlayerCollector(
        url=PLAYER_STATS_URL,
        url_params=StatsParams(stat="shooting", table="shooting"),
        validator=ShootingStats,
        cleaners=common_cleaners + [shooting_rename_cols],
    )
