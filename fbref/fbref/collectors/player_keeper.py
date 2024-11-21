from ..cleaners.common import common_cleaners
from ..cleaners.keepers import rename_keeper_cols
from ..schemas import KeeperStats
from .base import BasePlayerCollector, StatsParams
from ..constants import PLAYER_STATS_URL


def keeper_collector() -> BasePlayerCollector:
    return BasePlayerCollector(
        url=PLAYER_STATS_URL,
        url_params=StatsParams(stat="keeper", table="keeper"),
        validator=KeeperStats,
        cleaners=common_cleaners + [rename_keeper_cols],
    )
