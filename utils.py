import pandas as pd
import pickle
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def data_loader():
    """
    Load ZHVI and ZORI data from pickle files.

    Returns:
        tuple: DataFrames containing ZHVI and ZORI data.
    """
    try:
        zhvi = pd.read_pickle("data/zhvi.pkl")
        zhvi = zhvi[zhvi['Date'] > '2020-12-31']
        zhvi = zhvi.set_index('Date')
        zhvi['Year'] = zhvi.index.year
        zhvi['Month'] = zhvi.index.month
        zhvi['Week'] = zhvi.index.isocalendar().week
        zhvi['Day'] = zhvi.index.day
        zhvi['Region'] = zhvi['Region'].str.split(',').str[0]
        logger.info("ZHVI data loaded successfully.")
    except FileNotFoundError:
        logger.error("ZHVI data file not found.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading ZHVI data: {e}")
        raise

    try:
        zori = pd.read_pickle("data/zori.pkl")
        zori = zori[zori['Date'] > '2020-12-31']
        zori = zori.set_index('Date')
        zori['Year'] = zori.index.year
        zori['Month'] = zori.index.month
        zori['Week'] = zori.index.isocalendar().week
        zori['Day'] = zori.index.day
        zori['Region'] = zori['Region'].str.split(',').str[0]
        logger.info("ZORI data loaded successfully.")
    except FileNotFoundError:
        logger.error("ZORI data file not found.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading ZORI data: {e}")
        raise

    return zhvi, zori

def model_loader():
    """
    Load machine learning models from pickle files.

    Returns:
        tuple: LightGBM and XGBoost models.
    """
    try:
        with open("models/lgbm_zhvi.pkl", 'rb') as f:
            lgbm_zhvi = pickle.load(f)
        logger.info("LightGBM model loaded successfully.")
    except FileNotFoundError:
        logger.error("LightGBM model file not found.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading the LightGBM model: {e}")
        raise

    try:
        with open("models/xgb_zhvi.pkl", 'rb') as f:
            xgb_zhvi = pickle.load(f)
        logger.info("XGBoost model loaded successfully.")
    except FileNotFoundError:
        logger.error("XGBoost model file not found.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading the XGBoost model: {e}")
        raise

    try:
        with open("models/gb_zhvi.pkl", 'rb') as f:
            gb_zhvi = pickle.load(f)
        logger.info("Gradient Boosting model loaded successfully.")
    except FileNotFoundError:
        logger.error("Gradient Boosting model file not found.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading the Gradient Boosting model: {e}")
        raise

    try:
        with open("models/catboost_zhvi.pkl", 'rb') as f:
            cb_zhvi = pickle.load(f)
        logger.info("CatBoost model loaded successfully.")
    except FileNotFoundError:
        logger.error("CatBoost model file not found.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading the CatBoost model: {e}")
        raise

    try:
        with open("models/lgbm_zori.pkl", 'rb') as f:
            lgbm_zori = pickle.load(f)
        logger.info("LightGBM model loaded successfully.")
    except FileNotFoundError:
        logger.error("LightGBM model file not found.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading the LightGBM model: {e}")
        raise

    try:
        with open("models/xgb_zori.pkl", 'rb') as f:
            xgb_zori = pickle.load(f)
        logger.info("XGBoost model loaded successfully.")
    except FileNotFoundError:
        logger.error("XGBoost model file not found.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading the XGBoost model: {e}")
        raise

    try:
        with open("models/gb_zori.pkl", 'rb') as f:
            gb_zori = pickle.load(f)
        logger.info("Gradient Boosting model loaded successfully.")
    except FileNotFoundError:
        logger.error("Gradient Boosting model file not found.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading the Gradient Boosting model: {e}")
        raise

    try:
        with open("models/catboost_zori.pkl", 'rb') as f:
            cb_zori = pickle.load(f)
        logger.info("CatBoost model loaded successfully.")
    except FileNotFoundError:
        logger.error("CatBoost model file not found.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading the CatBoost model: {e}")
        raise

    return lgbm_zhvi, xgb_zhvi, gb_zhvi, cb_zhvi, lgbm_zori, xgb_zori, gb_zori, cb_zori 

def pipeline_loader():
    """
    Load preprocessing pipeline from a pickle file.

    Returns:
        Pipeline: Preprocessing pipeline.
    """
    try:
        with open("models/pipeline.pkl", 'rb') as f:
            pipeline = pickle.load(f)
        logger.info("Pipeline loaded successfully.")
    except FileNotFoundError:
        logger.error("Pipeline file not found.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading the pipeline: {e}")
        raise

    return pipeline
