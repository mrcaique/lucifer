#!/usr/bin/env python3

from sys import argv
from datetime import datetime
from random import randrange
from primality_test import fermat, miller_rabin

functions = {"miller_rabin": miller_rabin, "fermat": fermat}
assert len(argv) > 1, "You should pass at least one argument: \
        miller_rabin or fermat." 
assert argv[1] in functions, "Invalid function."
func = functions[argv[1]]

start = datetime.now()

for i in [i*100 for i in range(1, 100)]:
    for _ in range(10000):
        n = randrange(3, 2**i-1)
        if func(n, 100):
            end = datetime.now()
            print("Time: {}\n Bits: {}\n Number: {}\n".format(end-start, i, n))
            break
