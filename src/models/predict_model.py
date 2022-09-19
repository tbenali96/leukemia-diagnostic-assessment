import logging
import numpy as np
import pandas as pd
from joblib import load
from src.features.build_features import build_features


def make_predictions(
    data_for_prediction: pd.DataFrame, model_path: str, scaler_path: str, pca_path: str
) -> np.array:
    logging.info("Building the features for the test dataset")
    data = build_features(
        raw_data=data_for_prediction,
        train_or_test="test",
        scaler_path=scaler_path,
        pca_path=pca_path,
    )
    logging.info("Feature Engineering done")
    model = load(model_path)
    return model.predict(data.values)


if __name__ == "__main__":
    test_data = pd.read_csv("../../data/test/sample.csv")
    logging.info("Predicting ...")
    predictions = make_predictions(
        data_for_prediction=test_data,
        model_path="../../models/lr_model.pkl",
        scaler_path="../../models/scaler.pkl",
        pca_path="../../models/pca_model.pkl",
    )
    logging.info("Prediction done")
    print(f"The results of your predictions are : {predictions}")
