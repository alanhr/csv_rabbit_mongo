## Prerequisites

- Install [Docker](https://docs.docker.com/installation/)
- Install [Compose](https://docs.docker.com/compose/install/)

## Stack
- rabbitmq
- mongob
- python 3

### Run test

call the comande `make tests` inside of folders `csv_read` and `csv_upload`

### Run Project

 docker-compose -f "docker-compose.yml" up -d --build

 End-point to update the csv http://127.0.0.1:8080/users/upload

 