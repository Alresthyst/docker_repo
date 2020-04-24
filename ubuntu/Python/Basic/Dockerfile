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
RUN apt-get -qq -y install curl
RUN apt-get -qq -y install gcc g++ build-essential
RUN apt-get -qq -y upgrade
RUN apt-get -qq -y install libssl-dev openssl
RUN apt-get -qq -y install libffi-dev
RUN apt-get -qq -y install wget
RUN apt-get -qq -y install zlib1g-dev
RUN apt-get -qq -y install libpq-dev
RUN apt-get -qq -y install python-dev

# For install python
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz
RUN tar xvfz $(ls | grep ${PYTHON_VERSION})
RUN rm Python-${PYTHON_VERSION}.tgz
WORKDIR Python-${PYTHON_VERSION}
RUN ./configure
RUN make
RUN make install

# For install pip
RUN apt-get -y install python3-pip

# Update pip
RUN ${PIP} install --upgrade pip

# Install packages
RUN ${PIP} install flask --no-cache-dir
RUN ${PIP} install flask_restful --no-cache-dir
RUN ${PIP} install requests --no-cache-dir
RUN ${PIP} install opencv-python --no-cache-dir
RUN ${PIP} install pillow --no-cache-dir
RUN ${PIP} install psycopg2 --no-cache-dir
RUN ${PIP} install scikit-learn --no-cache-dir
RUN ${PIP} install pandas --no-cache-dir
RUN ${PIP} install matplotlib --no-cache-dir
RUN ${PIP} install jupyter notebook --no-cache-dir



CMD ["/bin/bash", "-c", "while true; do echo Still alive; sleep 0.1; done"]







