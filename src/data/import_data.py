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
        srr = "SRR" + str(first_srr + i)
        url = f"https://trace.ncbi.nlm.nih.gov/Traces/sra/?path=https%3A%2F%2Fsra-downloadb.be-md.ncbi.nlm.nih.gov%2Fsos1%2Fsra-pub-run-2%2F{srr}%2F{srr}.1&run={srr}&acc=CM000663.2&ref=chr1&range=&src=0&output=sam&output_to=File"
        print(url)
