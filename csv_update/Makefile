run-dev:
	gunicorn csv_update.app:app

run:
	gunicorn --config ./config.py csv_update.app:app

test-dev:
	pip install -r requirements.txt \
	&& pip install -e . \
	&& pytest -s test

tests:
	virtualenv -p python3 .env && source .env/bin/activate \
	&& pip install -r requirements.txt \
	&& pip install -e . \
	&& pytest -s test \
	&& deactivate && rm -rf .env