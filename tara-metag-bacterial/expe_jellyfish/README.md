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
	/ccc/cont007/home/fg0001/peterlop/jellyfish-linux count --mer-len=20 --canonical --size=3G --lower-count=2 --threads=128 /dev/stdin --output=/dev/stdout | \
	/ccc/cont007/home/fg0001/peterlop/jellyfish-linux dump --column --lower-count=2 /dev/stdin   |  \
	awk '{ print $1 }' | \
	./howdesbt makebf /dev/stdin --kmersin K=20 --bits=25000000000 --out=${name}.bf 
    done < bact_metaG_factorized.list
```

**Computation time**

The run was made on a TGCC node, limited to 72h of computation. After 72h hours, 129 bloom filters were constructued. 

The total estimated running time is 8071minutes for the 241 samples. 

**Ressources:** 

Disk used 0.8 TB (created bloom filters only, no intermediate disk is used during computation).

Max memory  82GB (for the first computed bloom filters).


