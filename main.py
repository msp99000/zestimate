import streamlit as st
from styles import streamlit_style
from streamlit_extras.switch_page_button import switch_page

streamlit_style()

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

# Add description
description = """
Zestimate is your ultimate destination for accurate housing predictions. Zestimate is a cutting-edge project designed to forecast the Zillow Home Value Index (ZHVI) and Zillow Home Value Forecast (ZHVF) using advanced machine learning techniques on comprehensive housing data.

At Zestimate, we understand the importance of making informed decisions in the dynamic real estate market. Whether you are a homeowner, real estate investor, or industry professional, our platform provides invaluable insights to help you navigate the ever-changing landscape of property values.

"""

st.write(description)
st.write("")


def main():

    zhvi, stats, zori = st.columns(3)

    # Add call buttons to navigate pages
    with zhvi:
        zhvi_btn = st.button("Predict ZHVI")
        if zhvi_btn:
            switch_page("ZHVI")

    with stats:
        stats_btn = st.button("Check Statistics")
        if stats_btn:
            switch_page("Statistics")

    with zori:
        zori_btn = st.button("Predict ZORI")
        if zori_btn:
            switch_page("ZORI")


if __name__ == "__main__":
    main()
