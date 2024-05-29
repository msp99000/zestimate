import streamlit as st
from styles import streamlit_style
from streamlit_extras.switch_page_button import switch_page
from streamlit_option_menu import option_menu
from sidebar import sidebar_content
from utils import data_loader, model_loader, pipeline_loader
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor

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

    # Load Data
    _, df = data_loader()

    # Load Model
    _, _, lgbm_zori, _ = model_loader()

    # Streamlit app
    def predict_zori(region, type, date):

        date_obj = pd.to_datetime(date)
        input_data = pd.DataFrame({
            'Region': [region],
            'Type': [type],
            'Year': [date_obj.year],
            'Month': [date_obj.month],
            'Week': [date_obj.week],
            'Day': [date_obj.day]
        })

        # One-hot encode categorical features
        categorical_cols = ['Region', 'Type']
        numerical_cols = ['ZHVI']

        categorical_transformer = OneHotEncoder(handle_unknown='ignore')
        pipeline_zori = ColumnTransformer(transformers=[('cat', categorical_transformer, categorical_cols)], remainder='passthrough')

        X = pipeline_zori.fit_transform(df[categorical_cols + ['Year', 'Month', 'Week', 'Day']])

        encoded_data = pipeline_zori.transform(input_data)
        model = lgbm_zori
        prediction = model.predict(encoded_data)[0]
        
        return prediction

    st.write("")
    st.title('Zillow Housing ZORI Prediction  ⚡️')

    region = st.selectbox('Select Region', df['Region'].unique())
    type = st.selectbox('Select Type', df['Type'].unique())
    date = st.date_input('Select Date')

    st.write("")
    if st.button('Predict'):
        predicted_zori = predict_zori(region, type, date)
        st.write("")
        st.markdown(f"""
                        <div style="font-size:22px;">
                            The <strong>Zillow Observed Rent Index</strong> for a 
                            <strong>{type}</strong> in 
                            📍<strong>{region}</strong> on 
                            <strong>{date}</strong> comes out to be 
                            <strong>${predicted_zori:.2f}</strong> 💵
                        </div>
                    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
