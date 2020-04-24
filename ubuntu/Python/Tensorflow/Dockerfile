FROM kwk1602/ubuntu:py3-jp-remote-v1
MAINTAINER Alresthyst


RUN mkdir /project
WORKDIR /project
COPY . .


ARG USE_PYTHON_3_NOT_2=1
ARG _PY_SUFFIX=3
ARG PYTHON=python3
ARG PIP=pip3
ENV LANG=C.UTF-8
ENV jupyter_port=8888
ENV run_server=False



RUN ${PIP} install pandas
RUN ${PIP} install matplotlib 
RUN ${PIP} install pymssql
RUN ${PIP} install numpy
RUN ${PIP} install scikit-learn
RUN ${PIP} install flask

RUN chmod +x init_parser.sh

CMD ./init_parser.sh --port=$jupyter_port --run_server=$run_server





