from ..cleaners.common import common_cleaners
from ..cleaners.passing import passing_type_rename_cols
from ..schemas import PassingTypeStats
from .base import BasePlayerCollector, StatsParams
from ..constants import PLAYER_STATS_URL


def passing_type_collector() -> BasePlayerCollector:
    return BasePlayerCollector(
        url=PLAYER_STATS_URL,
        url_params=StatsParams(stat="passing_types", table="passing_types"),
        validator=PassingTypeStats,
        cleaners=common_cleaners + [passing_type_rename_cols],
    )