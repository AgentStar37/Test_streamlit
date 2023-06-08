from random import choice
import pandas as pd
import streamlit as st

#--------------------------------------
st.set_page_config(
    page_title="Compte rendu de vol",
    page_icon="🛩",
    )
#--------------------------------------

#|----------------------------------------------------------------------------------------------------|#
temp_time_dict={
    "0mn":"22","1mn":"21","2mn":"18","3mn":"16","4mn":"15","5mn":"15","6mn":"14","7mn":"12","8mn":"12"
}
@st.cache_data
def choose_plane(planes):
    return choice(planes)

avions=["tbm 900", "tbm 940","tbm 960"]
avion_random=choose_plane(avions)
#|----------------------------------------------------------------------------------------------------|#



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

time_temp=st.select_slider(label="Selectionner le temps lors du vol",options=["0mn","1mn","2mn","3mn","4mn","5mn","6mn","7mn","8mn"])
st.metric(label="Température au niveau de l'avion à ce moment",value=str(temp_time_dict[time_temp])+" °C")