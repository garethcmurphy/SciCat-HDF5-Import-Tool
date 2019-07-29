#!/usr/bin/env python3
from GetFiles import GetFiles
import h5py


class ReadH5:
    def __init__(self):
        files = []
        get = GetFiles()
        files = get.get()
        print(files)
        for file in files:
            f = h5py.File(file, 'r')
            print(file)
            keys = list(f.keys())
            for key in keys:
                a = f[key].attrs
                print(a)
                for name in a:
                    print("{" ,name, ":" ,a[name] , "}")
            f.close()


if __name__ == "__main__":
    r = ReadH5()
