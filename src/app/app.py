import pandas as pd
import plotly.express as px
from plotly.graph_objs import Figure
from PIL import Image
import streamlit as st


def plot_box_amplitude_for_lambda(df: pd.DataFrame, lambda_n: str) -> Figure:
    return px.box(df, x=lambda_n, y="patient_state", color="cell_type")


def plot_pie_distribution_lymphocytes_for_patient(
    data: pd.DataFrame, patient_name: str
) -> Figure:
    df = data[data.patient_name == patient_name]
    df = (
        df[["cell_type", "patient_state"]]
        .groupby(by=["cell_type"], as_index=False)
        .count()
    )
    return px.pie(df, names="cell_type", values="patient_state")


def main_app():
    image = Image.open("logo.png")
    st.image(image)
    uploaded_file = st.file_uploader("Choose a CSV", type=["csv"])
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file, sep=";")
        st.write(dataframe)
        lambda_amplitude = st.selectbox(
            "Choose a wavelength number", [f"lambda_{i}" for i in range(1, 1000)]
        )
        st.plotly_chart(
            plot_box_amplitude_for_lambda(dataframe, lambda_n=lambda_amplitude)
        )
        patient_name = st.selectbox(
            "What is your patient name ?", dataframe.patient_name.unique()
        )
        st.write("You selected:", patient_name)
        st.plotly_chart(
            plot_pie_distribution_lymphocytes_for_patient(
                data=dataframe, patient_name=patient_name
            )
        )
        yes_or_no = st.radio("Do you want to see the spectrum ?", ("No", "Yes"))
        if yes_or_no == "Yes":
            cell_name = st.selectbox(
                "What is your cell name ?",
                dataframe[dataframe.patient_name == patient_name].cell_name.unique(),
            )
            spectrum_number = st.selectbox(
                "What is the spectrum number ?",
                dataframe[
                    (dataframe.patient_name == patient_name)
                    & (dataframe.cell_name == cell_name)
                ].spectre.unique(),
            )
            df_spectrum = dataframe[
                (dataframe.patient_name == patient_name)
                & (dataframe.cell_name == cell_name)
                & (dataframe.spectre == spectrum_number)
            ]
            df_spectrum = df_spectrum.drop(
                columns=[
                    "patient_name",
                    "cell_name",
                    "cell_type",
                    "patient_state",
                    "spectre",
                ]
            )
            df_spectrum = df_spectrum.transpose()
            st.plotly_chart(px.line(df_spectrum, y=df_spectrum.columns[0]))


if __name__ == "__main__":
    main_app()
