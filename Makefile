DOCKER_DIR=app

install:
	pip install -r app/requirements.txt

api:
	@echo "Starting the API locally..."
	export FLASK_APP=$(DOCKER_DIR)/main.py && export FLASK_ENV=development && flask run --host=0.0.0.0 --port=8000
db:
	@echo "Creating database and Redis containers..."
	docker compose -f $(DOCKER_DIR)/docker-compose.yml up -d db redis

up:
	@echo "Starting all services with Docker Compose..."
	docker compose -f $(DOCKER_DIR)/docker-compose.yml up --build -d

down:
	@echo "Stopping and removing all Docker containers..."
	docker compose -f $(DOCKER_DIR)/docker-compose.yml down

clean:
	@echo "Cleaning up Docker resources..."
	docker system prune -f
	docker volume prune -f

coverage:
	pytest --cov=app --cov-report=term-missing --cov-report=html

test:
	pytest --maxfail=1 --disable-warnings -v
