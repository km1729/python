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
docker build -t ubuntu .
```

Run a container
PuLL, create, start, attach at once
```bash
docker run -it -d --name container_name image_name
```

access on a running container
```bash
docker attach container_name
```


