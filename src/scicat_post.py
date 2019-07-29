#!/usr/bin/env python3
"""post to scicat"""
import datetime
import platform
import urllib

import keyring
import requests


class SciCatPost:
    """post raw dataset to scicat """

    url_base = "https://scicatapi.esss.dk"
    api = "/api/v3/"
    url_fragment = "RawDatasets"
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

    def create_payload(self, pid, h5data):
        """create payload"""
        date = datetime.datetime.now().isoformat()
        payload = {
            "accessGroups": ["loki", "odin"],
            "contactEmail":   h5data.get("contactEmail", "clement.derrez@esss.se"),
            "creationLocation":   h5data.get("creationLocation", "owncloud"),
            "creationTime":   h5data.get("creationTime", date),
            "dataFormat": "hdf5",
            "datasetName": h5data.get("datasetName", "beam inst"),
            "description":   h5data.get("description", "beam inst"),
            "endTime":   h5data.get("endTime", date),
            "isPublished": True,
            "keywords":  h5data.get("keywords", ["neutron", "beam"]),
            "orcidOfOwner":  h5data.get("orcidOfOwner", "beam inst"),
            "owner":  h5data.get("owner", "Clement Derrez"),
            "ownerEmail":  h5data.get("ownerEmail", "MRV1E2"),
            "ownerGroup": "ess",
            "packedSize": h5data.get("size", 0),
            "pid": pid,
            "principalInvestigator":   h5data.get("principalInvestigator", "beam inst"),
            "proposalId":  h5data.get("proposalId", "MRV1E2"),
            "scientificMetadata": h5data.get("scientificMetadata", {"a": 1}),
            "size": h5data.get("size", 0),
            "sourceFolder":   h5data.get("sourceFolder", "owncloud"),
            "type": "raw"
        }

        # print(payload)
        return payload

    def post(self, h5data):
        """post to scicat"""
        token = self.get_access_token()
        uri = self.get_url(token)
        # print(uri)
        prefix = "20.500.12269/"
        pid = "ghfjesl"
        payload = self.create_payload(pid, h5data)
        delete_uri = self.url_base + self.api + "RawDatasets/" + \
            urllib.parse.quote_plus(prefix+pid) + "?access_token="+token
        requests.delete(delete_uri)
        requests.post(uri, json=payload)

    def main(self):
        """post to scicat"""
        h5data = {
            "scientificMetadata": {
                "wavelength": 12
            }
        }
        self.post(h5data)


if __name__ == "__main__":
    SCI = SciCatPost()
    SCI.main()
