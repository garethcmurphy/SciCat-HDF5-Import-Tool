#!/usr/bin/env python3
"""read h5 files from directory"""
import os
import datetime

import h5py
from get_files import GetFiles
from scicat_post import SciCatPost


class ReadH5:
    """read h5 files"""
    files = []

    def __init__(self):
        pass

    def read(self):
        """read h5 files"""
        self.files = []
        get = GetFiles()
        self.files = get.get()
        self.files2 = [self.files[0]]
        print(self.files)
        for file_name in self.files2:
            stat = os.stat(file_name)
            file = h5py.File(file_name, 'r')
            print(file_name)
            keys = list(file.keys())
            scimet = {}
            for key in keys:
                attributes = file[key].attrs
                print(attributes)
                for name in attributes:
                    print("{", name, ":", attributes[name], "}")
                    binary = attributes[name]
                    scimet[key+'/'+name] = binary.decode('ascii')
            file.close()
            print(scimet)
            sci = SciCatPost()
            date = datetime.datetime.now().isoformat() 
            h5data = {
                "contactEmail": "clement.derrez@esss.se",
                "creationLocation": "https://meas01.esss.lu.se/owncloud/index.php/s/83I00bOPX57kBPZ",
                "creationTime": date,
                "datasetName":  "Beam Inst",
                "description": "Beam Instrumentation data",
                "endTime": date,
                "isPublished": True,
                "keywords": ["neutron", "beam"],
                "orcidOfOwner": "0000",
                "owner": "Clement Derrez",
                "ownerEmail": "clement.derrez@esss.se",
                "ownerGroup": "ess",
                "principalInvestigator": "Clement Derrez",
                "proposalId": "MRV1E2",
                "scientificMetadata": scimet,
                "size": stat.st_size,
                "sourceFolder": "https://meas01.esss.lu.se/owncloud/index.php/s/83I00bOPX57kBPZ",
                "type": "raw"
            }
            sci.post(h5data)

    def main(self):
        """main"""
        self.read()


if __name__ == "__main__":
    READER = ReadH5()
    READER.main()
