SHELL := /bin/bash

export NETWORK_NAME ?= invera

COMPOSE_FILE = ./compose/docker-compose.yaml
DEV_COMPOSE_FILE = ./compose/docker-compose.dev.yaml

# Check for NETWORK_NAME network and create it
DOCKER_NETWORK = $(shell docker network ls --filter name=^$(NETWORK_NAME)$$ --format="{{ .Name }}")

start: create_network run_compose_files

start_develop: create_network run_dev_compose_files

run_compose_files:
	docker compose -f $(COMPOSE_FILE) up -d

run_dev_compose_files:
	docker compose -f $(DEV_COMPOSE_FILE) up -d

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
	@if [ -z "$(username)" ] || [ -z "$(email)" ] || [ -z "$(password)" ]; then \
		echo "Error: username, email, and password are mandatory arguments"; \
		exit 1; \
	fi
	docker exec -it invera_todoapp python manage.py createadminuser $(username) $(email) $(password)

makemigrations:
	docker exec -it invera_todoapp python manage.py makemigrations

migrate:
	docker exec -it invera_todoapp python manage.py migrate
