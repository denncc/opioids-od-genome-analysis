Opioids Overdose Genome Analysis
==============================

## Project Overview
Opioids are now one of the most common causes of accidental death in the US. According to statistics, two out of three drug overdose deaths in 2018 involved an opioid, so opioid abuse can not only affect people physically and mentally but can also deprive their lives (https://docs.google.com/document/d/1JXWb1Bla8iqvyKl3EUxJcGAWBWTvqfO6rRhn1kzrOr4/edit#bookmark=id.p3zzn76i4h3). Opioid addiction has a unique background in that a large reason for why people become addicted is that patients in hospitals are often prescribed opioids to treat pain, however these patients wind up misusing their prescriptions and become addicted.
This is a data science project curated by Cathleen Peña, Zhaoyi Guo, and Dennis Wu. This github repo contains the codes that are essential to conduct the explicit visualization on the raw data gather from NCBI. 

## Running the Project 

### Pull the Docker Image
To test on the project, in DSMLP, simply pull the image we've generated exclusively for this project by inputting:

    launch-180.sh -i dencc/opioids-od:dw -G B04_Genetics
    
### Clone the Repository
In the directory you want to run the project in, run

    $ mkdir temp
    $ cd ./temp 
    $ git clone https://github.com/denncc/opioids-od-genome-analysis

Then you will be able to run the project the project after cloning

### Test the project
To test on the project, simply input

    python run.py test

You will be able to see the testing procedure to run

## Project Organization
```
📦opioids-od-genome-analysis  
 ┣ 📂config  
 ┃ ┣ 📜data_config.json  
 ┃ ┣ 📜feature_config.json  
 ┃ ┣ 📜submission.json  
 ┃ ┗ 📜test_config.json  
 ┣ 📂data  
 ┃ ┣ 📂external  
 ┃ ┃ ┗ 📜.gitkeep  
 ┃ ┣ 📂interim  
 ┃ ┃ ┗ 📜.gitkeep  
 ┃ ┣ 📂processed  
 ┃ ┃ ┗ 📜.gitkeep  
 ┃ ┣ 📂raw  
 ┃ ┃ ┗ 📜.gitkeep  
 ┃ ┗ 📂test  
 ┃ ┃ ┣ 📂SRR7949794  
 ┃ ┃ ┃ ┣ 📂out.bam  
 ┃ ┃ ┃ ┃ ┗ 📜run_info.json  
 ┃ ┃ ┃ ┣ 📜abundance.h5  
 ┃ ┃ ┃ ┣ 📜abundance.tsv  
 ┃ ┃ ┃ ┣ 📜pseudoalignments.bam  
 ┃ ┃ ┃ ┗ 📜pseudoaln.bin  
 ┃ ┃ ┣ 📜SRR7949794_1.fastq.gz  
 ┃ ┃ ┣ 📜SRR7949794_1.fastq.gz.1  
 ┃ ┃ ┣ 📜SRR7949794_2.fastq.gz  
 ┃ ┃ ┗ 📜SRR7949794_2.fastq.gz.1  
 ┣ 📂docs  
 ┃ ┣ 📜Makefile  
 ┃ ┣ 📜commands.rst  
 ┃ ┣ 📜conf.py  
 ┃ ┣ 📜getting-started.rst  
 ┃ ┣ 📜index.rst  
 ┃ ┗ 📜make.bat  
 ┣ 📂models  
 ┃ ┗ 📜.gitkeep  
 ┣ 📂notebooks  
 ┃ ┣ 📜.gitkeep  
 ┃ ┣ 📜EDA_python.ipynb  
 ┃ ┣ 📜EDA_r.ipynb  
 ┃ ┣ 📜HTSeq.ipynb  
 ┃ ┣ 📜SRA_eda.ipynb  
 ┃ ┣ 📜SRR7949794_cts_htseq.csv  
 ┃ ┣ 📜counts.csv  
 ┃ ┣ 📜cts.csv  
 ┃ ┣ 📜htseq_cts.csv  
 ┃ ┗ 📜htseq_cts.py  
 ┣ 📂references  
 ┃ ┗ 📜.gitkeep  
 ┣ 📂reports  
 ┃ ┣ 📂figures  
 ┃ ┃ ┗ 📜.gitkeep  
 ┃ ┗ 📜.gitkeep  
 ┣ 📂src  
 ┃ ┣ 📂__pycache__  
 ┃ ┃ ┣ 📜__init__.cpython-36.pyc  
 ┃ ┃ ┗ 📜__init__.cpython-37.pyc  
 ┃ ┣ 📂data  
 ┃ ┃ ┣ 📂__pycache__  
 ┃ ┃ ┃ ┣ 📜__init__.cpython-36.pyc  
 ┃ ┃ ┃ ┣ 📜__init__.cpython-37.pyc  
 ┃ ┃ ┃ ┣ 📜import_data.cpython-36.pyc  
 ┃ ┃ ┃ ┗ 📜import_data.cpython-37.pyc  
 ┃ ┃ ┣ 📜.gitkeep  
 ┃ ┃ ┣ 📜__init__.py  
 ┃ ┃ ┣ 📜__init__.pyc  
 ┃ ┃ ┣ 📜import_data.py  
 ┃ ┃ ┗ 📜make_dataset.py  
 ┃ ┣ 📂features  
 ┃ ┃ ┣ 📂__pycache__  
 ┃ ┃ ┃ ┣ 📜__init__.cpython-36.pyc  
 ┃ ┃ ┃ ┣ 📜__init__.cpython-37.pyc  
 ┃ ┃ ┃ ┣ 📜build_features.cpython-36.pyc  
 ┃ ┃ ┃ ┗ 📜build_features.cpython-37.pyc  
 ┃ ┃ ┣ 📂r_scripts  
 ┃ ┃ ┃ ┗ 📜main.R  
 ┃ ┃ ┣ 📜.gitkeep  
 ┃ ┃ ┣ 📜__init__.py  
 ┃ ┃ ┗ 📜build_features.py  
 ┃ ┣ 📂models  
 ┃ ┃ ┣ 📜.gitkeep  
 ┃ ┃ ┣ 📜__init__.py  
 ┃ ┃ ┣ 📜predict_model.py  
 ┃ ┃ ┗ 📜train_model.py  
 ┃ ┣ 📂visualization  
 ┃ ┃ ┣ 📜.gitkeep  
 ┃ ┃ ┣ 📜__init__.py  
 ┃ ┃ ┗ 📜visualize.py  
 ┃ ┣ 📜__init__.py  
 ┃ ┗ 📜__init__.pyc  
 ┣ 📜.gitignore  
 ┣ 📜Dockerfile  
 ┣ 📜LICENSE  
 ┣ 📜Makefile  
 ┣ 📜README.md  
 ┣ 📜command-line-htseq.txt  
 ┣ 📜htseq_cts.py  
 ┣ 📜r-bio.yaml  
 ┣ 📜requirements.txt  
 ┣ 📜run.py  
 ┣ 📜setup.py  
 ┣ 📜test_environment.py  
 ┗ 📜tox.ini
 ```