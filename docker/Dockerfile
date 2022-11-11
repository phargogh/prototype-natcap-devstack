FROM --platform=linux/amd64 mambaorg/micromamba:1.0.0-bullseye-slim

COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml /tmp/environment.yml
RUN micromamba install -y -n base -c conda-forge -f /tmp/environment.yml && \
        micromamba clean --all --yes
ENTRYPOINT ["/usr/local/bin/_entrypoint.sh"]
