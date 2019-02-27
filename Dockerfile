FROM stevenmburns/pysat_image:latest as tally_image

COPY tally/ /tally/
COPY .git/config /.git/config

RUN \
    bash -c "source general/bin/activate && cd /tally/ && pip install ." && \
    rm -r /tally














