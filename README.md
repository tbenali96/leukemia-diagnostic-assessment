leukemia-diagnostic-assessment
==============================

The goal of the project is to predict the proportion of lymphocytes B for a patient in order to better and easily have a diagnosis for the chronic lymphocytic leukemia.

Project Organization
------------

    ├── Makefile           <- Makefile with the necessary commands to work with the repository
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
    ├── test               <- Directory containing unit tests for the source code.
    ├── setup.cfg          <- Configuration file
    ├── .pre-commit-config.yaml     <- Configuration file for creating a pre-commit hook to evaluate the code's format with black and flake8
    ├── pyproject.toml               <- Configuration files
    │
    └── .gitignore         <- A gitignore file

--------

The following are some command lines to help use the source code of this project : 

Once you cloned the repository, you first need to create a virtual environment and make sure to download the right libraries. To do so, use :
```
make requirements
```
To launch the web app in order to see some visualizations, you use : 
```
make app
```
For the app, the user is asked to load a dataset, you can use the "raw_data.csv" dataset.
To build the features, you use :
```
make data
```
To train the model, you use :
```
make train
```
For the inference part, you need to upload your sample dataset. The following command will help make the inference on this particular dataset. 
But, in a production environment, we will have to make the dataset an argument for our inference function. 
```
make predict
```
To test and evaluate coverage of our code, you can use :
```
make test
```
Ultimately, the objective of the tests is to create a CI/CD pipeline to validate the correctness of our source code. It is important to note that the tests 
that we created are only related to the code itself, not the Machine Learning artifacts. 
We can, for example, add other tests that evaluate the validity of the model before putting into production. 