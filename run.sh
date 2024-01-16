#!/bin/bash
docker stop talana_combat
docker rm talana_combat
docker rmi talana_combat --force

docker build -t talana_combat .

docker run --name talana_combat --restart unless-stopped -p 8008:8008 \
  -v $(pwd):/app talana_combat