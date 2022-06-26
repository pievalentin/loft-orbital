
.PHONY: migrate
migrate:
	PYTHONPATH=`pwd` poetry run python manage.py migrate

.PHONY: makemigrations
makemigrations:
	PYTHONPATH=`pwd` poetry run python manage.py makemigrations

.PHONY: runserver
runserver :
	PYTHONPATH=`pwd` poetry run python manage.py runserver 8080

.PHONY: shell
shell:
	PYTHONPATH=`pwd` poetry run python manage.py shell_plus

.PHONY: resetdb
resetdb:
	PYTHONPATH=`pwd` poetry run python manage.py reset_db

.PHONY: superuser
superuser:
	PYTHONPATH=`pwd` poetry run python manage.py createsuperuser --email admin@example.com --username admin

.PHONY: tempservice
tempservice:
	docker run -p 1000:4000 --name satellite-temperature -e INTERVAL=20 -d us.gcr.io/loft-orbital-public/hiring/challenges/ground-software/back-end/satellite-temperature

.PHONY: loadtemp
loadtemp:
	PYTHONPATH=`pwd` poetry run python manage.py loaddata temps

.PHONY: freeze
freeze:
	PYTHONPATH=`pwd` poetry export -f requirements.txt --output requirements.txt

.PHONY: tests
tests:
	PYTHONPATH=`pwd` poetry run python -m pytest -vv

.PHONY: up
up:
	docker-compose up

.PHONY: down
down:
	docker-compose down

.PHONY: build
build:
	docker-compose build

.PHONY: format
format:
	PYTHONPATH=`pwd` poetry run black .
	PYTHONPATH=`pwd` poetry run isort .
	PYTHONPATH=`pwd` poetry run mypy .