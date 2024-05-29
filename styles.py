import streamlit as st

""" ---- HIDE STREAMLIT STYLE ---- """

def streamlit_style():

    st.set_page_config(
        initial_sidebar_state="collapsed",
        layout="centered",
        page_icon="images/logo.png",
        page_title="Zestimate",
    )

    st.markdown(
        "<style> div.block-container{padding-top:0rem;} </style>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
                    <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        header {visibility: hidden;}
                    </style>
        """,
        unsafe_allow_html=True,
    )
