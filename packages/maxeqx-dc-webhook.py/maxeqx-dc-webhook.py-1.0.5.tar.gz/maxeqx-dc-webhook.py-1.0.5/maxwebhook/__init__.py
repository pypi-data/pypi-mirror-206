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
        data = {
            "content" : self.message,
            "username" : self.username,
            "avatar_url" : self.avatar_url
            }
        datae = {
            "username" : self.username,
            "avatar_url" : self.avatar_url
            }
        datae["embed"] = [{
            "description" : self.embeddescription,
            "title" : self.embedtitle
        }]
        if self.embeddescription or self.embedtitle != None:
            result = requests.post(url, json = datae, headers={"Content-Type": "application/json"})

            result.raise_for_status()
        else:
            result = requests.post(url, json = data, headers={"Content-Type": "application/json"})

            result.raise_for_status()
