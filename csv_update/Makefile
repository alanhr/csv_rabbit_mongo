run-dev:
	gunicorn csv_update.app:app

run-test:
	pytest

run:
	gunicorn --config ./config.py csv_update.app:app