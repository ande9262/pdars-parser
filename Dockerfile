FROM centos:latest

RUN yum -y update &&\
    yum -y install python3 &&\
    yum -y install rpm-build

# RUN ["mkdir", "/build"]
COPY setup.py /opt
COPY src /opt/src

WORKDIR /opt
RUN python3 setup.py bdist_rpm --requires python3-numpy
RUN yum install -y dist/pdars-parser-0.0.1-1.noarch.rpm

