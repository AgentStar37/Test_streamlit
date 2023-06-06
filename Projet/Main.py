import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

#|----------------------------------------------------------------------------------------------------|#

flight_hight_data={
    "Altitude (en mètres)":[0,50,130,200,250,267,276,258,300]
}
graph_height=pd.DataFrame(flight_hight_data,index=["0mn","1mn","2mn","3mn","4mn","5mn","6mn","7mn","8mn"])

flight_speed_data={
    "Vitesse (en km/h)":[0,80,112,150,175,180,177,156,192]
}
graph_speed=pd.DataFrame(flight_speed_data,index=["0mn","1mn","2mn","3mn","4mn","5mn","6mn","7mn","8mn"])


st.title('Votre compte rendu de vol')

st.subheader("Voici le graphique de votre altitude au cours du vol")
st.area_chart(graph_height)

st.subheader("Voici le graphique de votre vitesse au cours du vol")
st.line_chart(graph_speed)