from typing import Callable, TypeVar
from .base import BasePlayerCollector
from .player_defense import defense_collector
from .player_gca import gca_collector
from .player_keeper import keeper_collector
from .player_keeper_adv import keeper_adv_collector
from .player_misc import misc_collector
from .player_passing import passing_collector
from .player_passing_type import passing_type_collector
from .player_playing_time import playing_time_collector
from .player_possession import possession_collector
from .player_shooting import shooting_collector
from .player_standard_stats import standard_stats_collector
from .player_wages import wage_collector


COLLECTOR_FUNCTION = TypeVar(
    "COLLECTION_FUNCTION", bound=Callable[..., BasePlayerCollector]
)
COLLECTORS: dict[str, COLLECTOR_FUNCTION] = {}
DECORATOR = Callable[[COLLECTOR_FUNCTION], COLLECTOR_FUNCTION]


def collector(collector: str) -> DECORATOR:
    def decorator(func: COLLECTOR_FUNCTION) -> COLLECTOR_FUNCTION:
        COLLECTORS[collector] = func
        return func

    return decorator


def get_collector(collector: str) -> COLLECTOR_FUNCTION:
    return COLLECTORS.get(collector)


@collector(collector="player_defense")
def defense():
    return defense_collector()


@collector(collector="player_gca")
def gca():
    return gca_collector()


@collector(collector="player_keeper")
def keeper():
    return keeper_collector()


@collector(collector="player_keeper_adv")
def keeper_adv():
    return keeper_adv_collector()


@collector(collector="player_misc")
def misc():
    return misc_collector()


@collector(collector="player_passing")
def passing():
    return passing_collector()


@collector(collector="player_passing_type")
def passing_type():
    return passing_type_collector()


@collector(collector="player_playing_time")
def playing_time():
    return playing_time_collector()


@collector(collector="player_possession")
def possession():
    return possession_collector()


@collector(collector="player_shooting")
def shooting():
    return shooting_collector()


@collector(collector="player_standard_stats")
def standard_stats():
    return standard_stats_collector()


@collector(collector='player_wages')
def wages(comp_id: int, comp_name: str):
    return wage_collector(comp_id=comp_id, comp_name=comp_name)