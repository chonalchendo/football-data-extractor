from ..cleaners.common import common_cleaners
from ..cleaners.possession import possession_rename_cols
from ..schemas import PossessionStats
from .base import BasePlayerCollector, StatsParams
from ..constants import PLAYER_STATS_URL


def possession_collector() -> BasePlayerCollector:
    return BasePlayerCollector(
        url=PLAYER_STATS_URL,
        url_params=StatsParams(stat="possession", table="possession"),
        validator=PossessionStats,
        cleaners=common_cleaners + [possession_rename_cols],
    )
