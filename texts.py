import streamlit as st

# App Description
description = """
Zestimate is your ultimate destination for accurate housing predictions. Zestimate is a cutting-edge project designed to forecast the Zillow Home Value Index (ZHVI) and Zillow Home Value Forecast (ZHVF) using advanced machine learning techniques on comprehensive housing data.

At Zestimate, we understand the importance of making informed decisions in the dynamic real estate market. Whether you are a homeowner, real estate investor, or industry professional, our platform provides invaluable insights to help you navigate the ever-changing landscape of property values.

"""


def landing_content():

    st.header("Revolutionizing Real Estate Forecasting")

    st.write("Zestimate is your ultimate tool for predicting home values and rental prices with unparalleled accuracy. Leveraging comprehensive data from Zillow, our state-of-the-art machine learning models provide detailed insights and forecasts for the Zillow Home Value Index (ZHVI) and Zillow Observed Rent Index (ZORI).")

    st.image("images/realestate.jpg")

    st.header("Why Choose Zestimate?")

    st.subheader("Accurate Predictions")
    st.write("Harness the power of advanced algorithms and extensive datasets to get precise forecasts for property values and rental prices. Our models are trained on years of historical data, ensuring reliability and accuracy.")

    st.subheader("Comprehensive Data")
    st.write("Zestimate utilizes a wide range of data points, including regional and property-specific indices, to deliver nuanced and detailed predictions. Access data for various property types, including single-family homes, condos, and more.")

    st.subheader("User-Friendly Interface")
    st.write("Our intuitive web application, powered by Streamlit, provides an interactive and easy-to-navigate platform for exploring predictions and insights. Simply enter the relevant data, and let Zestimate do the rest.")

    st.subheader("Interactive Visualizations")
    st.write("Gain deeper insights through interactive charts and graphs. Visualize trends, compare different regions, and understand the factors driving market changes.")

    st.header("Features")

    st.subheader("Advanced Machine Learning Models")
    st.write("Zestimate employs cutting-edge machine learning techniques, including LightGBM and XGBoost, to ensure high prediction accuracy.")

    st.subheader("Customizable Forecasts")
    st.write("Tailor predictions based on specific criteria such as location, property type, and time frame. Get forecasts that matter to you.")

    st.subheader("Real-Time Updates")
    st.write("Stay up-to-date with real-time data integration. Zestimate continuously updates its predictions as new data becomes available.")

    st.subheader("Secure and Reliable")
    st.write("Your data is safe with us. Zestimate follows industry-standard security practices to ensure your information is protected.")

    st.markdown(''' ## How It Works

    1. **Data Collection**: We gather extensive historical data from Zillow, covering various property types and regions.
    2. **Data Processing**: Our robust preprocessing pipeline cleans and organizes the data for optimal analysis.
    3. **Model Training**: Using advanced machine learning algorithms, we train models to predict ZHVI and ZORI accurately.
    4. **Prediction and Visualization**: Access the predictions through our user-friendly web app and explore the data through interactive visualizations.

    ## Testimonials

    > "Zestimate has completely transformed the way we approach real estate investments. The accuracy and detail of the predictions are unmatched." - Jane Doe, Real Estate Investor

    > "As a property manager, Zestimate's insights have been invaluable in setting competitive rental prices and understanding market trends." - John Smith, Property Manager

    ## Get Started Today

    Experience the future of real estate forecasting with Zestimate. Whether you're a real estate investor, property manager, or simply curious about market trends, Zestimate provides the insights you need.

    [Sign Up Now](https://zestimate.streamlit.app/signup) and start exploring the power of accurate real estate predictions.

    ## Contact Us

    Have questions or need support? Our team is here to help. [Contact us](https://zestimate.streamlit.app/contact) and we'll get back to you as soon as possible.''')

