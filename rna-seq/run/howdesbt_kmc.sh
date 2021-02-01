#!/bin/bash

in_fof=$1

for fullfile in `cat ${in_fof}`; do
  file=`basename $fullfile`; 
  base=`echo $file | cut -d "." -f 1 `; 
  kmc -k20 -m20 -fa -t20 -ci2 ${file} ${base} ./tmp
  kmc_dump ${base} /dev/stdout | awk '{print $1}' | \
  howdesbt makebf /dev/stdin --kmersin K=20 --bits=2G --out=${base}.bf
  rm ${base}.kmc_pre
  rm ${base}.kmc_suf
done

ls *.bf > filterlist

howdesbt cluster --list=filterlist \
--cull=20% --bits=500K --tree=uncompressed.culled.sbt --nodename=node{number}.bf
howdesbt build --determined,brief \
--rrr --tree=uncompressed.culled.sbt --outtree=howde.culled.rrr.sbt
