FROM docker.io/ubuntu:latest

# Install base utilities
RUN apt-get update && \
    apt-get install -y wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install minicondacond
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
     /bin/bash ~/miniconda.sh -b -p /opt/conda && \
     rm ~/miniconda.sh && \
     ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
     echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
     echo "conda activate base" >> ~/.bashrc && \
     echo "source ~/.bashrc"


# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

RUN conda update -y conda 
