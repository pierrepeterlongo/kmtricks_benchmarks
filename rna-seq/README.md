# Download

```
# In kmtricks paper, NB_RNA_SEQ is 100 or 674
NB_RNA_SEQ=1 ; cd data ; ./download.sh $NB_RNA_SEQ ; ./fof.sh $NB_RNA_SEQ ; cd ..
```

This command downloads `${NB_RNA_SEQ}` fasta.gz files (at ./data/fasta) and produces two files `fof_${NB_RNA_SEQ}_kmtricks.txt` and `fof_${NB_RNA_SEQ}.txt`

# Run

## Jellyfish - HowDe-SBT
```
cd run ; mkdir 1-JH ; cd 1-JH ; ../howdesbt.sh ../../data/fof_${NB_RNA_SEQ}.txt
```

## KMC - HowDe-SBT
```
cd run ; mkdir 2-KmH ; cd 2-KmH ; ../howdesbt_kmc.sh ../../data/fof_${NB_RNA_SEQ}.txt
```
## kmtricks - HowDe-SBT
```
cd run ; mkdir 3-KH ; cd 3-KH ; ../kmtricks.sh ../../data/fof_${NB_RNA_SEQ}_kmtricks.txt

```
## McCortex - COBS
```
# COBS must be in your path
cd run ; mkdir 4-MC ; cd 4-MC ; ../cobs.sh ../../data/fof_${NB_RNA_SEQ}.txt
```

## KMC - Metagraph
```
cd run ; mkdir 5-KM ; cd 5-KM ; ../metagraph.sh ../../data/fof_${NB_RNA_SEQ}.txt
```
