from random import choice
import pandas as pd
import streamlit as st

st.title("Conditions de vol:")


flight_temp_data={
    "Vitesse (en km/h)":["22°C","21°C","18°C","16°C","15°C","15°C","15°C","14°C","12°C"]
}
dataframe_temp=pd.DataFrame(flight_temp_data,index=["0mn","1mn","2mn","3mn","4mn","5mn","6mn","7mn","8mn"])

avions=["tbm 900", "tbm 940","tbm 960"]
avion_random=choice(avions)
st.write(f"Vous pilotiez un **{avion_random}**")
st.image("Projet/pages/Assets/"+avion_random+".jpg")

st.subheader("Température à l'altitude de l'avion au cours du vol")
st.line_chart(dataframe_temp)