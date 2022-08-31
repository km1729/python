```bash
FROM ubuntu:22.04
MAINTAINER 당신의 정보
RUN apt-get -y update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install jupyter
RUN pip3 install pandas
RUN pip3 install datetime
RUN pip3 install BeautifulSoup4
RUN pip3 install requests
RUN pip3 install lxml


docker build -t ubuntu-python

```