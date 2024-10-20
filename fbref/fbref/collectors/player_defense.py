from ..cleaners.common import common_cleaners
from ..cleaners.defense import defense_cleaners
from ..schemas import DefenseStats
from .base import BasePlayerCollector


PlayerDefense = BasePlayerCollector(
    stat='defense',
    table='defense',
    validator=DefenseStats,
    cleaners=common_cleaners + defense_cleaners
)

