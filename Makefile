###############################################
#
# Platform plugin portal commands.
#
###############################################

# Define PIP_COMPILE_OPTS=-v to get more information during make upgrade.
PIP_COMPILE = pip-compile --rebuild --upgrade $(PIP_COMPILE_OPTS)

PROJECT_NAME = event_bus_conductor
APP_PATH = event_bus_conductor

.DEFAULT_GOAL := help

.PHONY: requirements


help:  ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

clean:  ## delete most git-ignored files
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

requirements:  ## install environment requirements
	pip install -r requirements/base.txt

upgrade-requirements: export CUSTOM_COMPILE_COMMAND=make upgrade-requirements
upgrade-requirements:  ## update the requirements/*.txt files with the latest packages satisfying requirements/*.in
	# note - on upgrade issues try:
	# pip install pip==22.0.4
	# pip install --upgrade pip-tools

	$(PIP_COMPILE) -o requirements/pip-tools.txt requirements/pip-tools.in
	pip install -qr requirements/pip-tools.txt

	# Make sure to compile files after any other files they include!
	$(PIP_COMPILE) -o requirements/base.txt requirements/base.in
	$(PIP_COMPILE) -o requirements/test.txt requirements/test.in

quality-check: clean  ## check coding style (Ruff)
	ruff check $(APP_PATH)

quality: clean  ## check coding style (Ruff)
	ruff check --fix $(APP_PATH)

format-check: ## show bad formatting (Ruff)
	ruff format --check $(APP_PATH)

format: ## reformat code (Ruff)
	ruff format $(APP_PATH)

bump-check-%: ## check release update effect (bump-my-version)
	bump-my-version bump -v -n $*

bump-%: ## release new version (bump-my-version)
	bump-my-version bump $*

test-requirements:  ## install testing requirements
	pip install -r requirements/test.txt

test: clean  ## run pytest for plugin
	pytest -m "not example" $(args)