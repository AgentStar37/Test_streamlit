from random import choice
import streamlit as st

st.title("Conditions de vol:")

avions=["tbm 900", "tbm 940","tbm 960"]
avion_random=choice(avions)
st.write(f"Vous pilotiez un **{avion_random}**")
st.image("Projet/pages/Assets/"+avion_random+".jpg")