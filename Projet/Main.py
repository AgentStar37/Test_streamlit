import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

#|----------------------------------------------------------------------------------------------------|#
dataframe_map = pd.DataFrame(
    [(47.34050402250203, 0.9448078263737373),(47.33902784890322, 0.9509856106392972),(47.33646857391484, 0.9708983302756432),(47.341060161941044, 0.9842577463845583),(47.35279258589838, 1.0089945462637762),(47.36129097830923, 0.9895584892158192),(47.36906999659535, 0.9579307236559622),(47.373018905301414, 0.9098706553191963)],
    columns=["lat","lon"]
)

flight_hight_data={
    "Altitude (en mètres)":[0,50,130,200,250,267,276,258,300]
}
dataframe_height=pd.DataFrame(flight_hight_data,index=["0mn","1mn","2mn","3mn","4mn","5mn","6mn","7mn","8mn"])

flight_speed_data={
    "Vitesse (en km/h)":[0,80,112,150,175,180,177,156,192]
}
dataframe_speed=pd.DataFrame(flight_speed_data,index=["0mn","1mn","2mn","3mn","4mn","5mn","6mn","7mn","8mn"])
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
            content: "Menu des pages de l'appli";
            margin-left: 20px;
            margin-top: 20px;
            font-size: 20px;
            position: relative;
            top: 70px;
        }
    </style>
    """,
    unsafe_allow_html=True,
    )

st.sidebar.divider()
st.sidebar.divider()

st.title('Votre compte rendu de vol')

st.map(dataframe_map)

st.divider()

st.subheader("Voici le graphique de votre altitude au cours du vol")
st.area_chart(dataframe_height)

st.divider()

st.subheader("Voici le graphique de votre vitesse au cours du vol")
st.line_chart(dataframe_speed)
