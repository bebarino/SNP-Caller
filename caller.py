#!/bin/env python

import sys
from common import *

def count_snps(reads, ref, snps={}):
    """Tabulate all snps and their positions"""
    for read in reads:
        read, start = read.split()
        start = int(start)
        for (i, (r, s)) in enumerate(zip(ref[start:], read)):
            if r != s:
                stat = snps.get(start+i,{})
                if s in stat:
                    stat[s] += 1
                else:
                    stat[s] = 1
                snps[start+i] = stat
    return snps

def consensus(snps):
    """Return the snp with the highest frequency at each position"""
    return [(max(snp), pos) for pos, snp in snps.iteritems()]

if __name__ == "__main__":
    print consensus(count_snps(sys.stdin, parse_seq(open(sys.argv[1], 'r'))))
