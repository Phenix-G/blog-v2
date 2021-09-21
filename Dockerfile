FROM python:3.8.11

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y

RUN mkdir /code
WORKDIR /code

RUN pip install pip -U -i https://pypi.tuna.tsinghua.edu.cn/simple

ADD . /code/

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple