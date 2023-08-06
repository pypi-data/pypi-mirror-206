import requests

class Webhook():
    def __init__(self):
        self.url : str = None
        self.username : str = None
        self.avatar_url : str = None
        self.message : str = None
        self.embedtitle : str = None
        self.embeddescription : str = None
    def send(self):     
        url = self.url
        embed = {
        "description": self.embeddescription,
        "title": self.embedtitle
        }
        data = {
            "content" : self.message,
            "username" : self.username,
            "avatar_url" : self.avatar_url,
            "embeds": [embed]
            }

        headers = {
        "Content-Type": "application/json"
        }

        result = requests.post(url, json=data, headers=headers)
        result.raise_for_status()