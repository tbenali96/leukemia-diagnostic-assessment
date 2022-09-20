import pandas as pd
import streamlit as st
from PIL import Image
from src.models.predict_model import make_predictions


def predict_app():
    image = Image.open("logo.png")
    st.image(image)
    uploaded_file = st.file_uploader("Choose a CSV", type=["csv"])
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
        clicked = st.button("Make the prediction")
        if clicked:
            results = make_predictions(
                data_for_prediction=dataframe,
                model_path="../../models/lr_model.pkl",
                scaler_path="../../models/scaler.pkl",
                pca_path="../../models/pca_model.pkl",
            )
            st.write(f"The results of your predictions are : {results}")


if __name__ == "__main__":
    st.sidebar.markdown("# Predictions")
    predict_app()
