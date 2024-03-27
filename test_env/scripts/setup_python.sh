#!/usr/bin/env bash


# runs as root or needs sudo?
if [[ "$EUID" -ne 0 ]]; then
    sudo='sudo'
else
    sudo=''
fi

$sudo apt-get update
$sudo apt-get -y install locales localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
$sudo apt-get -y install vim less
$sudo apt-get -y install supervisor

$sudo pip install --upgrade pip
$sudo pip install --upgrade setuptools
$sudo pip install -r requirements.txt
