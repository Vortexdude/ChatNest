SHELL := bash

.PHONY: apply

apply:
	docker compose -f docker/docker-compose.yml up --remove-orphans --build -d

stop:
	docker compose -f docker/docker-compose.yml down
