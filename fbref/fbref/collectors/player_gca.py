from ..cleaners.common import common_cleaners
from ..cleaners.gca import gca_cleaners
from ..schemas import GcaStats
from .base import BasePlayerCollector, StatsParams
from ..constants import PLAYER_STATS_URL


def gca_collector() -> BasePlayerCollector:
    return BasePlayerCollector(
        url=PLAYER_STATS_URL,
        url_params=StatsParams(stat="gca", table="gca"),
        validator=GcaStats,
        cleaners=common_cleaners + gca_cleaners,
    )
