import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def fill_missing_median(df: pd.DataFrame, columns: list[str] = None) -> pd.DataFrame:
    df_clean = df.copy()
    if columns is None:
        columns = df_clean.select_dtypes(include=["number"]).columns

    for col in columns:
        if col in df_clean.columns:
            median_val = df_clean[col].median()
            df_clean[col] = df_clean[col].fillna(median_val)

    return df_clean


def drop_missing(df: pd.DataFrame, columns: list[str] = None, axis: int = 0) -> pd.DataFrame:
    df_clean = df.copy()

    if columns and axis == 0:
        return df_clean.dropna(subset=columns)

    return df_clean.dropna(axis=axis)


def normalize_data(df: pd.DataFrame, columns: list[str] = None) -> pd.DataFrame:
    df_clean = df.copy()

    if columns is None:
        columns = df_clean.select_dtypes(include=["number"]).columns

    scaler = MinMaxScaler()
    df_clean[columns] = scaler.fit_transform(df_clean[columns])

    return df_clean