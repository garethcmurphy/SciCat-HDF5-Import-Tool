#!/usr/bin/env python3
import os

class GetFiles:
    dir="./data"
    
    def __init__(self):
        pass

    def get(self):
        print("getting filenames")
        files = []
        for file in os.listdir(self.dir):
            if file.endswith(".hdf5"):
                fname= os.path.join(self.dir, file)
                files.append(fname)

        return files

if __name__ == "__main__":
    f = GetFiles()
    files =f.get()
    print(files)
