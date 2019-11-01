#!/usr/bin/env python3
"""
Author : kblumberg
Date   : 2019-10-29
Purpose: Prepare DNA or protein fasta sequences to benchmark applictions running Blast
"""

import argparse
import sys
import os
import shutil
from Bio import SeqIO

"""
./seq_count.py dna.fasta --int 3 --outdir dna_1000 --inputfiletype fastq
"""

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Seperate FASTQ sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FASTA', help='Input FASTA file(s)', nargs='+')

    parser.add_argument(
        '-o',
        '--outdir',
        help='A named string argument',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
        '--int',
        help='number of reads to grab',
        metavar='num_reads',
        type=int,
        default=50)

    parser.add_argument(
        '-t',
        '--inputfiletype',
        help='string file type fasta or fastq',
        type=str,
        default='fasta')

    # parser.add_argument(
    #     '-f', '--flag', help='A boolean flag', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    outdir_arg = args.outdir
    num_reads_arg = args.int
    pos_arg = args.positional
    infile_type = args.inputfiletype
    num_seq = 0

    #create outdir
    if os.path.exists(outdir_arg):
        shutil.rmtree(outdir_arg)
    os.makedirs(outdir_arg)

    for file in pos_arg:
        if not os.path.isfile(file):
            print('"{}" is not a file'.format(file), file=sys.stderr)

    for file in pos_arg:
        #check if positional arguments are files
        if os.path.isfile(file):
            basename = os.path.basename(file)
            #make outstring file path
            names = os.path.splitext(basename)
            low_str = names[0] + names[1]
            low_file_path = os.path.join(outdir_arg, low_str)
            low_fh = open(low_file_path, 'wt')

            with open(file) as f:
                for rec in SeqIO.parse(f, infile_type):
                    num_seq += 1
                    SeqIO.write(rec, low_fh, "fasta")
                    if num_seq >= num_reads_arg:
                        break

    print('Done, wrote {} sequences to out dir "{}"'.format(num_seq, outdir_arg))

# --------------------------------------------------
if __name__ == '__main__':
    main()
