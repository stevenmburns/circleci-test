FROM stevenmburns/pysat_image:2019feb28 as tally_image

COPY tally/ /tally/
COPY .git/ /.git/

RUN \
    bash -c "source general/bin/activate && cd /tally/ && pip install ."














