#!/bin/bash

in_fof=$1

while read -r exp;
do
  IFS=" " read file cutoff <<< "$exp"
  base="$(basename -- $file)"
  zcat $file \
  | jellyfish count --mer-len=20 --canonical --size=3G --lower-count=2 --threads=20 /dev/stdin --output=/dev/stdout \
  | jellyfish dump --column --lower-count=2 /dev/stdin \
  | awk '{ print $1 }' \
  | howdesbt makebf /dev/stdin --kmersin K=20 --bits=2G --out=${base}.bf
done < ${in_fof}

ls *.bf > filterlist

howdesbt cluster --list=filterlist \
--cull=20% --bits=500K --tree=uncompressed.culled.sbt --nodename=node{number}.bf
howdesbt build --determined,brief \
--rrr --tree=uncompressed.culled.sbt --outtree=howde.culled.rrr.sbt
