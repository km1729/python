#!/bin/bash

apt-get update
apt-get upgrade -y
apt-get -y install python3
apt-get -y install python3-pip
apt-get clean

# Install miniconda and remove Minocnda.sh 
wget --quiet https://repo.anaconda.com/miniconda/Miniconda2-4.5.11-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh 

# Add env Path

ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh
echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
echo "conda activate base" >> ~/.bashrc

# python library