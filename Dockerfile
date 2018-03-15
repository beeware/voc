#
# https://docs.docker.com/engine/reference/builder/
#
# https://voc.readthedocs.io/en/latest/background/install.html
#
# https://hub.docker.com/_/python/
FROM python:3.6-alpine


# prepare
RUN set -ex && \
    apk add --no-cache git ca-certificates wget


#
#__________________________________________________________________________________________________
# Install Java 8
# borrowed from: https://github.com/docker-library/openjdk/blob/master/8-jdk/alpine/Dockerfile
#
RUN set -ex && \
    apk add --no-cache openjdk8

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH ${PATH}:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin


#
#__________________________________________________________________________________________________
# Install Apache Ant
# borrowed from: https://github.com/webratio/docker/blob/master/ant/1.10.1/Dockerfile
#
# Version Number: https://www.apache.org/dist/ant/binaries/?C=M;O=A
ENV ANT_VERSION 1.10.2
RUN set -ex && \
    cd /tmp && \
    wget --no-verbose https://www.apache.org/dist/ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.gz && \
    tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \
    rm apache-ant-${ANT_VERSION}-bin.tar.gz && \
    mkdir /opt && \
    mv apache-ant-${ANT_VERSION} /opt/ant

ENV ANT_HOME /opt/ant
ENV PATH ${PATH}:/opt/ant/bin


#
#__________________________________________________________________________________________________
# Install VOC
#

RUN set -ex && \
    python --version && \
    javac -version && \
    ant -version

RUN set -ex && \
    mkdir ~/pybee && \
    cd ~/pybee && \
    git clone --depth=5 https://github.com/pybee/voc.git && \
    cd ~/pybee/voc && \
    pip install -e . && \
    ant java && \
    ls -la dist


#
#__________________________________________________________________________________________________
# build a "Hello World"
# https://voc.readthedocs.io/en/latest/tutorial/tutorial-0.html
#
RUN set -ex && \
    mkdir ~/tutorial0 && \
    cd ~/tutorial0 && \
    echo "print('Hello World!')">example.py && \
    voc -v example.py && \
    java -classpath ~/pybee/voc/dist/python-java-support.jar:. python.example
