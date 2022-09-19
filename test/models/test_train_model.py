import pandas as pd
from sklearn.linear_model import LogisticRegression
from src.models.train_model import train_model


def test_train_model_returns_the_right_model():
    # given
    dataframe = pd.DataFrame(
        {
            'feature1': [1, 2, 3],
            'feature2': [5, 8, 10],
            'feature3': [2, 9, -1],
            'target': [0, 1, 1],
        }
    )
    # when
    model = train_model(dataframe=dataframe, target_column='target')

    # then
    assert isinstance(model, LogisticRegression)
