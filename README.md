---
title: "Internship Project"
auhtor: "Yağmur Poyraz, Emrah Kırdök"

---

# Introduction

This readme is for the internship project. We will deposit all the information in this repository. 

# Folder hierarchy

This step is important. So we need to decided int the first place. Please place everything to their respective folders.  

We have a data folder but probably we will not push any data to github. If we can download data, then please write a script to download it. We will push data *only if* we have to.

+ data
    + if we can download data, then please 
+ codes
+ results
    + tables
    + plots
    + models
+ report
    + tables
    + figures
    + dotfiles
    + reference.bib
    + codes (to reproduce figures)

Let's follow these guideline.

# Overview of the project

Authentication of ancient DNA reads can be done using alignment based methods. However, it is not possible to align most of the aDNA sequences to reference genome. So, most of the aDNA sequences remain unauthenticated.

In this project, we would like to tackle this problem via usint the frequency difference of *k*-length nucleotide substrings (*k*-mers) between modern and ancient DNA sequences.

![The overview of the methodology in this project](report/figures/general_methodology.png)

# Material and Methods

## Tools

### Gargammel

We will use this tool to simulate modern and ancient DNA sequences. It is possible to download this tool using this [site](https://grenaud.github.io/gargammet/).

### Mapdamage2

This [site](https://ginolhac.github.io/mapDamage/).

## Steps

•	fragSim -n 100000 -l 100 /mnt/c/YAGMUR/staj/sequence.fasta  > modern.fasta   #creating DNA fragments of e.coli to be simulated by deamSim

•	python3.8 k-mer.py –f modern.fasta –k 3 –o kmerthree.kmer  #using pyhton code to divide the DNA simulated by fragSim to k-mers of 3 

•	deamSim -mapdamage misincorporation.txt double modern.fasta -b ancient.bam

•	bwa index sequence.fasta  # indexing the referance genome in order to have faster access 

•	bwa mem sequence.fasta ancient.fasta | samtools view -Sb > antik.bam  #aligning the ancient DNA sequence to referance genome using bwa and turning the output file from sam o into bam file

•	samtools sort antik.bam > antik.sorted.bam

•	samtools index antik.sorted.bam

•	mapDamage -i antik.sorted.bam -r sequence.fasta






