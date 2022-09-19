import logging
import pickle
from pickle import dump
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

IRRELEVANT_COLUMNS = ['patient_name', 'spectre', 'cell_name', 'patient_state']
TARGET_COLUMN = ['cell_type']


def clean_data(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    df = df.drop_duplicates()
    return df.drop(columns=columns)


def scale_numeric_features(df: pd.DataFrame, train_or_test: str, scaler_path: str):
    if train_or_test == 'train':
        features = df.drop(columns=TARGET_COLUMN)
        numeric_columns = features.select_dtypes(['int64', 'float64']).columns
        scaler = StandardScaler()
        scaler.fit(df[numeric_columns])
        dump(scaler, open(scaler_path, 'wb'))
    if train_or_test == 'test':
        numeric_columns = df.select_dtypes(['int64', 'float64']).columns
        with open(scaler_path, 'rb') as f:
            scaler = pickle.load(f)
    df[numeric_columns] = scaler.transform(df[numeric_columns])
    return df


def reduce_dimension(df: pd.DataFrame, train_or_test: str, pca_path: str):
    if train_or_test == 'train':
        features = df.drop(columns=TARGET_COLUMN).columns
        pca_model = PCA(n_components='mle')
        pca_model.fit(df[features])
        dump(pca_model, open(pca_path, 'wb'))
    if train_or_test == 'test':
        features = df.columns
        with open(pca_path, 'rb') as f:
            pca_model = pickle.load(f)
    principal_components = pca_model.transform(df[features])
    columns_name = []
    for i in range(1, principal_components.shape[1] + 1):
        columns_name.append(f'principal_component_{i}')
    principal_df = pd.DataFrame(data=principal_components,
                                columns=columns_name)
    if train_or_test == 'test':
        return principal_df
    if train_or_test == 'train':
        return pd.concat([principal_df, df[TARGET_COLUMN]], axis=1)


def build_features(raw_data: pd.DataFrame, train_or_test: str, scaler_path: str, pca_path: str) -> pd.DataFrame:
    data = clean_data(raw_data, columns=IRRELEVANT_COLUMNS)
    data = scale_numeric_features(data, train_or_test, scaler_path)
    data = reduce_dimension(data, train_or_test, pca_path)
    return data


if __name__ == '__main__':
    raw = pd.read_csv("../../data/raw/raw_data.csv", sep=";")
    logging.info("Building the features")
    preprocessed_data = build_features(raw_data=raw,
                                       train_or_test="train",
                                       scaler_path='../../models/scaler.pkl',
                                       pca_path='../models/pca_model.pkl')
    logging.info("Feature Engineering done")
    preprocessed_data.to_csv("../../data/processed/pre_processed_data.csv", index=False)