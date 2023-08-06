import requests

class Webhook():
    def __init__(self):
        self.url : str = None
        self.username : str = None
        self.avatar_url : str = None
        self.message : str = None
    def send(self):     
        url = self.url
        data = {
            "content" : self.message,
            "username" : self.username,
            "avatar_url" : self.avatar_url
            }

        result = requests.post(url, json = data)

        result.raise_for_status()
