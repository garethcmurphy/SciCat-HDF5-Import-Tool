#!/usr/bin/env python3
"""post to scicat"""
import requests


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

    def post(self):
        """post to scicat"""
        uri = self.url_base + self.api + self.url_fragment
        print(uri)
        # payload = {}
        response = requests.get(uri)
        print(response.json())
        print(self.url_base)

    def main(self):
        """post to scicat"""
        self.post()


if __name__ == "__main__":
    SCI = SciCatPost()
    SCI.post()
