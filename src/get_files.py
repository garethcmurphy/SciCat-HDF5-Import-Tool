#!/usr/bin/env python3
"""get files"""
import os


class GetFiles:
    """fetch files"""
    dir = "./data"
    suffix = ".hdf5"
    files = []

    def __init__(self):
        pass

    def get(self):
        """fetch files"""
        print("getting filenames")
        for file in os.listdir(self.dir):
            if file.endswith(self.suffix):
                fname = os.path.join(self.dir, file)
                self.files.append(fname)

        return self.files


if __name__ == "__main__":
    f = GetFiles()
    nearfiles = f.get()
    print(nearfiles)
