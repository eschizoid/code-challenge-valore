#!/usr/bin/env bash

docker-compose build \
  --no-cache \
  pipeline

docker-compose up \
  --force-recreate \
  pipeline