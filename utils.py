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
        logger.info("ZHVI data loaded successfully.")
    except FileNotFoundError:
        logger.error("ZHVI data file not found.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading ZHVI data: {e}")
        raise

    try:
        zori = pd.read_pickle("data/zori.pkl")
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
        with open("models/lgbm.pkl", 'rb') as f:
            lgbm = pickle.load(f)
        logger.info("LightGBM model loaded successfully.")
    except FileNotFoundError:
        logger.error("LightGBM model file not found.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading the LightGBM model: {e}")
        raise

    try:
        with open("models/xgb.pkl", 'rb') as f:
            xgb = pickle.load(f)
        logger.info("XGBoost model loaded successfully.")
    except FileNotFoundError:
        logger.error("XGBoost model file not found.")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading the XGBoost model: {e}")
        raise

    return lgbm, xgb

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
