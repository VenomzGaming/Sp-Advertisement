## IMPORTS

import json
import os


from cvars import ConVar
from engines.server import global_vars
from paths import PLUGIN_DATA_PATH

from .advert import Advert, adverts_list
from .configs import _configs

## ALL DECLARATION

__all__ = (
    'AdvertManager',
    'advert_manager',
)


## CLASS

class AdvertManager:

    def __init__(self):
        self._path = PLUGIN_DATA_PATH / 'advertisement/advertisement.json'
        self._load_advertisements()

    @property
    def reload(self):
        self._load_advertisements()

    def _load_advertisements(self):
        adverts_list.clear()

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
                    advert = dict()
                    for name, value in json.load(data_json).items():
                        advert[name] = value

                    # Create all Advert objects
                    for adv in advert['Adverts']:
                        Advert(adv)
                except:
                    raise ValueError(
                        'Json file incorrect.'
                        )

advert_manager = AdvertManager()