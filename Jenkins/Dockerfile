# https://www.hanumoka.net/2019/10/14/docker-20191014-docker-jenkins-docker-in-docker/

FROM jenkins/jenkins:lts


USER root
RUN apt-get update -y \
    && apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"
RUN apt-get update  -y \
    && apt-get install docker-ce -y
RUN service docker start
