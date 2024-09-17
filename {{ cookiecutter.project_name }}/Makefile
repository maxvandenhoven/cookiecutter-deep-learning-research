##########################################################################################
# Docker commands (run on host machine)
# NOTE: These commands work on both Windows and Linux hosts.
##########################################################################################
# Build all Docker images (in this project) using Docker Compose.
.PHONY: build
build:
	@echo Building Docker images ...
	@docker-compose --env-file docker/.env -f docker/docker-compose.yml build

# Start all Docker containers (in this project) using Docker Compose.
.PHONY: up
up:
	@echo Starting Docker containers ...
	@docker-compose --env-file docker/.env -f docker/docker-compose.yml up -d

# Stop all Docker containers (in this project) using Docker Compose.
.PHONY: down
down:
	@echo Stopping Docker containers ...
	@docker-compose --env-file docker/.env -f docker/docker-compose.yml down

# See current Docker containers that are running.
.PHONY: status
status:
	@echo Docker images:
	@docker image ls
	@echo ""
	@echo Docker containers:
	@docker ps
	@echo ""
	@echo Docker Compose instances:
	@docker-compose ls


{% if cookiecutter.setup_devtools == true %}
##########################################################################################
# Devtools commands (run when attached to Docker container)
# NOTE: These commands only work on Linux. 
##########################################################################################
# Format source code using ruff. 
.PHONY: format
format:
	@echo "\033[0;32mSorting imports with ruff ...\033[0m"
	@ruff check --select I --fix
	@ruff format
	@echo ""

# Lint source code using ruff.
.PHONY: lint
lint:
	@echo "\033[0;32mLinting with ruff ...\033[0m"
	@ruff check {{ cookiecutter.__package_name }} tests
	@echo ""

# Test code using pytest.
.PHONY: test
test:
	@echo "\033[0;32mTesting using pytest ...\033[0m"
	@pytest
	@echo ""

# Shortcut for formatting, linting, and testing before committing.
.PHONY: check
check: format lint test
{% endif %}