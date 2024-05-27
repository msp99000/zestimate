# Zestimate

Zestimate is a data-driven web application that utilizes data from Zillow to forecast and predict the Zillow Home Value Index (ZHVI) and Zillow Observed Rent Index (ZORI). The application is hosted at [zestimate.streamlit.app](https://zestimate.streamlit.app).

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [File Structure](#file-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Modeling](#modeling)
- [Contributing](#contributing)
- [License](#license)

## Overview

Zestimate leverages historical real estate data from Zillow to provide accurate and insightful predictions for home values and rent prices. This project involves data preprocessing, exploratory data analysis, and machine learning model development to generate these forecasts.

## Features

- **Data Preprocessing**: Clean and prepare Zillow data for analysis.
- **Exploratory Data Analysis (EDA)**: Visualize and understand the data trends and patterns.
- **Machine Learning Models**: Implement and train models to predict ZHVI and ZORI.
- **Web Application**: Interactive web interface to display predictions and insights.

## File Structure

```
Zestimate/
├── data/
│   ├── zhvi.pkl
│   ├── zhvi.xlsx
│   ├── zhvi_condo.csv
│   ├── zhvi_one_bedroom.csv
│   ├── zhvi_single_family.csv
│   ├── zhvi_three_bedroom.csv
│   ├── zhvi_two_bedroom.csv
│   ├── zori.pkl
│   ├── zori.xlsx
│   ├── zori_multi_family.csv
│   ├── zori_single_family.csv
├── models/
│   ├── lgbm.pkl
│   ├── xgb.pkl
├── notebooks/
│   ├── modeling.ipynb
│   ├── preprocessing.ipynb
│   ├── statistics.ipynb
├── .gitignore
├── main.py
├── README.md
```

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:

   ```sh
   git clone https://github.com/msp99000/zestimate.git
   cd zestimate
   ```

2. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

3. **Install Git LFS and pull large files**:
   ```sh
   git lfs install
   git lfs pull
   ```

## Usage

To run the web application locally, execute:

```sh
streamlit run main.py
```

Navigate to `http://localhost:8501` in your web browser to view the application.

## Data

The project uses various datasets from Zillow, including:

- **ZHVI Data**: Historical home value indices for different property types and regions.
- **ZORI Data**: Historical rent price indices for different property types and regions.

Data files are stored in the `data/` directory. Processed data is saved as `.pkl` files for efficient loading.

## Modeling

The project includes several machine learning models to predict ZHVI and ZORI:

- **LightGBM Model**: Stored in `models/lgbm.pkl`
- **XGBoost Model**: Stored in `models/xgb.pkl`

Model training and evaluation notebooks are located in the `notebooks/` directory.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
