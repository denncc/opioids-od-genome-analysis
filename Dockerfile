FROM ucsdets/scipy-ml-notebook:2020.2.9

USER root

# install samtools
RUN apt-get install --yes ncurses-dev libbz2-dev liblzma-dev && \
    cd /opt && \
    wget -q https://github.com/samtools/samtools/releases/download/1.10/samtools-1.10.tar.bz2 && \
    tar xvfj samtools-1.10.tar.bz2 && \
    cd samtools-1.10 && \
    ./configure && \
    make && \
    make install

# install bcftools
RUN apt-get install --yes ncurses-dev libbz2-dev liblzma-dev && \
    cd /opt && \
    wget -q https://github.com/samtools/bcftools/releases/download/1.10.2/bcftools-1.10.2.tar.bz2 && \
    tar xvfj bcftools-1.10.2.tar.bz2 && \
    cd bcftools-1.10.2 && \
    ./configure && \
    make && \
    make install

# FastQC
RUN wget http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip -P /tmp && \
    unzip /tmp/fastqc_v0.11.5.zip && \
    mv FastQC /opt/ && \
    rm -rf /tmp/fastqc_* && \
    chmod 777 /opt/FastQC/fastqc


RUN wget https://github.com/pachterlab/kallisto/releases/download/v0.42.4/kallisto_linux-v0.42.4.tar.gz -P /tmp && \
    tar -xvf /tmp/kallisto_linux-v0.42.4.tar.gz && \
    mv kallisto_* /opt/ && \
    rm /tmp/kallisto_linux-v0.42.4.tar.gz

# HTSeq
RUN pip install HTSeq

RUN rm -rf /opt/*.bz2 && \
    chmod -R +x /opt/*

COPY r-bio.yaml /tmp
RUN conda env create --file /tmp/r-bio.yaml && \
    rm -rf /opt/conda/bin/R /opt/conda/lib/R && \
    ln -s /opt/conda/envs/r-bio/bin/R /opt/conda/bin/R && \
    ln -s /opt/conda/envs/r-bio/lib/R /opt/conda/lib/R
    
# Install WGCNA    
RUN mkdir /opt/iterativeWGCNA && \
    git clone https://github.com/cstoeckert/iterativeWGCNA.git && \
    cd /opt/iterativeWGCNA && \
    python setup.py install
    
    
USER $NB_UID
