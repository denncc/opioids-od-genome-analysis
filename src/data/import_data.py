import os
import json

with open("./config/data_config.json") as f:
    config = json.load(f)
first_srr = config["download"]["first_srr"]

def download_seq(path, f = "sam"):
    """
    The pipeline to call linux wget to get all dataset into
    the specified locaiton on DSMLP in the specified format
    path: a string of the absolute path on DSMLP
    format: a string of the format of the sequence, 
    sample input: sam, bam, fastq, fasta
    """
    print(type(first_srr), first_srr)
    for i in range(50):
        url = "www.sampleurl.com/SRR" + str(first_srr + i) + "." + f + ".gz"
        print(url)