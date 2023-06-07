import streamlit as st

#--------------------------------------
st.set_page_config(
    page_title="Compte rendu de vol",
    page_icon="✈",
    )
#--------------------------------------

from ..fonctions import *

st.title("A propos de cette application")

st.write("Cette application a été réalisée au cours d'un stage par un étudiant à Polytech Tours")

for i in range(8):
    st.text("")

st.divider()

st.write("Etes vous satisfait de l'application ?")
note = st.slider("Donnez une note !",0,5)
st.write(f"Vous avez donné une note de **{note}** à l'application. Merci de votre retour !")
st.divider()