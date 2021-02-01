#!/bin/bash

in_fof=$1

mkdir sq_files
for fullfile in `cat ${in_fof}`; do  
  file=`basename $fullfile`; 
  base=`echo $file | cut -d "." -f 1 `;
  squeakr count -e -k 20 -c 2 -s 31 -t 20 -o sq_files/${base}.squeakr --no-counts ${file}
done 

ls sq_files/* > sq_files_list
mkdir mantis_index
mantis build -s 31 -i sq_files_list -o mantis_index