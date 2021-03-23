#!/bin/bash

in_fof=$1
mkdir ./tmp
while read -r exp;
do
  IFS=" " read file cutoff <<< "$exp"
  base="$(basename -- $file)"
  kmc -k20 -m20 -fa -t20 -ci${cutoff} ${file} ${base} ./tmp
done < ${in_fof}

mkdir swap_meta
metagraph_DNA build -v --parallel 20 --kmer-length 20 --disk-swap ./swap_meta -o ./meta_ind.dbg *kmc*

metagraph_DNA annotate -v -i ./meta_ind.dbg --parallel 20 --anno-filename -o ./meta_ind.anno *kmc*
