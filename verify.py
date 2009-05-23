#!/bin/env python

import sys
from common import parse_seq

def verify(seq, reads):
    error = 0
    total = 0
    for read in reads:
        total += 1
        pos, snp = read.split()
        pos = int(pos)
        if snp != seq[pos]:
            error += 1
    return error, total

if __name__ == "__main__":
    seq = parse_seq(open(sys.argv[1], 'r'))
    print "errored: %s\ntotal:%s" % verify(seq, sys.stdin)
