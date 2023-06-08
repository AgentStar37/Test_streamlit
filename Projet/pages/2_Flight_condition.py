from random import choice
import pandas as pd
import streamlit as st

#|----------------------------------------------------------------------------------------------------|#
temp_time_dict={
    "0mn":st.metric(value="22 °C"),"1mn":st.metric(value="21 °C", delta="-1 °C"),"2mn":st.metric(value="18 °C", delta="-3 °C"),"3mn":st.metric(value="16 °C", delta="-2 °C"),"4mn":st.metric(value="15 °C", delta="-1 °C"),"5mn":st.metric(value="15 °C"),"6mn":st.metric(value="14 °C", delta="-1 °C"),"7mn":st.metric(value="12 °C", delta="-2 °C"),"8mn":st.metric(value="12 °C")
}

avions=["tbm 900", "tbm 940","tbm 960"]
avion_random=choice(avions)
#|----------------------------------------------------------------------------------------------------|#

#--------------------------------------
st.set_page_config(
    page_title="Compte rendu de vol",
    page_icon="🛩",
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

time_temp=st.slider(label="Selectionner le temps lors du vol",options=["0mn","1mn","2mn","3mn","4mn","5mn","6mn","7mn","8mn"])
st.write(temp_time_dict[time_temp])