# KMC3 + howdesbt on all bacterial metaG Tara



Cf [README](../data/README.md) file in the data directory for information about data. 

**Reminder:** 

- there are approx 266 billion distinct kmers in this data set. 
- The total amount of fastq.gz is 6.1TB

This study aims to test how one may create one bloom filter per input read set using `KMC3` in combinaison with `howdesbt`

## Running KMC3 + howdesbt

KMC3: version 3.1.1 (2019-05-19)

howdesbt:  version 2.00.03 (2019-10-14)

**Command line**

Here we removed kmers seen once

We generated bloom filters composed of 4 billion bits each. 

```bash
for file in data/*.fof; 
    do 
        date; 
        name=`basename $file | cut -f 1 -d "."`; 
        echo ${name}; 
        ./kmc -t60 -k20 -cs2 -m256 @${file} ${name}_res .
     ./kmc_dump ${name}_res /dev/stdout | awk '{print $1}' \
     | ./howdesbt makebf /dev/stdin --kmersin K=20 --bits=40000000000 --out=${name}.bf
     rm -f ${name}_res_pre
     rm -f ${name}_res_suf
done
```

The directory `data`contains 241 file of files. Each file of file corresponds to one sample and contains read file names (fastq.gz).

**Computation time**

Because of high computation times, we stopped the processes after 83 bloom filters, leading to 49h computations. 
Based on this observation, and knowing that samples are not sorted by size or complexity, we estimate that for the 241 input samples, `kmc + howdesbt` would require more than 142h for generating the 241 bloom filters. 

**Ressources:** 

disk used 79 GB - including 39 GB of created bloom filters

max memory  213 GB.



**Details about ressources needed:** 

- `kmc` time: 
  - min: 277 seconds
  - max: 1303 seconds
  - avg: 642 seconds
- `kmc` temp disk size:
  - min: 15253MB
  - max: 55037MB
  - avg: 34388MB
- `kmc_dump | howdesbt makebf` time: 
  - avg: 1483 seconds

**Logs**
Computation times, number of kmers, disk used: [log_kmc.txt](log_kmc.txt)

