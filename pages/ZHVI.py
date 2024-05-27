import streamlit as st
from styles import streamlit_style
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu

streamlit_style()

def main():

    # Horizontal Menu
    selected = option_menu(None, ["Home", "Statistics", "ZHVI", 'ZORI'], 
                            icons=['house', 'cloud-upload', "list-task", 'gear'], 
                            menu_icon="cast", default_index=2, orientation="horizontal")
    
    if selected == 'Statistics':
        switch_page('Statistics')
    
    if selected == 'Home':
        switch_page('main')
    
    if selected == 'ZORI':
        switch_page('ZORI')


if __name__ == "__main__":
    main()
