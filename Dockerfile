FROM python:3.6-alpine
USER root
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN rm -f "/etc/localtime"
RUN ln -s /usr/share/zoneinfo/Asia/Tehran /etc/localtime
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN mkdir ./restbucks
WORKDIR /restbucks
COPY . /restbucks

RUN adduser -D azarkaman
RUN chown -R azarkaman:azarkaman /restbucks/
ENV PYTHONPATH /restbucks
