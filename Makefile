.PHONY: all test clean

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = little-big-code-atp-assessment
PYTHON_INTERPRETER = python3

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
requirements: test_environment
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

## Make Dataset
data:
	cd src/features && $(PYTHON_INTERPRETER) build_features.py

## Train Model
train: data
	cd src/models && $(PYTHON_INTERPRETER) train_model.py

## Predict
predict:
	cd src/models && $(PYTHON_INTERPRETER) predict_model.py

## Test
test:
	cd test/features && pytest --cov=src/features test_build_features.py
	cd test/models && pytest --cov=src/models test_train_model.py

## Launch the app
app:
	cd src/app && streamlit run app.py

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8
lint:
	flake8 src

## Test python environment is setup correctly
test_environment:
	$(PYTHON_INTERPRETER) test_environment.py


