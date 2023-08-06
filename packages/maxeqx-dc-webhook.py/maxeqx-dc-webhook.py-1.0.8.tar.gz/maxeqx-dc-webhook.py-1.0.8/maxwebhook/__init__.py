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

        headers = {
        "Content-Type": "application/json"
        }

        if self.embeddescription or self.embedtitle != None:
            embed = {
            "description": self.embeddescription,
            "title": self.embedtitle
            }
            data = {
            "username" : self.username,
            "avatar_url" : self.avatar_url,
            "embeds": [embed]
            }
            result = requests.post(url, json=data, headers=headers)
            result.raise_for_status()
        elif self.embeddescription and self.embedtitle and self.message != None:
            embed = {
            "description": self.embeddescription,
            "title": self.embedtitle,
            "content": self.message
            }
            data = {
            "username" : self.username,
            "avatar_url" : self.avatar_url,
            "embeds": [embed]
            }
            result = requests.post(url, json=data, headers=headers)
            result.raise_for_status()
        else:
            if self.message != None:
                data = {
                    "username" : self.username,
                    "avatar_url" : self.avatar_url,
                    "content" : self.message
                }
                result = requests.post(url, json=data, headers=headers)
                result.raise_for_status