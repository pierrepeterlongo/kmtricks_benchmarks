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
  --run-dir findere_kmtricks_metag_bact_tara_with_rescue \
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

23h53  

**Ressources** 

disk used: 1.1 TB 
max memory:  83.4 GB

## Creation of the howDeSbt index

```bash
kmtricks  index --run-dir findere_kmtricks_metag_bact_tara_with_rescue --cull2 --wbits 10000000:20000000 --howde
```
**Computation time**

20h, 49m. 

**Ressources** 

disk used: 0.6 TB 
max memory:  165 GB


## Query of the so-created index
Querying `random_10k.fa` containing 10000 reads. All those reads come from the 64SUR0CCKK11 station.
```bash
kmtricks query -run-dir findere_kmtricks_metag_bact_tara_with_rescue query random_10k.fa --output res_10k.txt -z 2
```
**Compuatation time**

12 minutes (for the 10000 queries)

**Ressources**

disk used: 0.08 GB
max memory: 11 GB


res_10k.txt contains for each queryied read, its number of shared kmer with each indexed dataset.

## First quick analyse of the obtained results
* Similarity agerage with 64SUR0CCKK11
```
grep 64SUR0CCKK11 res_10k.txt | cut -d " " -f 3 | awk '{ total += $1; count++ } END { print total/count }'
```
Result: 0.996808. This means that in average 99.7% of the kmers from queried reads (from 64SUR0CCKK11) are indexed in 64SUR0CCKK11. This is normal that we do not reach 100% as some kmers are filtered during the indexation.


* Similarity average with all stations in term of number of positions covered by at least a shared kmer:
```
for station in `cat bact_metaG_factorized.list | cut -d " " -f 1`; do echo -n "$station "; grep $station res_10k.txt | cut -d " " -f 4 | awk '{ total += $1; count++ } END { print total/count }'; done | sort -k 2 -n -r > res_similarity_sorted.txt
```
Result:
```
64SUR0CCKK11 0.999539
64DCM0CCKK11 0.984079
48SUR0CCII11 0.983414
65SUR0CCKK11 0.983078
65DCM0CCKK11 0.982879
...
```
We find as expected 64SUR0CCKK11 as the most similar with reads from itself. Other lines enable to measure the similarity between those 10000 reads and each station. 64SUR0CCKK11 is not strickly equal to 1 as some of its kmers were wrongly filtered. 


* Average number of shared kmers with all stations: 
```
for station in `cat bact_metaG_factorized.list | cut -d " " -f 1`; do echo -n "$station "; grep $station res_10k.txt | cut -d " " -f 3 | cut -d "/" -f 1 | awk '{ total += $1; count++ } END { print total/count }'; done | sort -k 2 -n -r > res_nb_kmers_sorted.txt
```
Again 64SUR0CCKK11 has the highest number of shared kmers with itself. 
```
Result:
64SUR0CCKK11 0.991061
65SUR0CCKK11 0.914656
64DCM0CCKK11 0.913087
48SUR0CCII11 0.911663
45SUR0CCII11 0.911454
...
```

Results files are stored in this directory
