Dockerfile
```bash
FROM docker.io/ubuntu:latest

WORKDIR /project

RUN apt-get -y update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip

COPY ./requirements.txt /project

EXPOSE 8888
```

Build an image
```bash
docker build -t ubuntu-python .
```

Run a container
```bash
docker run -it ubuntu-python
```


