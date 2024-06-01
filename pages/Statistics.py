import streamlit as st
from styles import streamlit_style
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu
from sidebar import sidebar_content
import plotly.express as px
import plotly.graph_objects as go
from plots import plot_zhvi, plot_zori

# Apply custom style
streamlit_style()

def main():
    # Display sidebar content
    sidebar_content()

    # Horizontal Menu
    selected = option_menu(
        None, 
        ["Home", "Statistics", "ZHVI", "ZORI"], 
        icons=['house', 'graph-up-arrow', "house-up", 'house-up-fill'], 
        menu_icon="cast", 
        default_index=1, 
        orientation="horizontal"
    )
    
    # Page navigation based on menu selection
    if selected == 'Home':
        switch_page('main')
    elif selected == 'ZHVI':
        switch_page('ZHVI')
    elif selected == 'ZORI':
        switch_page('ZORI')

    st.write("")
    st.subheader("Charts below show ZHVI/ZORI Statistics")
    st.write("")

    # Plot charts
    plot_zhvi()
    plot_zori()

if __name__ == "__main__":
    main()
