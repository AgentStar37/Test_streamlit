import streamlit as st
import pandas as pd

#--------------------------------------
st.set_page_config(
    page_title="Compte rendu de vol",
    page_icon="🛩",
    )
#--------------------------------------

#|----------------------------------------------------------------------------------------------------|#
pays_nb_tbm_dict={
    "France":38,"USA":120,"Suisse":18,"Angleterre":22,"Espagne":21
}

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

st.title("A propos de cette application")

st.write("Cette application a été réalisée au cours d'un stage par un étudiant à Polytech Tours")

for i in range(8):
    st.text("")

countries = st.multiselect("Nombre de TBM achetés par pays",options=["France","USA","Suisse","Angleterre","Espagne"],default=["France","USA","Suisse","Angleterre","Espagne"])
nb_tbm_dict={
    "Ventes de TBM": pays_nb_tbm_dict[country] for country in countries
}
countries_dataframe=pd.DataFrame(pays_nb_tbm_dict,index=countries)
st.bar_chart(countries_dataframe)

st.divider()

st.write("Etes vous satisfait de l'application ?")
note = st.slider("Donnez une note !",0,5)
st.write(f"Vous avez donné une note de **{note}** à l'application. Merci de votre retour !")
st.divider()