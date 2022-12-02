FROM docker.io/ubuntu:latest

WORKDIR /project

ADD install.sh /
RUN chmod UX+X /install.sh

COPY ./requirements.txt /project

EXPOSE 8888
