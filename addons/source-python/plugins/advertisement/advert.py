## IMPORTS

import datetime
import random
import re
from collections import Counter
from itertools import cycle

from cvars import ConVar
from engines.server import global_vars
from messages import SayText2, HintText, HudMsg

from .configs import _configs
from .strings import ADVERT_TRANSLATION

## ALL DECLARATION

__all__ = (
    'Advert',
    'adverts_list',
)

## GLOBAL

ADVERT_TYPE = {
    'say' : SayText2,
    'hint' : HintText,
    'hud' : HudMsg,
}

## CLASS


class Adverts(list):
    'This class is used to store all <Advert>'

    def count_all(self):
        return Counter(self)

    @property
    def find_all(self):
        if self.count_all() == 0:
            return False

        if _configs['advert_order'].get_int() == 1:
            random.shuffle(self)
            return cycle(self)
        else:
            return cycle(self)

adverts_list = Adverts()


class AdvertType(Enum):
    SAY = partial(SayText2)
    HINT = partial(HintText)
    HUD = partial(HudMsg)


class Advert(object):

    AVAILABLE_VALUE = {
        '{currentmap}' : global_vars.map_name,
        '{date}' : datetime.datetime.now().strftime('%d-%m-%Y'),
        '{time}' : datetime.datetime.now().time().strftime('%H:%M'),
    }


    def __init__(self, advert):
        self.type = advert['type']
        self.message = advert['message']
        self.translation = advert['translation']
        self.params = self._get_params()


    def __new__(cls, *args, **kwargs):
        'Store all the new instances inside the <Adverts>.'
        instance = object.__new__(cls)
        adverts_list.append(instance)
        return instance
        

    def _get_params(self):
        if not self.translation:
            variables = re.findall('\{[a-z_]+\}', self.message)
        else:
            translate_messages = ADVERT_TRANSLATION[self.translation]
            variables = re.findall('\{[a-z_]+\}', translate_messages[next(iter(translate_messages))])

        params = {}
        for var in variables:
            key = var.replace('{', '').replace('}', '')
            if var in self.AVAILABLE_VALUE:
                params[key] = str(self.AVAILABLE_VALUE[var])
            else:
                cvar_value = ConVar(key).get_string()
                params[key] = cvar_value
        return params


    def _format(self):
        return self.message.format(**self.params)


    def _get_string(self):
        if self.translation not in ADVERT_TRANSLATION:
            return self._format()

        translate_message = ADVERT_TRANSLATION[self.translation]
        return translate_message


    def send(self, players):
        formated_message = self._format() if not self.translation else self._get_string()

        if self.type.lower() not in ADVERT_TYPE:
           message = ADVERT_TYPE['say'](formated_message)
        else:
            if self.type.lower() == 'hud':
                message = ADVERT_TYPE['hud'](
                    message=formated_message,
                    hold_time=1,
                    x=-1,
                    y=-0.7,
                )
            else:
               message = ADVERT_TYPE[self.type.lower()](formated_message)

            message.send(players, **self.params)
