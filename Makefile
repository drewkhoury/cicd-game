.PHONY: build run clean

# Build the Docker image
build:
	docker-compose build app

# Run the game in the app service
run:
	docker-compose run --rm app

# Clean up Docker containers
clean:
	docker-compose down
