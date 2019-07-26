import os

class GetFiles:
    dir="./data"
    
    def __init__(self):
        pass

    def get(self):
        files = []
        for file in os.listdir(dir):
            if file.endswith(".hdf5"):
                print(os.path.join("/mydir", file))
                files.append(file)

        return files

if __name__ == "__main__":
    pass
