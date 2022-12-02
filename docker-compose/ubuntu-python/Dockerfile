ARG version=latest

FROM docker.io/ubuntu:${version}

# Install wget & pip
RUN apt-get update && \
    apt-get install -y wget && \
    apt-get install python3-pip -y && \ 
    apt-get clean && \ 
    mkdir /app


COPY ./requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt




 