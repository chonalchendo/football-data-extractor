from ..cleaners.common import common_cleaners
from ..cleaners.shooting import shooting_rename_cols
from ..schemas import ShootingStats
from .base import BasePlayerCollector

shooting_collector = BasePlayerCollector(
    stat="shooting",
    table="shooting",
    validator=ShootingStats,
    cleaners=common_cleaners + [shooting_rename_cols],
)
