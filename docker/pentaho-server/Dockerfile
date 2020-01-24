FROM openjdk:8-jdk

ENV PENTAHO_HOME /opt/pentaho

RUN . /etc/environment
ENV JAVA_HOME /usr/local/openjdk-8
ENV PENTAHO_JAVA_HOME /usr/local/openjdk-8
ENV CATALINA_OPTS="-Djava.awt.headless=true -Xms4096m -Xmx6144m -XX:MaxPermSize=256m -Dsun.rmi.dgc.client.gcInterval=3600000 -Dsun.rmi.dgc.server.gcInterval=3600000"

# Install Dependences
RUN apt-get update
RUN apt-get install zip netcat postgresql-client mysql-client  ttf-dejavu -y
RUN apt-get install wget unzip git vim cron nano libwebkitgtk-1.0-0 -y
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir ${PENTAHO_HOME}; useradd -s /bin/bash -d ${PENTAHO_HOME} pentaho; chown pentaho:pentaho ${PENTAHO_HOME}

RUN mkdir /jobs

VOLUME /etc/cron.d
VOLUME /jobs

# Download PDI
RUN wget --progress=dot:giga https://downloads.sourceforge.net/project/pentaho/Pentaho%208.2/server/pentaho-server-ce-8.2.0.0-342.zip -O /tmp/pentaho-server.zip
RUN /usr/bin/unzip -q /tmp/pentaho-server.zip -d $PENTAHO_HOME;
RUN rm -f /tmp/pentaho-server.zip;
RUN rm -f /opt/pentaho/pentaho-server/promptuser.sh

EXPOSE 8080

COPY run_pentaho_server.sh /usr/local/bin
RUN chmod +x /usr/local/bin/run_pentaho_server.sh
CMD /usr/local/bin/run_pentaho_server.sh