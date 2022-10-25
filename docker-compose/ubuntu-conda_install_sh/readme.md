Buid an image from the Dockerfile
```bash
FROM docker.io/conda/miniconda3

WORKDIR /app
COPY . /app
#RUN conda install --file requirements.txt
CMD ["bin/bash"]
```

```bash
docker build -t miniconda3
```

