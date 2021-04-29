#!/usr/bin/env python

from __future__ import print_function
from string import *
import argparse
import collections
import itertools

parser=argparse.ArgumentParser(description="Calculates k-mer frequencies from a given fasta file(s).")
parser.add_argument('-f', '--file', dest="infile", type =str, help="fasta file for the sequences (do not use for stdin")
parser.add_argument("-k", "--k-mer", dest="kmer", type=int, help="kmer")
parser.add_argument("-o", "--out-file",dest="outfile",type=str,help="name of the resulting file")

args=parser.parse_args()

infile=args.infile
kmer=args.kmer
outfile=args.outfile

bases=["A","T","G","C"]
comps={"A": "T", "T": "A", "G":"C", "C":"G"}

def reverse(seq):
    strand=""
    for nuc in reversed(seq):
        strand=strand+comps[nuc]
    return(strand)

def init_kmer_dict(kmer):
    print("Creating k-mer dictionary")
    dict_kmer={}
    a=[''.join(p) for p in itertools.product(bases, repeat=kmer)]
    for key in a:
        dict_kmer[key]=0
    return(dict_kmer)

def frekuency_kmer(id,seq,dict_kmer,k):
    dict_kmer=dict_kmer.fromkeys(dict_kmer,0) #flushing dictionary
    print("Profiling", id, "with", len(seq),"nucleotides.")
    for n in range(len(seq)-k+1):
        kmer_word=seq[n:n+k]
        dict_kmer[kmer_word]+=1
        kmer_word_reversed=reverse(kmer_word)
        dict_kmer[kmer_word_reversed]+=1

    summed=sum(dict_kmer.values())
    frekuency_table=[]
    frekuency_table.append(id)
    for key in sorted(dict_kmer):
        frek_k=round(float(dict_kmer[key])/summed,4)
        frekuency_table.append(frek_k)
    return(frekuency_table)

def control(seq):
    seq=seq.upper()
    for l in 'NRYMKSWHBVD':
        seq=seq.replace(l, '')
    return seq



def read_fasta(infile):
    try:
        file=open(infile, 'r')
    except:
        file=open("/dev/stdin","r")

    line=file.readline()

    while line!='':
        if line[0]==">":
            seq=[]
            id=line.split()[0][1:]
            print(id)
            line=file.readline()
        if line[0]!=">":
            seq.append(line)
            print("seq found", line)
            line=file.readline()
        
        if line=='':
            sequence= "".join(seq).replace(" ", "").replace("N","").replace("\n", "").upper()
            print (id,sequence)
            frekuency_table=frekuency_kmer(id,sequence,dict_kmer,kmer)
            print(*frekuency_table, sep=":", file=output, end='\n')
            break
        if line[0]==">":
            sequence= "".join(seq).replace(" ", "").replace("N","").replace("\n", "").upper()
            print (id,sequence)
            frekuency_table=frekuency_kmer(id,sequence,dict_kmer,kmer)
            print(*frekuency_table, sep=":", file=output, end='\n')


dict_kmer=init_kmer_dict(kmer)

output=open(outfile,'w')
print("%K-MER:",kmer,file=output,sep="", end="\n")

read_fasta(infile)

output.close()
