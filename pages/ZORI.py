import streamlit as st
from styles import streamlit_style
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu
from sidebar import sidebar_content

streamlit_style()

def main():

    sidebar_content()

    # Horizontal Menu
    selected = option_menu(None, ["Home", "Statistics", "ZHVI", 'ZORI'], 
                            icons=['house', 'cloud-upload', "list-task", 'gear'], 
                            menu_icon="cast", default_index=3, orientation="horizontal")
    
    if selected == 'Statistics':
        switch_page('Statistics')
    
    if selected == 'ZHVI':
        switch_page('ZHVI')
    
    if selected == 'Home':
        switch_page('main')


if __name__ == "__main__":
    main()
