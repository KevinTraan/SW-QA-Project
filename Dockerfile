FROM python:3.8-slim
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip3 install -r requirements.txt
ADD . /app
ADD wait-for-it.sh /app
RUN apt-get update && apt-get install -y dos2unix
RUN dos2unix wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh
EXPOSE 8081