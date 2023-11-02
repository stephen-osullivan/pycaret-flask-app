install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

install-train:
	pip install --upgrade pip &&\
		pip install -r requirements_train.txt

lint:
	pylint --disable=R,C *.py

test:
	python -m pytest -vv

launch-app:
	python app.py

sample-predict:
	curl -X POST -H "Content-Type: application/json" -d @sample_predictions.json http://127.0.0.1:5000/predict