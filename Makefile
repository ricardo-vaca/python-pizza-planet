#!/bin/sh

init_db:
	python3 manage.py db init && \
	python3 manage.py db migrate && \
	python3 manage.py db upgrade

seed_db:
	python3 manage.py seed run --root app/seeders

clear_db:
	python3 manage.py clear-db

run:
	python3 manage.py run

test:
	python3 manage.py test
