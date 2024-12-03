# Eventshuffle
A solution to the Eventshuffle challenge

## Dependencies

Docker compose

## How to run

You can run the containers with docker compose:

```docker compose up```

(or ```docker-compose up``` of you are using and older version of docker compose)

The application has been tested with Docker Compose version v2.23.3

This repository provides a default .env file with PostgreSQL database credentials. These are used when creating the database container, so these can be changed.

Tests are run each time the backend container starts.

## Quick overview

The application consists of a Django backend and a PostgreSQL database. Both of these are containerized using Docker compose.

