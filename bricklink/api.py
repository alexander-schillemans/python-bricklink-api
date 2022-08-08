import base64
import requests
import json
import time

from . import config
from .authhandler import AuthHandler

from .endpoints.orders import OrderMethods

class BrickLinkAPI:

    def __init__(self, consumerKey, consumerSecret, token, tokenSecret):

        self.consumerKey = consumerKey
        self.consumerSecret = consumerSecret
        self.token = token
        self.tokenSecret = tokenSecret

        self.headers = {
            'Accept' : 'application/json',
            'Content-Type' : 'application/json',
        }

        self.baseUrl = config.BASE_URL
        self.authHandler = AuthHandler(self, self.consumerKey, self.consumerSecret, self.token, self.tokenSecret)

        self.orders = OrderMethods(self)

    def doRequest(self, method, url, data=None, headers=None, files=None, auth=None):

        if headers is not None:
            mergedHeaders = self.headers
            mergedHeaders.update(headers)
            headers = mergedHeaders
        else:
            headers = self.headers

        if url.startswith('http'):
            raise('Invalid URL format, do not include base URL: {base}'.format(base=self.baseUrl))
        reqUrl = '{base}/{url}'.format(base=self.baseUrl, url=url)

        if method == 'GET':
            response = requests.get(reqUrl, params=data, headers=headers, auth=auth)
        elif method == 'POST':
            if files: response = requests.post(reqUrl, data=json.dumps(data), files=files, headers=headers, auth=auth)
            else: response = requests.post(reqUrl, data=json.dumps(data), headers=headers, auth=auth)
        elif method == 'PUT':
            response = requests.put(reqUrl, data=json.dumps(data), headers=headers, auth=auth)
        elif method == 'DELETE':
            response = requests.delete(reqUrl, params=json.dumps(data), headers=headers, auth=auth)

        return response

    def request(self, method, url, data=None, headers=None, files=None):

        auth = self.authHandler.getAuth()

        response = self.doRequest(method, url, data, headers, files, auth=auth)
        respContent = json.loads(response.content) if response.content else None

        return response.status_code, response.headers, respContent

    def get(self, url, data=None, headers=None):
        status, headers, response = self.request('GET', url, data, headers)
        return status, headers, response

    def post(self, url, data=None, headers=None, files=None):
        status, headers, response = self.request('POST', url, data, headers, files)
        return status, headers, response

    def put(self, url, data=None, headers=None):
        status, headers, response = self.request('PUT', url, data, headers)
        return status, headers, response

    def delete(self, url, data=None, headers=None):
        status, headers, response = self.request('DELETE', url, data, headers)
        return status, headers, response
