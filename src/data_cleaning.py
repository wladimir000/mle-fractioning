import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the King County housing dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Raw King County housing data.

    Returns
    -------
    pd.DataFrame
        Cleaned housing data.
    """

    df = df.copy()

    # Remove implausible bedroom observation
    df = df[df["bedrooms"] != 33]

    # Recalculate basement area
    df["sqft_basement"] = df["sqft_living"] - df["sqft_above"]

    # Handle missing values
    df["view"] = df["view"].fillna(0)
    df["waterfront"] = df["waterfront"].fillna(0)

    # Use renovation year if available,
    # otherwise use construction year
    renovation_year = df["yr_renovated"].fillna(0)

    df["last_known_change"] = renovation_year.where(
        renovation_year != 0,
        df["yr_built"]
    ).astype(int)

    # Original year columns are no longer needed
    df = df.drop(columns=["yr_renovated", "yr_built"])

    return df