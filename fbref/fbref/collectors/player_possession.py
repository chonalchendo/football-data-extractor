from ..cleaners.common import common_cleaners
from ..cleaners.possession import possession_rename_cols
from ..schemas import PossessionStats
from .base import BasePlayerCollector

possession_collector = BasePlayerCollector(
    stat="possession",
    table="possession",
    validator=PossessionStats,
    cleaners=common_cleaners + [possession_rename_cols],
)
