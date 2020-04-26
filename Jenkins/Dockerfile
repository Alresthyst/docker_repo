# https://www.hanumoka.net/2019/10/14/docker-20191014-docker-jenkins-docker-in-docker/

FROM jenkins/jenkins:lts


USER root

COPY docker_install.sh /docker_install.sh

RUN chmod +x /docker_install.sh

RUN /docker_install.sh