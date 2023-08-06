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
        if self.message != None and self.embeddescription or self.embedtitle == None:
            data = {
                "content": self.message,
                "username": self.username,
                "avatar_url" : self.avatar_url
            }
            result = requests.post(url, json=data)
            result.raise_for_status()
        
        elif self.message == None and self.embeddescription or self.embedtitle != None:
            embed = {
            "description": self.embeddescription,
            "title": self.embedtitle,
            }
            data = {
            "username" : self.username,
            "avatar_url" : self.avatar_url,
            "embeds": [embed]
            }
            result = requests.post(url, json=data)
            result.raise_for_status()
        elif self.message != None and self.embeddescription or self.embeddescription != None:
            embed = {
            "description": self.embeddescription,
            "title": self.embedtitle,
            }
            data = {
            "content": self.message,
            "username" : self.username,
            "avatar_url" : self.avatar_url,
            "embeds": [embed]
            }
            result = requests.post(url, json=data)