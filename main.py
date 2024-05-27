import streamlit as st
from styles import streamlit_style
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu
from texts import description

streamlit_style()

def main():

    # Horizontal Menu
    selected = option_menu(None, ["Home", "Statistics", "ZHVI", 'ZORI'], 
                            icons=['house', 'cloud-upload', "list-task", 'gear'], 
                            menu_icon="cast", default_index=0, orientation="horizontal")
    
    if selected == 'Statistics':
        switch_page('Statistics')
    
    if selected == 'ZHVI':
        switch_page('ZHVI')
    
    if selected == 'ZORI':
        switch_page('ZORI')

    # App Logo
    st.write("")
    a, b, c = st.columns([1, 3, 1])

    with b:
        st.image("images/transparent_logo.png")

    # Add header
    st.write("")
    st.markdown(
        "<h1 style='text-align: center; color: #47c099;'>Welcome to Zestimate !</h1>",
        unsafe_allow_html=True,
    )
    st.write("")

    st.write(description)
    st.write("")

if __name__ == "__main__":
    main()
