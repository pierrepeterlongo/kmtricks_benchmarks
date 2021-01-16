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

## kmtricks - HowDe-SBT
```
cd run ; mkdir 2-KH ; cd 2-KH ; ../kmtricks.sh ../../data/fof_${NB_RNA_SEQ}_kmtricks.txt

```
## McCortex - COBS
```
# COBS must be in your path
cd run ; mkdir 3-MC ; cd 3-MC ; ../cobs.sh ../../data/fof_${NB_RNA_SEQ}.txt
```

