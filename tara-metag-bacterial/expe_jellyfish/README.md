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
	/ccc/cont007/home/fg0001/peterlop/jellyfish-linux count --mer-len=20 --canonical --size=4G --lower-count=1 --threads=60 /dev/stdin --output=/dev/stdout | \
	/ccc/cont007/home/fg0001/peterlop/jellyfish-linux dump --column --lower-count=1 /dev/stdin   |  \
	awk '{ print $1 }' | \
	./howdesbt makebf /dev/stdin --kmersin K=20 --bits=40000000000 --out=${name}.bf 
    done < bact_metaG_factorized.list
```

**Computation time**

Because of high computation times, we stopped the processes after 10 bloom filters, leading to 9h44 of computations.

**Ressources:** 

disk used 1.1 TB (created bloom filters only, no intermediate disk is used during computation).

max memory  82GB.

**Logs**
Computation times, number of kmers, disk used: [XXX](XXX)

