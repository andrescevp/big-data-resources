# See https://github.com/accso/docker-pentaho-pdi
FROM openjdk:8

ENV JAVA_HOME /usr/local/openjdk-8
ENV PENTAHO_JAVA_HOME /usr/local/openjdk-8

# Install Dependences
RUN apt-get update
RUN apt-get install zip netcat postgresql-client mysql-client  ttf-dejavu -y
RUN apt-get install wget unzip git vim cron nano libwebkitgtk-3.0-0 -y
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN adduser --disabled-login --uid 1000 pentaho
RUN chown pentaho:pentaho /home/pentaho
ENV MAJOR_MINOR_VERSION=8.3
ENV VERSION=8.3.0.0-371
ENV FILENAME=pdi-ce-${VERSION}.zip
ENV URL=https://kent.dl.sourceforge.net/project/pentaho/Pentaho%20${MAJOR_MINOR_VERSION}/client-tools/${FILENAME}
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install \
	   curl \
	   unzip \
	   libwebkitgtk-1.0-0 \
	   libxtst6 \
    && mkdir -p /opt
RUN echo "Downloading ${URL}" \
    && wget --no-check-certificate --progress=dot:giga ${URL} -O /opt/${FILENAME}

RUN mkdir /tmp/down cp ${FILENAME} /tmp/down/${FILENAME}

RUN cd /opt \
    && unzip ${FILENAME} \
    && rm ${FILENAME}

RUN apt-get update
# RUN apt-get install gtk
RUN apt-get install -y xauth
RUN apt-get install -y sudo

RUN mkdir -p ~/.ssh
RUN mkdir -p /home/pentaho/.ssh
RUN echo 'ForwardX11 yes' > ~/.ssh/config
RUN echo 'ForwardX11 yes' > /home/pentaho/.ssh/config

COPY ./connectors/mysql-connector-java-5.1.47.jar /opt/data-integration/lib/mysql-connector-java-5.1.47.jar
COPY ./connectors/mysql-connector-java-5.1.47-bin.jar /opt/data-integration/lib/mysql-connector-java-5.1.47-bin.jar

RUN chmod +x /opt/data-integration/spoon.sh

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENV DOCKER_USER=pentaho
ENTRYPOINT [ "/docker-entrypoint.sh" ]