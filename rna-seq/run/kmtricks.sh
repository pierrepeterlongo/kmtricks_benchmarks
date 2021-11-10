#! /bin/bash

in_fof=$1

kmtricks pipeline --run-dir ./run --file ${in_fof} --hard-min 2 --kmer-size 20 --threads 20 --mode
hash:bft:bin --nb-partitions 300 --focus 0.5 --bloom-size 2000000000 --bf-format howdesbt --cpr --verbose info

kmtricks index --run-dir ./run --cull 0.2 --bits 500000 --howde
