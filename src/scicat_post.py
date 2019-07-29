#!/usr/bin/env python3
"""post to scicat"""
import platform
import requests
import keyring


class SciCatPost:
    """post raw dataset to scicat """

    url_base = "https://scicatapi.esss.dk"
    api = "/api/v3/"
    url_fragment = "Datasets"
    options = {}

    def __init__(self):
        self.url_base = "http://localhost:3000"
        self.options = {
            'uri': self.url_base
        }

    def get_url(self, token):
        """get URL"""
        uri = self.url_base + self.api + self.url_fragment +"?access_token=" + token
        print(uri)
        return uri

    def get_access_token(self):
        """get access token"""
        if platform.system() == 'Darwin':
            username = "ingestor"
            password = keyring.get_password('scicat', username)
        else:
            pass

        token = ""

        login_url = self.url_base + self.api + "/Users/login"
        config = {
            "username": username,
            "password": password
        }
        response = requests.post(login_url, data=config)
        print(response.json())
        token = response.json()

        return token["id"]

    def create_payload():
        """create payload"""
        payload = {
            "ownerGroup":"ess"
        }
        return payload

    def post(self):
        """post to scicat"""
        token = self.get_access_token()
        uri = self.get_url(token)
        print(uri)
        # payload = {}
        response = requests.get(uri)
        # response = requests.payload(uri, payload)
        print(response.json())
        print(self.url_base)

    def main(self):
        """post to scicat"""
        self.post()


if __name__ == "__main__":
    SCI = SciCatPost()
    SCI.post()
