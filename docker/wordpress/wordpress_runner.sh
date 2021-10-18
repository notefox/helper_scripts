#!/bin/bash

# the here given script was created on the basis of this github repo
# (https://github.com/etopian/alpine-php-wordpress)

mkdir -p /data/sites/etopian.com/htdocs

docker run \
  -e VIRTUAL_HOST=etopian.com,www.etopian.com \
  -v /data/sites/etopian.com:/DATA \
  -p 80:80 \
  etopian/alpine-php-wordpress

chown -R 100:101 /data/sites/etopian.com/htdocs

