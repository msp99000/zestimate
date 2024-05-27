import streamlit as st
from styles import streamlit_style
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu
from sidebar import sidebar_content
from utils import data_loader, model_loader, pipeline_loader
import pandas as pd
from xgboost import XGBRegressor
import pickle

streamlit_style()

def main():

    sidebar_content()

    # Horizontal Menu
    selected = option_menu(None, ["Home", "Statistics", "ZHVI", 'ZORI'], 
                            icons=['house', 'graph-up-arrow', "house-up", 'house-up-fill'], 
                            menu_icon="cast", default_index=3, orientation="horizontal")
    
    if selected == 'Statistics':
        switch_page('Statistics')
    
    if selected == 'ZHVI':
        switch_page('ZHVI')
    
    if selected == 'Home':
        switch_page('main')

    df, _ = data_loader()
    lgbm, xgb = model_loader()
    pipeline = pipeline_loader()

    # Streamlit app
    def predict_zori(state, type, date):
        region = 'N/A'
        date_obj = pd.to_datetime(date)
        year = date_obj.year
        month = date_obj.month
        week = date_obj.isocalendar().week
        day = date_obj.day
        encoded_data = pipeline.transform([[region, state, type, year, month, week, day]])
        
        model = xgb
        
        prediction = model.predict(encoded_data)[0]
        return prediction

    st.write("")
    st.title('Zillow Housing ZORI Prediction')

    state = st.selectbox('State', df['State'].unique())
    type = st.selectbox('Type', df['Type'].unique())
    date = st.date_input('Date')

    if st.button('Predict'):
        predicted_zori = predict_zori(state, type, date)
        st.write(f'Predicted ZORI: ${predicted_zhvi:.2f}')

if __name__ == "__main__":
    main()
