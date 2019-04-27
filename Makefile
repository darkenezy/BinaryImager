test:
	PYTHONPATH=$(PWD) pytest

coverage:
	coverage run -m pytest
	coverage report --omit=*lib* -m

lint:
	pylint binaryimager.py
