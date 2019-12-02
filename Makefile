clean:
	rm -rf .venv

venv:
	mkdir -p .venv
	pipenv install
