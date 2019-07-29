#!/usr/bin/env python3
"""read h5 files from directory"""
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
            h5data = {
                "scientificMetadata": scimet
            }
            sci.post(h5data)

    def main(self):
        """main"""
        self.read()


if __name__ == "__main__":
    READER = ReadH5()
    READER.main()
