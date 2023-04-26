FROM docker.io/jupyter/scipy-notebook:latest
# COPY ./environment.yml /home/jovyan/requirements.yml
# RUN conda env update --file requirements.yml --prune
RUN conda update -n base -c conda-forge conda

CMD ["start-notebook.sh"]