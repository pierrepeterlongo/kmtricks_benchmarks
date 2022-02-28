# Benchmarks kmtricks

This directory synthetises the analyses and results obtained by kmtricks, as described in the paper "*kmtricks: Efficient  construction of Bloom filters and kmer matrices for large sequencing data collections*"

The experiments were conducted with [kmtricks v1.1.1](https://github.com/tlemane/kmtricks/releases/tag/v1.1.1).

## Environment

```bash
conda env create -p km_reproduce --file environment.yml
```
COBS is not available on Conda, installation from the [repository](https://github.com/bingmann/cobs).

## RNA-seq experiments

- see [rna-seq](https://github.com/pierrepeterlongo/kmtricks_benchmarks/tree/master/rna-seq) directory

## TARA Ocean, metagenomics bacterial experiments

- see [tara-metag-bacterial](https://github.com/pierrepeterlongo/kmtricks_benchmarks/tree/master/tara-metag-bacterial) directory



