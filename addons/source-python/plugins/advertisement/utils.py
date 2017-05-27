## IMPORTS

import datetime
import json
import os
import random
import re


from itertools import cycle


from cvars import ConVar
from engines.server import global_vars
from paths import PLUGIN_DATA_PATH


from .configs import _configs

## ALL DECLARATION

__all__ = (
    'AdvertisementManager',
    'AdvertParser'
)

class AdvertisementManager(dict):

    def __init__(self):
        super().__init__()
        self._path = PLUGIN_DATA_PATH / 'advertisement/advertisement.json'
        self._load_advertisements()

    @property
    def adverts(self):
        if len(self['Adverts']) == 0:
            return False

        if _configs['advert_order'].get_int() == 1:
            advert_list = self['Adverts']
            random.shuffle(advert_list)
            return cycle(advert_list)
        else:
            return cycle(self['Adverts'])

    @property
    def reload(self):
        self._load_advertisements()

    def _load_advertisements(self):
        self.clear()

        if self._path.find('.json') == -1:
            raise ValueError(
                'Path of location must be an Json file.'
            )

        if not self._path.exists():
            with open(self._path, 'w+') as file:
                default_schema = { "Adverts": [] }
                json.dump(default_schema, file)
        else:
            with open(self._path) as data_json: 
                try:
                    for name, value in json.load(data_json).items():
                        self[name] = value
                except:
                    raise ValueError(
                        'Json file incorrect.'
                        )


class AdvertParser:

    AVAILABLE_VALUE = {
        '{currentmap}' : global_vars.map_name,
        '{date}' : datetime.datetime.now().strftime('%d-%m-%Y'),
        '{time}' : datetime.datetime.now().time().strftime('%H:%M'),
    }

    @classmethod
    def parse(cls, message):
        variable = re.findall('\{[a-z_]+\}', message)
        counter = len(re.findall('\{[a-z_]+\}', message))
        if counter != 0:
            for i in range(0, counter):
                if variable[i] in AdvertParser.AVAILABLE_VALUE:
                    parsed_message = message.replace(
                        variable[i], 
                        str(AdvertParser.AVAILABLE_VALUE[variable[i]])
                    )
                else:
                    cvar = variable[i].replace('{', '')
                    cvar = cvar.replace('}', '')
                    cvar_value = ConVar(cvar).get_string()
                    parsed_message = message.replace(variable[i], cvar_value)
        else:
            parsed_message = message
        return parsed_message