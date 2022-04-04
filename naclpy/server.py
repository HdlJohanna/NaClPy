import json
from flask import Flask, request, redirect, url_for
from .crypto import make_key, decrypt


class Server(object):
    def __init__(self,secret_key:bytes,hash_key:bytes or None = None,host="127.0.0.1",port=2839):
        self.secret_key = secret_key
        self.host = host
        self.port = port
        self.app = Flask(__name__)
        self.hash_key = make_key() if not hash_key else hash_key

        @self.app.route("/")
        def main():
            return redirect("/test")
            
        @self.app.route("/test")
        def test():
            return json.dumps({
                "Response-Code":200,
                "User_Agent":request.headers.get("User-Agent"),
                "IPv4":request.remote_addr
            })

    def authorize(self,session):
        print(session.headers.get("SECRET_KEY"))
        print(self.secret_key.decode())
        if decrypt(session.headers.get("SECRET_KEY"),self.hash_key) == self.secret_key.decode():
            return True # Key Matches
        return False # Key doesn't match - 403 forbidden

    def start(self):        
        self.app.run(self.host,self.port)
