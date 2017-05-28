# Sp-Advertisement
This plugin is a simple advert system for any games in Source-Python. It displays advert with a regular interval define in configuration.

# Configuration

<b>Advert interval</b><br>
<em>Time in seconds between adverts. (Must be an integer)</em><br>
<br>
<b>Advert order</b><br>
<em>Define the appearance order of advert.</em>
<pre>
  0 - Follow order of advert in json file.
  1 - Get random advert.
</pre>

<u>Example :</u>
<pre>{
  "Adverts": [
    {
      "type": "say",
      "message": "Welcome on {hostname} !",
      "translation": "say:1"
    },
    {
      "type": "say",
      "message": "The current map is {currentmap}",
      "translation": "say:2"
    },
    {
      "type": "hint",
      "message": "Kill them all ! [Friendlyfire : {mp_friendlyfire}]",
      "translation": "hint:1"
    },
    {
      "type": "hud",
      "message": "The time is {time}",
      "translation": "hud:1"
    }
  ]
}</pre>
The translation attribute must contains the key of advert translation and must refer to a key in 'advertissement_server.ini'.
If "translation" attribute is defined you are not oblige to write something in "message" key.

<pre>{
  "Adverts": [
    {
      "type": "say",
      "message": "",
      "translation": "say:1"
    }
  ]
}
</pre>

<b>Define template variables :</b><br>
<pre>
  - {currentmap} : Show current map name
  - {date} : Show current date
  - {time} : Show current time
</pre>
<br><br>
<b>Other variables :</b><br>
You can also show all cvar of your server, like mp_friendlyfire, mp_roundtime ...
