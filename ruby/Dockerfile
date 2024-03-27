FROM ruby:3.2.2

ENV LANG=ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV TZ=Asia/Tokyo

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs

WORKDIR /code

COPY Gemfile /code/Gemfile

COPY Gemfile.lock /code/Gemfile.lock

RUN bundle install

