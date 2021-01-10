test:
	pytest --cov-report term-missing --cov=atm tests/ --cov-fail-under=90

start:
	pipenv run python run_atm.py