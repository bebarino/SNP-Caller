#!/bin/env python

import sys
from common import *

class SNP(dict):
    """Maintains a tally of SNPs occuring at a single position"""
    def __init__(self, pos, ref):
        dict.__init__(self)
        self.total = 0
        self.pos = pos
        self.ref = ref

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)

def count_snps(reads, ref, snps={}):
    """Tabulate all snps and their positions"""
    for read in reads:
        read, start = read.split()
        start = int(start)
        for (i, (r, s)) in enumerate(zip(ref[start:], read)):
            snp = snps.setdefault(start+i,SNP(start+i, r))
            if r != s:
                if s in snp:
                    snp[s] += 1
                else:
                    snp[s] = 1
            snp.total += 1
    return snps

def consensus(snp):
    """Consensus snp calling method, returns "Unknown" if no majority"""
    best = ('Unknown', 0)
    for k, v in snp.iteritems():
        p = float(v/snp.total)
        if p > best[1]:
            best = (k, v)
    else:
        if best[1] < 0.5:
            best = ('Unknown', 0)
    return "%s %s" % (snp.pos, best[0])

if __name__ == "__main__":
    snps = count_snps(sys.stdin, parse_seq(open(sys.argv[1], 'r')))
    print '\n'.join("%s" % consensus(snp) for snp in snps.values()
                    if len(snp) > 0)
