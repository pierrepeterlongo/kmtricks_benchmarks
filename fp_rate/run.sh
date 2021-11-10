#!/bin/bash

kmtricks pipeline --file kmtricks.fof --run-dir ./fpr --mode hash:bft:bin --bloom-size 2000000000 --kmer-size 20 --nb-partitions 300 --cpr --threads 20
