#!/bin/bash
cd server
export DOCKER_BUILDKIT=1
export COMPOSE_DOCKER_CLI_BUILD=1
docker compose up --build --force-recreate &

cd ../client
docker build . -t "pokermon-client:v1.0"
docker run -p 3000:3000 pokermon-client:v1.0 &

