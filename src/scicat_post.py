#!/usr/bin/env python3
"""post to scicat"""
import platform
import requests
import keyring
import urllib


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
        uri = self.url_base + self.api + self.url_fragment + "?access_token=" + token
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

    def create_payload(self, pid):
        """create payload"""
        payload = {
            "principalInvestigator": "string1",
            "endTime": "2019-07-29T09:10:04.629Z",
            "creationLocation": "string2",
            "dataFormat": "string3",
            "scientificMetadata": {},
            "pid": pid,
            "owner": "string4",
            "ownerEmail": "string5",
            "orcidOfOwner": "string6",
            "contactEmail": "string7",
            "sourceFolder": "string8",
            "type": "raw",
            "size": 0,
            "packedSize": 0,
            "creationTime": "2019-07-29T09:10:04.629Z",
            "keywords": [
                "string",
                "beam"
            ],
            "description": "string9",
            "datasetName": "string10",
            "isPublished": True,
            "ownerGroup": "ess",
            "accessGroups": [
                "loki",
                "odin"
            ],
            "sampleId": "string11",
            "proposalId": "string12"
        }
        return payload

    def post(self):
        """post to scicat"""
        token = self.get_access_token()
        uri = self.get_url(token)
        print(uri)
        prefix = "20.500.12269/"
        pid = "ghfjesl"
        payload = self.create_payload(pid)
        # response = requests.get(uri)
        delete_uri = self.url_base + self.api + "RawDatasets/" + \
            urllib.parse.quote_plus(prefix+pid) + "?access_token="+token
        print(delete_uri)
        response = requests.delete(delete_uri)
        print(response.json())
        response = requests.post(uri, payload)
        print(response.json())
        print(self.url_base)

    def main(self):
        """post to scicat"""
        self.post()


if __name__ == "__main__":
    SCI = SciCatPost()
    SCI.post()
