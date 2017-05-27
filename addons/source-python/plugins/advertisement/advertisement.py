## IMPORTS

from events import Event
from listeners import OnLevelInit
from listeners.tick import Repeat
from messages import SayText2, HintText, HudMsg
from paths import PLUGIN_DATA_PATH
from translations.strings import LangStrings


from .info import info
from .configs import _configs
from .utils import AdvertisementManager, AdvertParser


## GLOBALS

messages = LangStrings('advertisement')

ADVERT_TYPE = {
    'say' : SayText2,
    'hint' : HintText,
    'hud' : HudMsg,
}

MINUTES_BETWEEN_ADVERTS = _configs['advert_interval'].get_int()

# Load all adverts
advert_manager = AdvertisementManager()
ADVERTS = advert_manager.adverts


## GAME EVENT

@OnLevelInit
def _on_level_init(map_name):
    advert_manager.reload


@Repeat
def _send_advert():
    if not ADVERTS:
        SayText2(messages['Not Found']).send()
    else:
        advert = next(ADVERTS)
        parsed_message = AdvertParser.parse(advert['message'])
        if advert['type'] not in ADVERT_TYPE:
            ADVERT_TYPE['say'](parsed_message).send()
        else:
            if advert['type'] == 'hud':
                ADVERT_TYPE[advert['type']](
                    message=parsed_message,
                    hold_time=1,
                    x=-1,
                    y=-0.7,
                ).send()
            else:
                ADVERT_TYPE[advert['type']](parsed_message).send()

_send_advert.start(MINUTES_BETWEEN_ADVERTS * 60)
