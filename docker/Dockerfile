FROM --platform=linux/amd64 conda/miniconda3

USER root
RUN conda install -y -c conda-forge mamba
RUN mamba install -y -c conda-forge \
        python=3.9 \
        gdal \
        pygeoprocessing \
        pandas \
        taskgraph \
        matplotlib \
        cxx-compiler \
        jupyter

# Make RUN commands use the new environment:
RUN conda init bash
RUN echo "conda activate myenv" >> ~/.bashrc
ENV PATH /usr/local/bin:$PATH
ADD docker-entrypoint.sh /opt/docker-entrypoint.sh
RUN chmod a+x /opt/docker-entrypoint.sh

# Need to override the default PROJ_LIB; needs the trailing backslash
ENV PROJ_LIB /usr/local/share/proj/

SHELL ["/bin/bash", "--login", "-c"]
ENTRYPOINT ["/opt/docker-entrypoint.sh"]
