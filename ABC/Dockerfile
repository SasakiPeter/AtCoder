FROM python:3.4.3

RUN apt-get update && apt-get install -y \
  sudo \
  cmake \
  python3-setuptools &&\
  apt-get clean && \ 
  rm -rf /var/lib/apt/lists/* &&\
  pip --no-cache-dir install --upgrade pip setuptools &&\
  pip --no-cache-dir install \
  numpy \
  scipy