FROM openjdk:11-slim

RUN apt-get update
WORKDIR /code/src/java