#!/usr/bin/env python3
"""post to scicat"""
import os
import datetime
import platform
import urllib

import keyring
import requests


class SciCatPost:
    """post raw dataset to scicat """

    url_base = "https://scicatapi.esss.dk"
    api = "/api/v3/"
    url_fragment = "Datasets"
    options = {}
    token = ""

    def __init__(self):
        self.url_base = "http://localhost:3000"
        self.url_base = "https://scicatapi.esss.dk"
        self.options = {
            'uri': self.url_base
        }

    def get_url(self):
        """get URL"""
        uri = self.url_base + self.api + self.url_fragment + "?access_token=" + self.token
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

    def create_payload(self, h5data):
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
            "owner":  h5data.get("owner", "Clement Derrez"),
            "ownerEmail":  h5data.get("ownerEmail", "MRV1E2"),
            "ownerGroup": "ess",
            "pid":  h5data.get("pid", "jfklds"),
            "principalInvestigator":   h5data.get("principalInvestigator", "beam inst"),
            "proposalId":  h5data.get("proposalId", "MRV1E2"),
            "scientificMetadata": h5data.get("scientificMetadata", {"a": 1}),
            "sourceFolder":   h5data.get("sourceFolder", "owncloud"),
            "type": "raw"
        }

        # print(payload)
        return payload

    def sci_orig(self, prefixedpid, pathtofile, stat, date_string):
        """post orig data blocks"""
        permissions = oct(stat.st_mode & 0o777)
        orig = {
            "size": stat.st_size,
            "dataFileList": [
                {
                    "path": pathtofile,
                    "size": stat.st_size,
                    "time": date_string,
                    "chk": "string",
                    "uid": stat.st_uid,
                    "gid":  stat.st_gid,
                    "perm": permissions
                }
            ],
            "ownerGroup": "ess",
            "accessGroups": [
                "loki",
                "odin"
            ],
            "datasetId": prefixedpid
        }

        url = self.url_base + self.api + "OrigDatablocks" + "?access_token="+self.token
        print("gm url: ", url)
        print("gm orig", orig)
        response = requests.post(url, json=orig)
        print(response.json())
        return 0

    def delete_orig(self, prefix, pid):
        """delete original data blocks"""
        delete_orig_url = self.url_base + self.api + "Datasets/" + \
            urllib.parse.quote_plus(prefix+pid) + \
            "/origdatablocks?access_token=" + self.token
        requests.delete(delete_orig_url)

    def post(self, h5data, filename, stat):
        """post to scicat"""
        self.token = self.get_access_token()
        uri = self.get_url()
        # print(uri)
        prefix = "20.500.12269/"
        pid = h5data.get("pid", "xyz")
        prefixedpid = prefix+pid
        payload = self.create_payload(h5data)
        self.delete_orig(prefix, pid)
        delete_uri = self.url_base + self.api + "RawDatasets/" + \
            urllib.parse.quote_plus(prefix+pid) + "?access_token="+self.token
        requests.delete(delete_uri)
        response = requests.post(uri, json=payload)
        path = h5data.get("creationLocation", "owncloud")
        basename = os.path.basename(filename)
        path_fragment="/download?path=%2F&files="
        pathtofile = path + path_fragment + basename
        date_string = h5data.get("endTime", "20190101T0101")
        self.sci_orig(prefixedpid, pathtofile, stat, date_string)
        translate = response.json()
        print(translate["pid"])

    def main(self):
        """post to scicat"""
        filename = "rferf"
        h5data = {
            "scientificMetadata": {
                "wavelength": 12
            }
        }
        stat = {
            "st_size": 1123
        }
        self.post(h5data, filename, stat)


if __name__ == "__main__":
    SCI = SciCatPost()
    SCI.main()
