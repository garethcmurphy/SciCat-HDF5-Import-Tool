#!/usr/bin/env python3
"""read h5 files"""
from get_files import GetFiles
import h5py


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
        print(self.files)
        for file_name in self.files:
            file = h5py.File(file_name, 'r')
            print(file_name)
            keys = list(file.keys())
            for key in keys:
                attributes = file[key].attrs
                print(attributes)
                for name in attributes:
                    print("{", name, ":", attributes[name], "}")
            file.close()

    def main(self):
        """main"""
        self.read()



if __name__ == "__main__":
    READER = ReadH5()
    READER.main()
