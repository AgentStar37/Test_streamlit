from random import choice
import pandas as pd
import streamlit as st

#|----------------------------------------------------------------------------------------------------|#
flight_temp_data={
    "Température (en °C)":[st.metric(value="22 °C"),st.metric(value="21 °C", delta="-1 °C"),st.metric(value="18 °C", delta="-3 °C"),st.metric(value="16 °C", delta="-2 °C"),st.metric(value="15 °C", delta="-1 °C"),st.metric(value="15 °C"),st.metric(value="14 °C", delta="-1 °C"),st.metric(value="12 °C", delta="-2 °C")]
}
dataframe_temp=pd.DataFrame(flight_temp_data,index=["0mn","1mn","2mn","3mn","4mn","5mn","6mn","7mn","8mn"])

avions=["tbm 900", "tbm 940","tbm 960"]
avion_random=choice(avions)
#|----------------------------------------------------------------------------------------------------|#

#--------------------------------------
st.set_page_config(
    page_title="Compte rendu de vol",
    page_icon="✈",
    )
#--------------------------------------

st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] {
            padding-top: 150px;
            background-position: 20px 20px;
        }
        [data-testid="stSidebarNav"]::before {
            content: "Menu";
            margin-left: 20px;
            margin-top: 20px;
            font-size: 40px;
            position: relative;
            top: 70px;
        }
    </style>
    """,
    unsafe_allow_html=True,
    )

st.sidebar.divider()

st.title("Conditions de vol:")

st.subheader(f"Vous pilotiez un **{avion_random}**")
st.image("Projet/pages/Assets/"+avion_random+".jpg")

st.divider()

st.subheader("Température à l'altitude de l'avion au cours du vol en degrés Celsius")
st.line_chart(dataframe_temp)