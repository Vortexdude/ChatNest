compose_file := ./docker/docker-compose.yml

FONT_RED := $(shell tput setaf 1)
FONT_GREEN := $(shell tput setaf 2)
FONT_YELLOW := $(shell tput setaf 3)
FONT_BLUE := $(shell tput setaf 4)
FONT_PURPLE := $(shell tput setaf 5)
FONT_CYAN := $(shell tput setaf 6)
FONT_GRAY := $(shell tput setaf 7)
FONT_BLACK := $(shell tput setaf 8)
FONT_BOLD := $(shell tput bold)
FONT_RESET := $(shell tput sgr0)


print:
	@printf "\n$(FONT_GREEN)------Welcom To The Project Development-----$(FONT_RESET)\n"
	@printf "\n$(FONT_GREEN)Using the compose file $(compose_file)$(FONT_RESET)\n"

$(info  $(bold)$(compose_file)$(sgr0))

build: print
	docker compose -f $(compose_file) build

up: print
	docker compose -f $(compose_file) up -d

down: print
	docker compose -f $(compose_file) down

web-bash:
	docker exec -it chatnest bash

restart: print down up

log: print
	docker logs --follow chatnest
