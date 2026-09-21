import pandas as pd

from src.data_cleaning import clean_data
from src.feature_engineering import engineer_features


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Run the complete preprocessing pipeline.

    1. Data cleaning
    2. Feature engineering
    """

    df = clean_data(df)
    df = engineer_features(df)

    return df