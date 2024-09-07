VENV=venv
PYTHON=python
PIP=pip

.PHONY: run clean install

# Create virtualenv
virtual:
	$(PYTHON) -m $(VENV) venv

# Run the application
run:
	$(PYTHON) main.py

#Install dependencies
install:
	$(PIP) install -r requirements.txt

# Clean up Python cache files
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
