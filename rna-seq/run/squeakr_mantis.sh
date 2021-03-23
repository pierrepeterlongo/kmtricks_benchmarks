#!/bin/bash

in_fof=$1

mkdir sq_files
while read -r exp;
do
  IFS=" " read file cutoff <<< "$exp"
  base="$(basename -- $file)"
  squeakr count -e -k 20 -c ${cutoff} -s 31 -t 20 -o sq_files/${base}.squeakr --no-counts ${file}
done < ${in_fof}

ls sq_files/* > sq_files_list
mkdir mantis_index
mantis build -s 31 -i sq_files_list -o mantis_index