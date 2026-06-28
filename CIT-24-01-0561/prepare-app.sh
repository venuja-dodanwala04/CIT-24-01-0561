#!/bin/bash

echo "Preparing application..."

docker network create notes-network 2>/dev/null

docker volume create mysql_data

docker compose build

echo "Preparation completed."