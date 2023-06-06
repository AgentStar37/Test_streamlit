import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

#|----------------------------------------------------------------------------------------------------|#

flight_hight_data={
    "Altitude (en mètres)":[0,50,130,200,250,267,276,258,300]
}

graph_height=pd.DataFrame(flight_hight_data,index=["0mn","1mn","2mn","3mn","4mn","5mn","6mn","7mn","8mn"])



st.title('Voici votre compte rendu de vol')

st.subheader("Voici le graphique de votre altitude au cours de votre vol")

st.area_chart(graph_height)