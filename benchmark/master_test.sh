#!/bin/bash

# $1 = URL of the SequenceServer instance
# $2 = Number of search submitted
# $3 = database1 DNA
# $4 = database2 protein


# --------------------------------------------------
## write out DNA and protein sequences
# subsample DNA data
./seq_count.py dna.fasta --int 3 --outdir dna_1000 --inputfiletype fastq
./seq_count.py dna.fasta --int 5 --outdir dna_2000 --inputfiletype fastq
./seq_count.py dna.fasta --int 12 --outdir dna_5000 --inputfiletype fastq
./seq_count.py dna.fasta --int 25 --outdir dna_10000 --inputfiletype fastq
./seq_count.py dna.fasta --int 124 --outdir dna_50000 --inputfiletype fastq
./seq_count.py dna.fasta --int 247 --outdir dna_100000 --inputfiletype fastq
./seq_count.py dna.fasta --int 1235 --outdir dna_500000 --inputfiletype fastq

# subsample protein data
./seq_count.py protein.fasta --int 1 --outdir protein_1 --inputfiletype fasta
./seq_count.py protein.fasta --int 5 --outdir protein_5 --inputfiletype fasta
./seq_count.py protein.fasta --int 50 --outdir protein_50 --inputfiletype fasta
./seq_count.py protein.fasta --int 100 --outdir protein_100 --inputfiletype fasta
./seq_count.py protein.fasta --int 500 --outdir protein_500 --inputfiletype fasta

# --------------------------------------------------


#Run for DNA sequences:
#./test_script_thread.py --url=$1 --len=0 --num=$2 --seq-file=dna_1000/dna.fasta --db=$3

#Run for protein sequences:
#./test_script_thread.py --url=$1 --len=0 --num=$2 --seq-file=protein_1/protein.fasta --db=$4





# example run
# ./test_script_thread.py --url=localhost:4567 --len=0 --num=10 --seq-file=some_sequence.txt --db=cdd_delta



# set -u
#
# ARG1=""
#
# function USAGE() {
#     printf "Usage:\\n  %s -a ARG\\n\\n" "$(basename "$0")"
#
#     echo "Required arguments:"
#     echo " -a ARG"
#     echo
#     exit "${1:-0}"
# }
#
# [[ $# -eq 0 ]] && USAGE 1
#
# while getopts :a:h OPT; do
#     case $OPT in
#         a)
#             ARG="$OPTARG"
#             ;;
#         h)
#             USAGE
#             ;;
#         :)
#             echo "Error: Option -$OPTARG requires an argument."
#             exit 1
#             ;;
#         \?)
#             echo "Error: Invalid option: -${OPTARG:-""}"
#             exit 1
#     esac
# done
#
# echo "ARG \"$ARG\""
