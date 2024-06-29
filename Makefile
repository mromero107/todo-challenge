SHELL := /bin/bash

export NETWORK_NAME ?= invera

COMPOSE_FILE = ./compose/docker-compose.yaml

# Check for NETWORK_NAME network and create it
DOCKER_NETWORK = $(shell docker network ls --filter name=^$(NETWORK_NAME)$$ --format="{{ .Name }}")

start: create_network start_services

start_services:
	docker compose -f $(COMPOSE_FILE) up -d

stop:
	docker compose -f $(COMPOSE_FILE) down

create_network:
ifeq ($(DOCKER_NETWORK),)
	@echo "Creating docker network '$(NETWORK_NAME)'"
	@docker network create $(NETWORK_NAME)
else
	@echo "Docker network '$(NETWORK_NAME)' already exists"
endif

create_superuser:
	docker exec -it invera_todoapp python manage.py createsuperuser

makemigrations:
	docker exec -it invera_todoapp python manage.py makemigrations

migrate:
	docker exec -it invera_todoapp python manage.py migrate
