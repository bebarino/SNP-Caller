#!/bin/env python
# Inspired by seqLib2.py (Nick Furlotte <nfurlott@cs.ucla.edu>)

import random
import sys
from optparse import OptionParser

def write_FASTA_file(seq, filename, title):
    """Dumps a sequence 'seq' in FASTA file format to 'filename'"""
    f = open(filename, 'w')
    write_FASTA(seq, f, title)
    f.close()

def write_FASTA(seq, f, title, n=78):
    """Dumps a sequence 'seq' in FASTA file format to 'f'"""
    f.write("> %s\n" % title)
    f.writelines(["%s\n" % seq[i:i+n-1] for i in xrange(0,len(seq),n-1)])

def gen_seq(l, letters=['A', 'T', 'C', 'G']):
    """Generates a sequence of length 'l'"""
    return ''.join(random.choice(letters) for _ in xrange(l))

if __name__ == "__main__":
    parser = OptionParser(usage="%prog length [options]")
    parser.add_option("-f", "--file", dest="file",
                      help="write generated sequence to FILE", metavar="FILE")
    parser.add_option("-t", "--title", dest="title", help="title for sequence",
                      metavar="TITLE", default="")

    (options, args) = parser.parse_args(sys.argv[1:])
    if len(args) != 1:
        parser.error("incorrect number of args")
    if not args[0].isdigit():
        parser.error("length not an integer")

    if options.file == None:
        options.file = sys.stdout
    else:
        options.file = open(options.file, 'w')

    write_FASTA(gen_seq(int(args[0])), options.file, options.title)
