run: venv-prod
	pipenv run python -m webapp.app

clean:
	rm -rf .venv

initial-setup:
	rm .git/hooks/pre-commit
	ln -s hooks/pre-commit .git/hooks/pre-commit
	echo "PYTHONPATH=${PYTHONPATH}:`pwd`" >> .env

venv-dir:
	mkdir -p .venv

venv-dev: venv-dir
	pipenv install --dev

venv-prod: venv-dir
	pipenv install
