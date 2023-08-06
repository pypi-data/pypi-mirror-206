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
        if self.embedtitle or self.embeddescription != None:
            data["embed"] = [{
                "description" : self.embeddescription,
                "title" : self.embedtitle
            }]
            result = requests.post(url, json = data)
        else:
            result = requests.post(url, json = data)

        result.raise_for_status()
