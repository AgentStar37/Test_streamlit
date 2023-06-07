from random import choice
import pandas as pd
import streamlit as st

#--------------
st.set_page_config(
    page_title="Compte rendu de vol",
    page_icon="✈",
    )
#--------------

st.title("Conditions de vol:")


flight_temp_data={
    "Température (en °C)":[22,21,18,16,15,15,15,14,12]
}
dataframe_temp=pd.DataFrame(flight_temp_data,index=["0mn","1mn","2mn","3mn","4mn","5mn","6mn","7mn","8mn"])

avions=["tbm 900", "tbm 940","tbm 960"]
avion_random=choice(avions)
st.subheader(f"Vous pilotiez un **{avion_random}**")
st.image("Projet/pages/Assets/"+avion_random+".jpg")

st.divider()

st.subheader("Température à l'altitude de l'avion au cours du vol en degrés Celsius")
st.line_chart(dataframe_temp)