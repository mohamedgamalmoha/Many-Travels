VENV=../venv
PYTHON=$(VENV)/bin/python3

DB_NAME := travel_db
DB_USER := travel_db_user
DB_PASSWORD := 123456
DB_HOST := localhost
DB_PORT := 5432

install:
	$(PYTHON) -m pip install -r requirements.txt

install-requirements:
	$(PYTHON) -m pip install -r requirements.txt

install-postgres:
	sudo apt update
	sudo apt install postgresql postgresql-contrib -y

run-postgres:
	service postgresql start

setup-postgres:
	sudo -u postgres psql -c "CREATE USER ${DB_USER} WITH PASSWORD '${DB_PASSWORD}';"
	sudo -u postgres psql -c "CREATE DATABASE ${DB_NAME} WITH OWNER ${DB_USER};"
	sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE ${DB_NAME} TO ${DB_USER};"

status-postgres:
	service postgresql status

teardown-postgres:
	sudo -u postgres psql -c "DROP DATABASE ${DB_NAME};"
	sudo -u postgres psql -c "DROP USER ${DB_USER};"

stop-postgres:
	service postgresql stop

make-migrations:
	$(PYTHON) manage.py makemigrations

apply-migrations:
	$(PYTHON) manage.py migrate

run-server:
	$(PYTHON) manage.py runserver 0.0.0.0:8000

all: install-requirements install-postgres run-postgres setup-postgres make-migrations apply-migrations run-server

test:
	$(PYTHON) pytest -v -p no:warnings --tb=short --setup-show

clean-cache:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "__pycache__" -exec rm -rf {} \;
