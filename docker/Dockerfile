FROM --platform=linux/amd64 conda/miniconda3

USER root
RUN conda install -y -c conda-forge mamba
RUN mamba install -y \
        -c conda-forge \
        python=3.9 \
        "gdal<3.5" \
        pygeoprocessing \
        pandas \
        taskgraph \
        matplotlib \
        cxx-compiler \
        jupyter

# Make RUN commands use the new environment:
ADD docker-entrypoint.sh /opt/docker-entrypoint.sh
RUN conda init bash && echo "conda activate myenv" >> ~/.bashrc
ENV PATH /opt/conda/envs/$conda_env/bin:$PATH

# Need to override the default PROJ_LIB; needs the trailing backslash
ENV PROJ_LIB /usr/local/share/proj/

SHELL ["/bin/bash", "--login", "-c"]
ENTRYPOINT ["/opt/docker-entrypoint.sh"]
