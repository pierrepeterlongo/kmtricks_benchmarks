# kmtricks on all bacterial metaG Tara



Cf [README](https://gitlab.inria.fr/ppeterlo/kmtricks_tara/-/blob/master/data/metaG_bacterial/README.md) file in the data directory for information about data. 

**Reminder:** 

- there are approx 266 billion distinct kmers in this data set. 

- The total amount of fastq.gz is 6.1TB

## Running kmtricks

kmtricks commit [9b8fc49](https://github.com/tlemane/kmtricks/commit/9b8fc4942f819d170488bf6bd2475cf3668a18d2)

**Command line**

```bash
python3 /ccc/cont007/home/fg0001/peterlop/kmtricks_9b8fc49/kmtricks.py run \
  --file /ccc/scratch/cont007/fg0001/peterlop/tara_metaG_bact_kmtricks/bact_metaG_factorized.list \
  --kmer-size 20 \
  --run-dir ${BRIDGE_MSUB_PWD}/kmtricks_metag_bact_tara \
  --count-abundance-min 2 \
  --max-memory 8000 \
  --mode bf_trp \
  --nb-cores 60 \
  --lz4 \
  --merge-abundance-min /ccc/scratch/cont007/fg0001/peterlop/tara_metaG_bact_kmtricks/upper_rare_kmer_thresholds_10_percent.txt \
  --recurrence-min 1 \
  --save-if 1 \
  --max-hash 20000000000 \
  --hasher sabuhash \
  --split howde
```



**Partitions**

- Generates 2544 partitions
- Reminder: 241 read sets

**Computation time**

1 day, 18h, 20 minutes. 

**Ressources:** 

disk used 3151036337 KB (2.93 TB)

max memory  53251100 KB (50 GB)

## Creation of the howDeSbt index, with option --cull

(using kmtricks, version [21f04b4](https://github.com/tlemane/kmtricks/commit/21f04b4dcc197d0ce3b3589d2a7f0df51025e70b))

Determine the tree topology (less than a minute)
`~/kmtricks_21f04b4/bin/howdesbt cluster list_bf.txt --cull --out=cluster_tara 10000000..20000000`
Note that we do not compute the tree topology using the first bits of the bloom filters. This is because, these first bits (first 8 million in this experiment) correspond to the first gatb partition, which contains low complexity kmers. 

Tree has 472 nodes (including 241 leaves)

Create the index: 

`kmtricks_21f04b4/bin/howdesbt build --howde cluster_tara`

- Computation Time: 20h03
- Max Disk Used: 351G
- Max Mem Used: 63G
- Size Directory: 309G
- Directory contains 472 bf files and one sbt file



## Creation of the howDeSbt index, with option --nocull

(using kmtricks, version [21f04b4](https://github.com/tlemane/kmtricks/commit/21f04b4dcc197d0ce3b3589d2a7f0df51025e70b))

Determine the tree topology (less than a minute)
`~/kmtricks_21f04b4/bin/howdesbt cluster list_bf.txt --nocull --out=cluster_tara 10000000..20000000`

Tree has 481 nodes (including 241 leaves)

Create the index: 
`kmtricks_21f04b4/bin/howdesbt build --howde cluster_tara`

- Computation Time: 20h18
- Max Disk Used: 331G
- Max Mem Used: 21G
- Size Directory: 310G
- Directory contains 481 bf files and one sbt file



## THM resources needed to finalise the index

**Time**: 42h20 (kmtricks) + 20h (howde) = 60h

**Max RAM**: 64 GB (howde)

**Max disk usage**: 2.93 TB (kmtricks)

**Index Size**: 309 GB




## Query of the so-created index, with 10 reads
Using kmtrics version [3a3426f](https://github.com/tlemane/kmtricks/commit/3a3426feef0f7fa7a783a31424610eb58dc1cfe9) (close to release 0.0.1)
*Creates a random query, using 10 first reads from set `64SUR0CCKK11`*:
```bash
zcat /ccc/store/cont007/fg0001/fg0001/rawdata/projet_APY/AAAI/RunsSolexa/110712_BISMUTH_63A2BAAXX/APY_AAAIOSF_1_1_63A2BAAXX_clean.fastq.gz | head -n 40 | ./fastq2fasta.py > random10.fa
```
[fastq2fasta.py](https://gitlab.inria.fr/ppeterlo/kmtricks_tara/-/blob/master/scripts/fastq2fasta.py)

**Performs the query**

```
~/kmtricks_3a3426f/bin/howdesbt queryKm --tree=cluster_tara.detbrief.sbt --repart=minimRepart.minimRepart --win=hash_window.vec random.fa
```
Takes 5 minutes 0 bit on disk, and approx 8GB or RAM.

**Result:**
cf [result file](https://gitlab.inria.fr/ppeterlo/kmtricks_tara/-/blob/master/expe/query_howde_kmtricks.txt)
64SUR0CCKK11 is found for all reads except one - number of shared kmers is too low, due to (over?) filtering.
More precisely, 
64SUR0CCKK11 is the target of 9 reads among 10
65DCM0CCKK11 is the target of 5 reads among 10
31SUR1CCII11, 45SUR0CCII11, 64DCM0CCKK11, 65SUR0CCKK11, 78SUR0CCKK11 are the target of 4 reads among 10
...

**Detailled results**:
Adding option --sort (for visualizing) and --threshold=0.01, one finds 64SUR0CCKK11 for all queries, with the highest number of shared kmers. 
This time computation time is 11 minutes. 
cf [result file](https://gitlab.inria.fr/ppeterlo/kmtricks_tara/-/blob/master/expe/query_howde_kmtricks_sort_threshold001.txt)
This result enables to check the number of shared kmers per input query

## Query of the so-created index, with 1000 reads
```bash
zcat /ccc/store/cont007/fg0001/fg0001/rawdata/projet_APY/AAAI/RunsSolexa/110712_BISMUTH_63A2BAAXX/APY_AAAIOSF_1_1_63A2BAAXX_clean.fastq.gz | head -n 4000 | ./fastq2fasta.py > random1000.fa
```



```bash 
~/kmtricks_3a3426f/bin/howdesbt queryKm --tree=cluster_tara.detbrief.sbt --repart=minimRepart.minimRepart --win=hash_window.vec random1000.fa
```

Time: 

real	14m55.844s
user	0m25.813s
sys	7m23.710s

[Result file](https://gitlab.inria.fr/ppeterlo/kmtricks_tara/-/blob/master/expe/query_howde_kmtricks_1000.txt)

Most found read sets: 

 562 78SUR0CCKK11
 565 149SUR0CCKK11
 582 146SUR0CCKK11
 582 78DCM0CCEE11
 585 57SUR0CCKK11
 592 62SUR0CCKK11
 602 78DCM0CCKK11
 608 52DCM0CCII11
 609 148SUR0CCKK11
 619 58DCM0CCKK11
 680 65SUR0CCKK11
 703 64DCM0CCKK11
 707 65DCM0CCKK11
 940 64SUR0CCKK11

