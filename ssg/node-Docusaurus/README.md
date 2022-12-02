```bash
$ docker build . -t hello-world
$ docker run -d -p 5000:3000 --name hello hello-world
# $ docker run -it --rm --name my-node-up my-node
```