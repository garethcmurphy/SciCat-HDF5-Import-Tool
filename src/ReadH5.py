#!/usr/bin/env python3
from GetFiles import GetFiles
import h5py


class ReadH5:
    def __init__(self):
        get = GetFiles()
        files= get.get()
        for file in files:
            f = h5py.File(file, 'r')
            print(list(f.keys()))
            #g=f['/FMC-PICO/FMC-Pico-1m4-C3'].keys()
            #print(list(g))
            #a=f['/FMC-PICO/FMC-Pico-1m4-C3/18002_CH4_RNG1_OC'].attrs
            #for name in a:
            #    print(name, a[name])
            f.close()

