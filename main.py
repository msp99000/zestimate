import streamlit as st
from styles import streamlit_style
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu
from texts import description, landing_content
from sidebar import sidebar_content

streamlit_style()

def main():

    sidebar_content()

    # Horizontal Menu
    selected = option_menu(None, ["Home", "Statistics", "ZHVI", 'ZORI'], 
                            icons=['house', 'graph-up-arrow', "house-up", 'house-up-fill'], 
                            menu_icon="cast", default_index=0, orientation="horizontal")
    
    if selected == 'Statistics':
        switch_page('Statistics')
    
    if selected == 'ZHVI':
        switch_page('ZHVI')
    
    if selected == 'ZORI':
        switch_page('ZORI')

    st.subheader("")

    # App Logo
    st.write("")
    a, b, c = st.columns([1, 3, 1])

    with b:
        st.image("images/transparent_logo.png")


    # Add header
    st.subheader("")
    st.title("Welcome to Zestimate")

    st.write(description)
    st.write("")

    landing_content()

if __name__ == "__main__":
    main()
