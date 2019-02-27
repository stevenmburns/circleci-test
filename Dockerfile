FROM stevenmburns/pysat_image:latest as tally_image

COPY tally/ /tally/

RUN \
    apt-get update && apt-get install -yq --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    bash -c "source general/bin/activate && cd /tally/ && pip install ." && \
    rm -r /tally














