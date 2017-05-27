# Sp-Advertisement
This plugin is a simple advert system for any games in Source-Python. It displays advert with a regular interval define in configuration.

# Configuration

<b>Advert interval</b><br>
<em>Time in minutes between adverts. (Must be an integer)</em><br>
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
      "message": "Welcome on our server !"
    },
    {
      "type": "say",
      "message": "The current map is {currentmap}"
    },
    {
      "type": "hint",
      "message": "Kill them all ! [Friendlyfire : {mp_friendlyfire}]"
    },
    {
      "type": "hud",
      "message": "The time is {time}"
    }
  ]
}</pre>

<b>Define template variable :</b><br>
<pre>
  - {currentmap} : Show current map name
  - {date} : Show current date
  - {time} : Show current time
</pre>
<br><br>
<b>Other variable :</b><br>
You can also show all cvar of your server, like mp_friendlyfire, mp_roundtimer ...
