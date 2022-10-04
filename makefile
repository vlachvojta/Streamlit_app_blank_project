PY=python3.9
APP=app.py
ST=streamlit
PYCACHE=__pycache__

all: test_local

test_local:
	$(ST) run $(APP)

clean:
	rm -rf $(PYCACHE)

pep8_check:
	$(PY) -m pycodestyle $(wildcard *.py) $(wildcard **/*.py)
	$(PY) -m pydocstyle $(wildcard *.py) $(wildcard **/*.py)

list_requirements:
	pipreqs --force
