## IMPORTS

from events import Event
from filters.players import PlayerIter
from listeners import OnLevelInit
from listeners.tick import Repeat
from messages import SayText2, HintText, HudMsg
from paths import PLUGIN_DATA_PATH
from translations.strings import LangStrings


from .info import info
from .configs import _configs


__all__ = (
	'NOT_FOUND',
	'ADVERT_TRANSLATION',
)

## GLOBALS

strings = LangStrings('advertisement')

NOT_FOUND = strings['Not Found']

ADVERT_TRANSLATION = strings