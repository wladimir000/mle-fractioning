import numpy as np
import pandas as pd


def dist(long, lat, ref_long, ref_lat):
    """
    Compute the approximate distance in kilometers
    between a location and a reference location.
    """
    delta_long = long - ref_long
    delta_lat = lat - ref_lat
    delta_long_corr = delta_long * np.cos(np.radians(ref_lat))

    return (
        ((delta_long_corr) ** 2 + delta_lat**2) ** (1 / 2)
        * 2
        * np.pi
        * 6378
        / 360
    )


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create the engineered features used in the
    King County housing notebook.
    """
    df = df.copy()

    # Price per square foot
    df["sqft_price"] = (
        df["price"] / (df["sqft_living"] + df["sqft_lot"])
    ).round(2)

    # Distance to the reference center
    df["delta_lat"] = np.absolute(47.62774 - df["lat"])
    df["delta_long"] = np.absolute(-122.24194 - df["long"])

    df["center_distance"] = (
        (
            (df["delta_long"] * np.cos(np.radians(47.6219))) ** 2
            + df["delta_lat"] ** 2
        )
        ** (1 / 2)
        * 2
        * np.pi
        * 6378
        / 360
    )

    # Waterfront houses serve as reference points
    water_list = df.query("waterfront == 1")

    water_distance = []

    for idx in df.index:
        ref_list = []

        for x, y in zip(water_list["long"], water_list["lat"]):
            ref_list.append(
                dist(
                    df.loc[idx, "long"],
                    df.loc[idx, "lat"],
                    x,
                    y,
                )
            )

        water_distance.append(min(ref_list))

    df["water_distance"] = water_distance

    return df
