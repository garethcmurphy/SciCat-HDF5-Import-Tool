#!/usr/bin/env python3
"""read h5 files from directory"""
import os
import datetime

import numpy
import dateutil.parser
import h5py
import pytz
import emoji
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
        dataset_offset = 4
        for file_name in self.files:
            print(emoji.emojize(':bus:  processing '), file_name)
            dataset_offset = dataset_offset + 1
            pid_number = "beam" + str(dataset_offset).zfill(4)
            self.recursive(file_name)
            stat = os.stat(file_name)
            file = h5py.File(file_name, 'r')
            file_attrs = {}
            for key, val in file.attrs.items():
                val2 = val
                try:
                    val2 = val.decode('ascii')
                except AttributeError:
                    pass
                file_attrs[key] = val2

            print(file_attrs)
            date = datetime.datetime.now().replace(tzinfo=pytz.utc).isoformat()
            measurement_date = file_attrs.get("Measurement date", date)
            date_object = dateutil.parser.parse(measurement_date)
            date_string = date_object.replace(tzinfo=pytz.utc).isoformat()
            print(date_string)

            # print(file_attrs)
            file.close()
            sci = SciCatPost()
            # print(date)
            owncloud_location = "https://meas01.esss.lu.se/owncloud/index.php/s/83I00bOPX57kBPZ"
            owner = file_attrs.get("Operator name", "Clement Derrez")
            owner_email = "Clement.Derrez@esss.se"
            self.all_attributes.update(file_attrs)
            h5data = {
                "contactEmail": owner_email,
                "creationLocation": owncloud_location,
                "creationTime": date_string,
                "datasetName":  "Beam Instrumentation " + str(dataset_offset),
                "description": "Beam Instrumentation data",
                "endTime": date_string,
                "isPublished": True,
                "keywords": ["neutron", "beam"],
                "orcidOfOwner": "0000",
                "owner": owner,
                "ownerEmail": owner_email,
                "ownerGroup": "ess",
                "pid": pid_number,
                "principalInvestigator": owner,
                "proposalId": "MRV1E2",
                "scientificMetadata": self.all_attributes,
                "size": stat.st_size,
                "sourceFolder": owncloud_location,
                "type": "raw"
            }
            sci.post(h5data, file_name, stat)


    def main(self):
        """main"""
        self.read()


if __name__ == "__main__":
    READER = ReadH5()
    READER.main()
