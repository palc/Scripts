#!/usr/bin/env python

"""Display length of the shortest sequence of a fasta file.

Usage:
    %program file.fasta"""

import sys

try:
    from Bio import SeqIO
except:
    print "This program requires the Biopython library"
    sys.exit(0)

try:
    handle = open(sys.argv[1], 'rU')
    print "Minimum sequence length:", min(map(lambda seq: len(seq.seq), \
        SeqIO.parse(handle, 'fasta')))
except:
    print __doc__
