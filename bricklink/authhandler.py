import time

from requests_oauthlib import OAuth1

from . import config
from .constants.errors import NotFoundError

class AuthHandler:

    def __init__(self, api, consumerKey, consumerSecret, token, tokenSecret):
        
        self.consumerKey = consumerKey
        self.consumerSecret = consumerSecret
        self.token = token
        self.tokenSecret = tokenSecret

        self.api = api
    
    def getAuth(self):
        auth = OAuth1(self.consumerKey, self.consumerSecret, self.token, self.tokenSecret)
        return auth