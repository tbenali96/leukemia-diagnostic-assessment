import logging
from pickle import dump

import pandas as pd
from sklearn.linear_model import LogisticRegression


def train_model(dataframe: pd.DataFrame, target_column: str) -> LogisticRegression:
    X = dataframe.drop(columns=[target_column])
    y = dataframe[target_column]
    model = LogisticRegression(
        class_weight="balanced",
        C=0.01,
        penalty="l1",
        solver="liblinear",
        random_state=0,
    )
    model.fit(X.values, y)
    return model


if __name__ == "__main__":
    data = pd.read_csv("../../data/processed/preprocessed_data.csv")
    logging.info("Training ...")
    model = train_model(dataframe=data, target_column="cell_type")
    dump(model, open("../../models/lr_model.pkl", "wb"))
    logging.info("Training done")
