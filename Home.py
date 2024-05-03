import streamlit as st
from styles import streamlit_style
from streamlit_extras.switch_page_button import switch_page

streamlit_style()

# App Logo
st.image("logo.png")

# Add header
st.title("Zestimate - Forecasting Property Growth")

# Add description
description = """
Welcome to Zestimate – your ultimate destination for accurate housing predictions. Zestimate is a cutting-edge project designed to forecast the Zillow Home Value Index (ZHVI) and Zillow Home Value Forecast (ZHVF) using advanced machine learning techniques on comprehensive housing data.

At Zestimate, we understand the importance of making informed decisions in the dynamic real estate market. Whether you are a homeowner, real estate investor, or industry professional, our platform provides invaluable insights to help you navigate the ever-changing landscape of property values.

Our approach leverages state-of-the-art time series analysis and predictive modeling to deliver precise forecasts of ZHVI and ZHVF based on a rich set of features, including historical property data, economic indicators, and local market trends. By analyzing vast amounts of data, we identify patterns and trends that enable us to anticipate future changes in home values with unparalleled accuracy.

With Zestimate, you can gain a competitive edge in the real estate market. Our intuitive platform offers easy access to detailed forecasts, customizable reports, and interactive visualizations, empowering you to make strategic decisions confidently. Whether you're buying, selling, or investing in real estate, Zestimate equips you with the insights you need to succeed.

Join thousands of users who trust Zestimate for their real estate forecasting needs. Start exploring our platform today and unlock the power of predictive analytics to shape your future in real estate.

Unlock Tomorrow's Home Values with Zestimate – Where Insight meets Innovation.
"""

st.write(description)
st.header(" ")


def main():

    depression, anxiety, stress = st.columns(3)

    # Add call buttons to navigate pages
    # with depression:
    #     dep_btn = st.button("Do you feel Depressed?")
    #     if dep_btn:
    #         switch_page("Depression")
    #
    # with anxiety:
    #     anx_btn = st.button("Do you feel Anxiety?")
    #     if anx_btn:
    #         switch_page("Anxiety")
    #
    # with stress:
    #     stress_btn = st.button("Do you feel Stressed?")
    #     if stress_btn:
    #         switch_page("Stress")


if __name__ == "__main__":
    main()
