# Jellyfish on all bacterial metaG Tara

<u>RUNNING</u>



Cf [README](../data/README.md) file in the data directory for information about data. 

**Reminder:** 

- there are approx 266 billion distinct kmers in this data set. 
- The total amount of fastq.gz is 6.1TB

This study aims to test how one may create one bloom filter per input read set using `fellyfish` in combinaison with `howdesbt`

## Running fellyfish+ howdesbt

 jellyfish: version 2.3.0

howdesbt:  version 2.00.03 (2019-10-14)

**Command line**

Here we removed kmers seen once

We generated bloom filters composed of 4 billion bits each. 

```bash
while read y; do 
    name=`echo $y |cut -f 1 -d ":"`;   
    name=`echo $name | sed 's/ *$//g'` # trim
    files=`echo $y |cut -f 2- -d ":" | tr ";" " ";`; 
    date;  
    echo $name; 
    zcat $files | \ 
	/ccc/cont007/home/fg0001/peterlop/jellyfish-linux count --mer-len=20 --canonical --size=4G --lower-count=2 --threads=60 /dev/stdin --output=/dev/stdout | \
	/ccc/cont007/home/fg0001/peterlop/jellyfish-linux dump --column --lower-count=2 /dev/stdin   |  \
	awk '{ print $1 }' | \
	./howdesbt makebf /dev/stdin --kmersin K=20 --bits=40000000000 --out=${name}.bf 
    done < bact_metaG_factorized.list
```

**Computation time**

Because of high computation times, we stopped the processes after 55.3h of computation, leading to 73 constructed bloom filters. 

In the manuscript, we present results for 50h hours of computations, leading to 66 constructed bloom filters. 

In both cases the total estimated running time is ~182h for the 241 samples. 

Average computation time: 2731 sec.

**Ressources:** 

Disk used 1.1 TB (created bloom filters only, no intermediate disk is used during computation).

Max memory  82GB (for the first computed bloom filters).

**Logs**
Computation times, number of kmers, disk used: [log_jellyfish_stopped.txt](log_jellyfish_stopped.txt)

