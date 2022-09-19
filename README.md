leukemia-diagnostic-assessment
==============================

A short description of the project.

Project Organization
------------

    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │    ├── processed      <- The final, canonical data sets for modeling.
    │    ├── test           <- A sample to for tests.
    │    └── raw            <- The original, immutable data dump.
    │
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering).
    │
    ├── visualizations     <- Data exploration charts.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │    └── build_features.py
    │   │
    │   ├── app       <- Scripts to create a simple dashboard on streamlit
    │   │    ├── logo.png    <- Logo
    │   │    └── app.py      <- Streamlit App
    │   │
    │   └── models         <- Scripts to train models and then use trained models to make
    │       │                 predictions
    │       ├── predict_model.py
    │       └── train_model.py 
    │ 
    ├── test               <- Directory containing unit tests for each directory in the source code.
    ├── setup.cfg          <- Configuration file
    ├── .pre-commit-config.yaml     <- Configuration file for creating a pre-commit hook to evaluate the code's format with black and flake8
    ├── pyproject.toml               <- Configuration files
    │
    └── .gitignore         <- A gitignore file

--------