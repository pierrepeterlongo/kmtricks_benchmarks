tab = head(read.table("all_bact_metaG_20_mers_k20.hist"), 10000)
tab = tab[-1,]
tab = tab[-1,]
plot(tab$V1,tab$V2,type="h",xlab="kmer count",log = "y",ylab="count",main="freq. kmers all stations")
