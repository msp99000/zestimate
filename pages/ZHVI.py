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
                            menu_icon="cast", default_index=2, orientation="horizontal")
    
    if selected == 'Statistics':
        switch_page('Statistics')
    
    if selected == 'Home':
        switch_page('main')
    
    if selected == 'ZORI':
        switch_page('ZORI')

    # Load Data
    df, _ = data_loader()

    # Load Model
    lgbm_zhiv, _, _, _ = model_loader()

    # Streamlit app
    def predict_zhvi(region, type, date):
        
        date_obj = pd.to_datetime(date)
        input_data = pd.DataFrame({
            'Region': [state],
            'Type': [type],
            'Year': [date_obj.year],
            'Month': [date_obj.month],
            'Week': [date_obj.week],
            'Day': [date_obj.day]
        })

        encoded_data = pipeline.transform([[region, state, type, year, month, week, day]])
        model = xgb
        prediction = model.predict(encoded_data)[0]
        return prediction

    st.write("")
    st.title('Zillow Housing ZHVI Prediction')

    state = st.selectbox('State', df['State'].unique())
    type = st.selectbox('Type', df['Type'].unique())
    date = st.date_input('Date')

    if st.button('Predict'):
        predicted_zhvi = predict_zhvi(state, type, date)
        st.write(f'Predicted ZHVI: ${predicted_zhvi:.2f}')

if __name__ == "__main__":
    main()
