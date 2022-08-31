FROM docker.io/ubuntu:latest

MAINTAINER kelly

RUN apt-get -y update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install jupyter
RUN pip3 install pandas
RUN pip3 install datetime
RUN pip3 install BeautifulSoup4
RUN pip3 install requests
RUN pip3 install lxml



# '''
# 도커 이미지를 빌드하고 컨테이너를 생성 할 수 있도록,
# 커스터마이즈된 설정이 담긴 파일
# 패키지설치, 환경변수 설정, 설정파일 변경등
# '''

# # 이미지
# FROM docker.io/python:3

# WORKDIR /usr/src/app

# #requirements.txt 파일을 루트에 복사
# COPY requirements.txt ./

# #명령실행, 테스트를 위한 패키지가 담긴 requirements.txt를 이용하여 패키지 설치
# RUN pip install --no-cache-dir -r requirements.txt

# #이것은 무슨카피?
# COPY . .


# CMD [ "python", "./your-daemon-or-script.py" ]