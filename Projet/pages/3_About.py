import streamlit as st

st.title("A propos de cette application")

st.write("Cette application a été réalisée au cours d'un stage par un étudiant à Polytech Tours")

for i in range(8):
    st.text("")

st.divider()

def note_given(note):
    st.write(f"Vous avez donné une note de **{note}** à l'application. Merci de votre retour !")

st.write("Etes vous satisfait de l'application ?")
note = st.slider("Donnez une note !",0,5, on_change=note_given())

st.divider()