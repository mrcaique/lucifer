from sys import argv, exit
from datetime import datetime
from time import time
from collections import Counter
from lcg import LCG
from xorshift import Xorshift
from park_miller import Park_miller

if __name__ == "__main__":
    seed = datetime.now().microsecond
    rounds = 10000000
    bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    if argv[1].lower() == "lcg":
        c = 11
        a = 25214903917
        for n in bits: 
            m = 2**n
            start = time()
            result = LCG(a, c, m)
            result.generate(seed, rounds)
            end = time()
            print((end-start)/rounds)
        exit(0)
    
    if argv[1].lower() == "park_miller" or argv[1].lower() == "pm":
        g = 48271
        for n in bits:
            m = 2**n-1
            start = time()
            result = Park_miller(g, m)
            result.generate(seed, rounds)
            end = time()
            print((end-start)/rounds)
        exit(0)
    
    if argv[1].lower() == "xorshift":
        for n in bits:
            start = time()
            result = Xorshift(1, 2**n)
            result.generate(seed, rounds)
            end = time()
            print((end-start)/rounds)
        exit(0)
