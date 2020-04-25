FROM kwk1602/ubuntu-python:v2

ENV jupyter_port=8888
ENV run_server=True

RUN mkdir /work_space
WORKDIR /work_space
COPY . .

RUN chmod +x init_parser.sh

CMD ./init_parser.sh --port=$jupyter_port --run_server=$run_server







