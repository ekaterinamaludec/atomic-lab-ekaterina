.PHONY: install lint test run clean

install:
	python -m venv venv
	venv\Scripts\activate && pip install -r requirements.lock.txt
	venv\Scripts\activate && pip install black flake8 pytest

lint:
	venv\Scripts\black --check app.py test_app.py
	venv\Scripts\flake8 app.py test_app.py --max-line-length=88

test:
	venv\Scripts\pytest test_app.py -v

run:
	venv\Scripts\python app.py

clean:
	rmdir /s /q venv
	del /s /q *.pyc
