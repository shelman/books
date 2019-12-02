clean:
	rm -rf .venv

venv-dir:
	mkdir -p .venv

venv-dev: venv-dir
	pipenv install --dev

venv-prod: venv-dir
	pipenv install
