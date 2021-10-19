#!/bin/bash

# the here given script was created on the basis of this github repo
# (https://github.com/etopian/alpine-php-wordpress)

function removeOldDocker() {
  echo "> container already exists, rebuilding"
  docker stop wordpress > /dev/null
  docker rm wordpress > /dev/null
}

function createDocker() {
  if [ "$( docker ps -a | grep -c wordpress )" -gt 0 ]; then
    removeOldDocker
  fi
  sudo docker run -e VIRTUAL_HOST=localhost -v /data/sites/etopian.com:/DATA -p 3030:3030 --name wordpress etopian/alpine-php-wordpress
  echo "> container running"
}

sudo mkdir -p /data/sites/etopian.com/htdocs

createDocker

sudo chown -R 100:101 /data/sites/etopian.com/htdocs


