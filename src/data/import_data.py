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
        # url = f"https://trace.ncbi.nlm.nih.gov/Traces/sra/?path=https%3A%2F%2Fsra-downloadb.be-md.ncbi.nlm.nih.gov%2Fsos1%2Fsra-pub-run-2%2F{srr}%2F{srr}.1&run={srr}&acc=CM000663.2&ref=chr1&range=&src=0&output=sam&output_to=File"
        url_1 = f"ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR794/00{(4 + i) % 10}/SRR{7949794 + i}/SRR{7949794 + i}_1.fastq.gz"
        url_2 = f"ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR794/00{(4 + i) % 10}/SRR{7949794 + i}/SRR{7949794 + i}_2.fastq.gz"
        command_1 = f"wget {url_1} -P {path}"
        command_2 = f"wget {url_2} -P {path}"
        print(f"start downloading SRR{7949794 + i}_1")
        os.system(command_1)
        print(f"start downloading SRR{7949794 + i}_2")        
        os.system(command_2)
        print(f"finish downloading SRR{7949794 + i}")
        return


def convert_idx(in_dir, out_dir):
    """
    The method to convert the FASTA file into Kallisto index
    """
    command = f"/opt/kallisto_linux-v0.42.4/kallisto index -i {out_dir} {in_dir}"
    print("\n\nstart building the index")
    os.system(command)
    print("\n\nfinish building the index\n\n")
    return