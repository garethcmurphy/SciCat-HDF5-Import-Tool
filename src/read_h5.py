#!/usr/bin/env python3
"""read h5 files from directory"""
import os
import datetime

import numpy
import h5py
import pytz
from get_files import GetFiles
from scicat_post import SciCatPost


class ReadH5:
    """read h5 files"""
    files = []
    files2 = []
    all_attributes = {}

    def __init__(self):
        pass

    def print_attrs(self, name, obj):
        """recursive"""
        for key, val in obj.attrs.items():
            val2 = val
            try:
                val2 = val.decode('ascii')
            except AttributeError:
                pass
            if isinstance(val2, numpy.int64):
                val2 = int(val2)
            self.all_attributes[name+'/'+key] = val2
            #print ('  "%s/%s": "%s",' % (name,key, val))

    def recursive(self, filename):
        """recursive"""
        file = h5py.File(filename, 'r')
        file.visititems(self.print_attrs)

    def read(self):
        """read h5 files"""
        self.files = []
        get = GetFiles()
        self.files = get.get()
        self.files2 = [self.files[0]]
        print(self.files)
        for file_name in self.files2:
            self.recursive(file_name)
            # print("all attributes", self.all_attributes)
            stat = os.stat(file_name)
            file = h5py.File(file_name, 'r')
            # print(file_name)
            keys = list(file.keys())
            file_attrs = file.attrs
            print(file_attrs)
            scimet = {}
            for key in keys:
                attributes = file[key].attrs
                # print(attributes)
                for name in attributes:
                    # print("{", name, ":", attributes[name], "}")
                    binary = attributes[name]
                    scimet[key+'/'+name] = binary.decode('ascii')
            file.close()
            # print(scimet)
            sci = SciCatPost()
            date = datetime.datetime.now().replace(tzinfo=pytz.utc).isoformat()
            print(date)
            owncloud_location = "https://meas01.esss.lu.se/owncloud/index.php/s/83I00bOPX57kBPZ"
            h5data = {
                "contactEmail": "clement.derrez@esss.se",
                "creationLocation": owncloud_location,
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
                "scientificMetadata": self.all_attributes,
                "size": stat.st_size,
                "sourceFolder": owncloud_location,
                "type": "raw"
            }
            sci.post(h5data)

    def main(self):
        """main"""
        self.read()


if __name__ == "__main__":
    READER = ReadH5()
    READER.main()
