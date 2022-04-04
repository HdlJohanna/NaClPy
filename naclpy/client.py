import requests
from .crypto import make_key, encrypt

class METHOD:
    GET = "GET"
    POST = "POST"
    PATCH = "PUT"
    PATCH = "PATCH"

class Client:
    def __init__(self,secret_key:bytes,hash_key:bytes or None = None,host="127.0.0.1",port=2839):
        self.secret_key = secret_key
        self.host = host
        self.port = port
        self.hash_key = make_key() if not hash_key else hash_key

    def request(self,endpoint:str="test",method:str=METHOD.GET):
        resource = requests.request(method,f'http://{self.host}:{self.port}/{endpoint}',headers={
            "SECRET_KEY":encrypt(self.secret_key,self.hash_key)
        })
        return resource
