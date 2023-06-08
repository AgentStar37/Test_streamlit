import streamlit as st

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

st.title("A propos de cette application")

st.write("Cette application a été réalisée au cours d'un stage par un étudiant à Polytech Tours")

for i in range(8):
    st.text("")

st.divider()

st.write("Etes vous satisfait de l'application ?")
note = st.slider("Donnez une note !",0,5)
st.write(f"Vous avez donné une note de **{note}** à l'application. Merci de votre retour !")
st.divider()