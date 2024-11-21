from ..cleaners.common import common_cleaners
from ..cleaners.misc import misc_rename_cols
from ..schemas import MiscStats
from .base import BasePlayerCollector, StatsParams
from ..constants import PLAYER_STATS_URL


def misc_collector() -> BasePlayerCollector:
    return BasePlayerCollector(
        url=PLAYER_STATS_URL,
        url_params=StatsParams(stat="misc", table="misc"),
        validator=MiscStats,
        cleaners=common_cleaners + [misc_rename_cols],
    )
