#!/bin/bash

echo "Removing application..."

docker compose down -v

docker image rm flask-app 2>/dev/null

docker network rm notes-network 2>/dev/null

docker volume rm mysql_data 2>/dev/null

echo "Application removed."