.PHONY: build run clean help

default: help

# Build the Docker image
build: ## Build the application's Docker image
	docker-compose build app

# Run the game in the app service
run: ## Run the game inside a Docker container
	docker-compose run --rm app

# Clean up Docker containers
clean: ## Clean up running Docker containers related to this service
	docker-compose down

help: ## Show this help message
	@echo "Available commands:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
