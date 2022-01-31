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
        ./kmc -t128 -m100 -k20 -ci2  @${file} ${name}_res .
     ./kmc_dump ${name}_res /dev/stdout | awk '{print $1}' \
     | ./howdesbt makebf /dev/stdin --kmersin K=20 --bits=25000000000 --out=${name}.bf
     rm -f ${name}_res_pre
     rm -f ${name}_res_suf
done
```

The directory `data`contains 241 file of files. Each file of file corresponds to one sample and contains read file names (fastq.gz).

The run was made on a TGCC node, limited to 72h of computation. After 72h hours, 196 bloom filters were constructued.

The total estimated running time is 5312 minutes for the 241 samples.

Ressources:

Disk used 0.8 TB (created bloom filters only, no intermediate disk is used during computation).

Max measured memory 101GB


**Logs**
Computation times, number of kmers, disk used: [log_kmc.txt](log_kmc.txt)

