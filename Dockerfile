FROM stevenmburns/pysat_image:2019mar08 as tally_image

COPY tally/ /tally/

RUN \
    bash -c "source general/bin/activate && cd /tally/ && pip install ."














