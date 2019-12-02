clean:
	rm -rf .venv

setup:
	rm .git/hooks/pre-commit
	ln -s hooks/pre-commit .git/hooks/pre-commit

venv-dir:
	mkdir -p .venv

venv-dev: venv-dir
	pipenv install --dev

venv-prod: venv-dir
	pipenv install
