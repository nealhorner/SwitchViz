import pandas as pd
from app import cache
import requests


def find_current_url():
    options = [
        "https://raw.githubusercontent.com/ThereminGoat/switch-scores/refs/heads/master/1-Composite%20Overall%20Total%20Score%20Sheet.csv",
        "https://raw.githubusercontent.com/ThereminGoat/switch-scores/refs/heads/master/1-Composite%20Overall%20Total%20Score%20Sheet%20.csv",
    ]

    # check if url does not return 404
    for url in options:
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            continue
        if response.status_code == 200:
            return url


@cache.memoize(timeout=600)
def get_data():
    df = pd.read_csv(
        find_current_url(),
        skiprows=4,
        usecols=[
            "Rank",
            "Switch Name",
            "Manufacturer",
            "Type",
            "Push Feel",
            "Wobble",
            "Sound",
            "Context",
            "Other",
            "Timeless\nTotal",
            "Time Wtd. \nTotal",
        ],
    )
    df.rename(
        columns={
            "Timeless\nTotal": "Timeless Total",
            "Time Wtd. \nTotal": "Time Wtd. Total",
            "Rank": "Rank Within Type",
        },
        inplace=True,
    )
    df = df[pd.to_numeric(df["Rank Within Type"], errors="coerce").notna()]

    # Convert data types after clean up
    df["Rank Within Type"] = df["Rank Within Type"].astype(int)
    df["Push Feel"] = df["Push Feel"].astype(int)
    df["Wobble"] = df["Wobble"].astype(int)
    df["Sound"] = df["Sound"].astype(int)
    df["Context"] = df["Context"].astype(int)
    df["Other"] = df["Other"].astype(int)
    df["Timeless Total"] = df["Timeless Total"].astype(int)
    df["Time Wtd. Total"] = df["Time Wtd. Total"].astype(float)

    # Dense rank the data from Time Wtd. Total
    df["Rank"] = df["Time Wtd. Total"].rank(method="dense", ascending=False).astype(int)

    # Reorder the columns
    df = df[
        [
            "Rank",
            # "Rank Within Type",
            "Switch Name",
            "Manufacturer",
            "Type",
            "Push Feel",
            "Wobble",
            "Sound",
            "Context",
            "Other",
            "Timeless Total",
            "Time Wtd. Total",
        ]
    ]

    return df


@cache.memoize(timeout=600)
def get_switch_names():
    return sorted(get_data()["Switch Name"].unique())


@cache.memoize(timeout=600)
def get_switch_manufacturers():
    return sorted(get_data()["Manufacturer"].unique())


@cache.memoize(timeout=600)
def get_switch_types():
    return sorted(get_data()["Type"].unique())
