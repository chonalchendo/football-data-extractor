from ..cleaners.common import common_cleaners
from ..cleaners.passing import passing_type_rename_cols
from ..schemas import PassingTypeStats
from .base import BasePlayerCollector

passing_type_collector = BasePlayerCollector(
    stat="passing_types",
    table="passing_types",
    validator=PassingTypeStats,
    cleaners=common_cleaners + [passing_type_rename_cols],
)
