#!/bin/env python

import random
import sys
from optparse import OptionParser
from common import *

def gen_reads(seq, l, coverage=1):
    num_reads = int((len(seq)/l) * coverage)
    for _ in xrange(num_reads):
        yield gen_read(seq, l)

def gen_read(seq, l):
    """Generates a random read of length 'l' from the sequence 'seq'"""
    start = random.choice(xrange(len(seq)-l))
    read = seq[start:start+l]
    return (read, start)

def write_reads(rs, f):
    """Write reads 'rs' to a file 'f'"""
    for read in rs:
        f.write('\t'.join(str(x) for x in read))
        f.write('\n')

if __name__ == "__main__":
    parser = OptionParser(usage="%prog length [options]")

    parser.add_option('-f', '--file', dest="infile", default=sys.stdin,
                       help="use reference sequence from FILE", metavar="FILE",
                       type=str, action="callback", callback=parser_open_file,
                       callback_args=('r',))
    parser.add_option('-o', '--out-file', dest='outfile', default=sys.stdout,
                       help="write reads to FILE", metavar="FILE", type=str,
                       action="callback", callback=parser_open_file,
                       callback_args=('w',))
    parser.add_option('-c', '--coverage', dest='coverage', default=1,
                       help="amount of read coverage", metavar="NUM",
                       type=float)

    (options, args) = parser.parse_args(sys.argv[1:])
    if len(args) != 1:
	parser.error('length must be specified')
    if not args[0].isdigit():
        parser.error('length must be a digit')

    write_reads(gen_reads(parse_seq(options.infile), int(args[0]),
                options.coverage), options.outfile)
