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

from maxwebhook import *

#creating webhook object
webhook = Webhook()

#setting webhook url
webhook.url = "webhookurl"

#setting username
webhook.username = 'username'

#setting avatar url
webhook.avatar_url = 'avatarurl'

#setting message
webhook.message = 'message'

#sending message
await webhook.send()
