FROM ubuntu:18.04 as tally_image

RUN apt-get update && apt-get install -yq pkg-config python3 python3-pip python3-venv git build-essential graphviz libgraphviz-dev protobuf-compiler && apt-get clean

RUN \
    python3 -m venv general && \
    bash -c "source general/bin/activate; pip install pytest coverage pytest-cov"

RUN \
    apt-get install zlib1g-dev && \
    bash -c "source general/bin/activate && pip install --upgrade pip && pip install --upgrade wheel && pip install python-sat"

ADD tally/ /tally/

RUN \
    bash -c "source general/bin/activate && cd /tally/ && pip install ." && \
    rm -r /tally














