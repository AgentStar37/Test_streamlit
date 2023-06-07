import streamlit as st


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