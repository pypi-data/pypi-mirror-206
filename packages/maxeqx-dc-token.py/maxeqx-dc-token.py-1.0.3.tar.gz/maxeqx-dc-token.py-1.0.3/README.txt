maxeqx-dc-webhook.py
=================


This is simple webhook sender in discord.


Installing

Python 3.8 or higher is required

    # Linux/macOS
    pip3 install -U maxeqx-dc-webhook.py

    # Windows
    pip install -U maxeqx-dc-webhook.py

Example usage

from maxtoken import *

#setting tokens
#u must create tokens.txt file!

#setting proxies
#u must create proxies.txt file!

#setting object
maxtoken = DiscordToken()

#execute invite_join
maxtoken.invite_join(invite_code='code')