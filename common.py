from optparse import OptionParser, OptionValueError

def parse_seq(f):
    """Parse a FASTA sequence from the file 'f', returning its full string"""
    if not f.readline().startswith(">"):
        raise Exception("Not a FASTA sequence")
    lines = []
    for line in f:
        if line.startswith(">"):
            break
        lines += [line.strip()]
    return ''.join(lines)

def parser_open_file(option, opt_str, value, parser, mode):
    try:
        f = open(value, mode)
    except IOError, e:
         raise OptionValueError(str(e))
    setattr(parser.values, option.dest, f)
