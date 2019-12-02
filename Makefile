run: venv-prod
	pipenv run python -m webapp.app

clean:
	rm -rf .venv

initial-setup:
	./scripts/initialize_git_hooks.sh
	echo "PYTHONPATH=${PYTHONPATH}:`pwd`" >> .env

venv-dir:
	mkdir -p .venv

venv-dev: venv-dir
	pipenv install --dev

venv-prod: venv-dir
	pipenv install
