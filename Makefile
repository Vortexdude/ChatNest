LOCAL_EXEC := /bin/bash -c

$(info ------Welcome to Project Developement------)

ifneq ($(app),)
ARGS += --app ${app}
endif

ifneq ($(env),)
ARGS += --env ${env}
endif

.PHONY: start
start:
	@$(LOCAL_EXEC) "(./docker/runner --action $@ ${ARGS})"

.PHONY: stop
stop:
	@$(LOCAL_EXEC) "(./docker/runner --action $@ ${ARGS})"

.PHONY: logs
logs:
	@$(LOCAL_EXEC) "(./docker/runner --action $@ ${ARGS})"
