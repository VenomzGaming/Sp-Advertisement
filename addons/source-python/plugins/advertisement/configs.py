## IMPORTS

from config.manager import ConfigManager


from .info import info

## ALL DECLARATION

__all__ = (
    '_configs',
)

## GLOBALS

_configs = dict()

with ConfigManager(info.name) as _config:

    _config.section('Advert Config')

    _configs['advert_interval'] = _config.cvar(
        'advert_interval', 3,
        'Time in minutes between adverts.')

    _configs['advert_order'] = _config.cvar(
        'advert_order', 0,
        '0 - Follow order of advert in json file. | 1 - Get random advert')

