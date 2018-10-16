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