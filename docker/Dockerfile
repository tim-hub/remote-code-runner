FROM ubuntu:18.04

MAINTAINER Michael Liao

# install gcc, python 3.8, lua 5.3, chezscheme 9.5:

RUN apt-get update \
  && apt-get install -y wget build-essential python3.8 lua5.3 chezscheme9.5 \
  && cd /usr/bin \
  && ln -s python3.8 python3 \
  && ln -s lua5.3 lua \
  && ln -s chezscheme9.5 scheme

RUN apt-get 

# install java 14 at /opt/jdk-14 and link to /usr/bin/java

RUN cd /opt \
  && wget https://download.java.net/java/GA/jdk14/076bab302c7b4508975440c56f6cc26a/36/GPL/openjdk-14_linux-x64_bin.tar.gz \
  && tar zxf openjdk-14_linux-x64_bin.tar.gz \
  && rm openjdk-14_linux-x64_bin.tar.gz \
  && ln -s /opt/jdk-14/bin/java /usr/bin/java

# install node 13 at /opt/node-v13.12.0-linux-x64 and link to /usr/bin/node

RUN cd /opt \
  && wget https://nodejs.org/dist/v13.12.0/node-v13.12.0-linux-x64.tar.gz \
  && tar zxf node-v13.12.0-linux-x64.tar.gz \
  && rm node-v13.12.0-linux-x64.tar.gz \
  && ln -s /opt/node-v13.12.0-linux-x64/bin/node /usr/bin/node

# install ruby 2.7 at /opt/ruby-2.7.1 and build to /usr/local/bin/ruby:

RUN cd /opt \
  && wget https://cache.ruby-lang.org/pub/ruby/2.7/ruby-2.7.1.tar.gz \
  && tar zxf ruby-2.7.1.tar.gz \
  && rm ruby-2.7.1.tar.gz \
  && cd ruby-2.7.1 \
  && ./configure \
  && make \
  && make install

RUN echo "ok"
