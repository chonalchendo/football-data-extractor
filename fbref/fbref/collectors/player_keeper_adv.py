from ..cleaners.common import common_plus_xg_cleaners
from ..cleaners.keepers import rename_keeper_adv_cols
from ..schemas import KeeperAdvStats
from .base import BasePlayerCollector, StatsParams
from ..constants import PLAYER_STATS_URL


def keeper_adv_collector() -> BasePlayerCollector:
    return BasePlayerCollector(
        url=PLAYER_STATS_URL,
        url_params=StatsParams(stat="keepersadv", table="keeper_adv"),
        validator=KeeperAdvStats,
        cleaners=common_plus_xg_cleaners + [rename_keeper_adv_cols],
    )
