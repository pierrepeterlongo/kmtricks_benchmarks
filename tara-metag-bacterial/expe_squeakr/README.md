Unfortunately we were unable to run squeakr on Tara ocean samples. 


We raised an issue about this [Segmentation fault · Issue #47 · splatlab/squeakr · GitHub](https://github.com/splatlab/squeakr/issues/47)



The used command line was: 

```bash
squeakr count -k 20 -c 1 -s ${log_slots} -o output_${sample}/res ${input_files} -t 128;
# log_slots value is in [34,36], depending on the datasets.
# output_${sample} directory is created before the run.
```




