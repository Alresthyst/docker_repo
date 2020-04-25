FROM ubuntu:18.04

MAINTAINER Alresthyst

ARG USE_PYTHON_3_NOT_2=1
ARG _PY_SUFFIX=3
ARG PYTHON=python3
ARG PIP=pip3
ARG PYTHON_VERSION=3.7.7

ENV LANG=C.UTF-8


# For basic set-up
RUN apt-get -qq -y update
RUN set -ex \
    && apt-get install -y dpkg-dev g++ gcc build-essential libssl-dev openssl curl libffi-dev libbz2-dev \
    libpng-dev libpq-dev wget zlib1g-dev python-dev\
    && wget --no-check-certificate \
    https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz\
    && mkdir -p /usr/src/python \
    && tar xvfz Python-${PYTHON_VERSION}.tgz \
    && rm Python-${PYTHON_VERSION}.tgz && cd Python-${PYTHON_VERSION} \
    && ./configure \
    && make install \
    && rm -rf /var/lib/apt/lists/* \
    && cd / && rm -rf Python-${PYTHON_VERSION} && python3 --version \
    && apt-get purge -y --auto-remove \
     $(apt-get | grep $(apt-get | grep " install " /var/log/dpkg.log | cut -d " " -f 1| sort -r | head -n 1) \
      /var/log/dpkg.log | grep " install " | cut -d " " -f 4)


# For install pip
RUN apt-get -qq -y update
RUN apt-get -y --no-install-recommends install python3-pip


# Update pip
RUN ${PIP} install --upgrade pip

# Install packages
RUN ${PIP} install flask --no-cache-dir
RUN ${PIP} install flask_restful --no-cache-dir
RUN ${PIP} install requests --no-cache-dir
# Quite large size
#RUN ${PIP} install opencv-python --no-cache-dir
RUN ${PIP} install pillow --no-cache-dir
RUN ${PIP} install scikit-learn --no-cache-dir
RUN ${PIP} install pandas --no-cache-dir
RUN ${PIP} install matplotlib --no-cache-dir
RUN ${PIP} install jupyter notebook --no-cache-dir

CMD ["/bin/bash", "-c", "while true; do echo Still alive; sleep 0.1; done"]



