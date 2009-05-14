#!/bin/env python

import sys
import random

def snpify(seq, p):
    """Change a letter in the sequence 'seq' with probability 'p'"""
    for line in seq:
        # Don't touch titles
        if line.startswith(">"):
            yield line
            continue

        for l in line[:-1]:
            if random.random() < p:
                yield random.choice(line[:-1])
            else:
                yield l
        yield line[-1]

if __name__ == "__main__":
    prob = 0.05
    if len(sys.argv) == 2:
	prob = float(sys.argv[1])

    for line in snpify(sys.stdin, prob):
        sys.stdout.write(line)
