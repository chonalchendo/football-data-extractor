from ..cleaners.common import common_cleaners
from ..cleaners.keepers import rename_keeper_cols
from ..schemas import KeeperStats
from .base import BasePlayerCollector

keeper_collector = BasePlayerCollector(
    stat="keeper",
    table="keeper",
    validator=KeeperStats,
    cleaners=common_cleaners + [rename_keeper_cols],
)
