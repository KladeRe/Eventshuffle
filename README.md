# Eventshuffle
A solution to the Eventshuffle challenge

## Dependencies

Docker compose

## How to run

You can run the containers with docker compose:

```docker compose up```

(or ```docker-compose up``` of you are using and older version of docker compose)

The application expects a .env file with database credentials, an example file could be:
```
HOST = postgres_db
SQL_NAME = tasks_db
SQL_USER = ray
SQL_PASSWORD = password
HOST = postgres_db
PORT = 5432
```
However, these can be freely chosen.