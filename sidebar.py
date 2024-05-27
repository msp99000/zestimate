import streamlit as st


def sidebar_content():

    st.sidebar.title("")
    _, x, _ = st.sidebar.columns([0.2, 0.6, 0.2])
    with x:
        st.sidebar.image("images/transparent_logo.png")

    st.sidebar.title("")
    st.sidebar.markdown('''
        <h1 style='text-align: center;'>Welcome to Zestimate !</h1>''',
         unsafe_allow_html=True)