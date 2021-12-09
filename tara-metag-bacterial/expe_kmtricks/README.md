# kmtricks on all bacterial metaG Tara



Cf [README](../data/README.md) file in the data directory for information about data. 

**Reminder:** 

- there are approx 266 billion distinct kmers in this data set. 

- The total amount of fastq.gz is 6.1TB

## Running kmtricks

kmtricks release v1.1.1

**Command line**

Here we conserved all kmers from all dataset, before to filter the low abundant one (with thesholds as defined in file `upper_rare_kmer_thresholds_10_percent.txt`) that are not rescued.

We generated bloom filters composed of 4 billion bits each. 

```bash
kmtricks  pipeline \
  --file bact_metaG_factorized.list \
  --run-dir kmtricks111_metag_bact_tara_with_rescue \
  --kmer-size 20 \
  --hard-min 1 \
  --mode hash:bft:bin \
  --soft-min upper_rare_20mer_thresholds_10_percent.txt \
  --share-min 1 \
  --nb-partitions 2500 \
  --focus 0.25 \
  --cpr \
  --bloom-size 25000000000 \
  --bf-format howdesbt \
  --threads 60
```



**Partitions**

- Generates 2500 partitions
- Reminder: 241 read sets

**Computation time**

1 day, 13h, 30m. 

**Ressources:** 

disk used 2.23 TB 

max memory  43 GB

## Creation of the howDeSbt index

```bash
kmtricks  index --run-dir kmtricks111_metag_bact_tara_with_rescue --cull2 --wbits 10000000:20000000 --howde
```
**Computation time**

20h, 20m. 

**Ressources:** 

disk used 0.6 TB 

max memory  165 MB


## Query of the so-created index
Querying `random_10k.fa` containing 10000 reads
```bash
kmtricks query -run-dir ${BRIDGE_MSUB_PWD}/kmtricks110_metag_bact_tara_with_rescue --query random_10k.fa --output res_10k.txt --sort
```
Query time is 18 minutes. 

res_10k.txt contains for each queryied read, its number of shared kmer with each indexed dataset.

