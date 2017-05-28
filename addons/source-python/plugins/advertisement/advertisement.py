## IMPORTS

from events import Event
from filters.players import PlayerIter
from listeners import OnLevelInit
from listeners.tick import Repeat
from messages import SayText2
from paths import PLUGIN_DATA_PATH
from translations.strings import LangStrings


from .info import info
from .configs import _configs
from .advert import adverts_list
from .advert_manager import advert_manager
from .strings import NOT_FOUND


## GLOBALS

ADVERTS = adverts_list.find_all

TIME_BETWEEN_ADVERTS = _configs['advert_interval'].get_int()


_human_players = PlayerIter('human')

## GAME EVENT

@OnLevelInit
def _on_level_init(map_name):
    advert_manager.reload


@Repeat
def _send_advert():
    if not ADVERTS:
        SayText2(NOT_FOUND).send()
    else:
        advert = next(ADVERTS)
        advert.send(_human_players)

_send_advert.start(TIME_BETWEEN_ADVERTS)
