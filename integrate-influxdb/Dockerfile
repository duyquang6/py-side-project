FROM python:3.7.2-slim
#FROM python:3.7.2-alpine

EXPOSE 5000

WORKDIR /app

RUN apt-get update
RUN apt-get install -y libsnappy-dev gcc g++ tzdata supervisor vim-tiny

ENV TZ=Asia/Bangkok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install statsd

COPY . /app

CMD python main.py
