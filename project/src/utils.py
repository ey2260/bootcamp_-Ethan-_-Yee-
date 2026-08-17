import pandas as pd
import sys
sys.path.append("..")

from src.utils import clean_columns

def parse_dates(df: pd.DataFrame, date_column: str) -> pd.DataFrame:
    """
    Converts a specified column into datetime format.
    """
    df_copy = df.copy()
    df_copy[date_column] = pd.to_datetime(df_copy[date_column])
    return df_copy
    
from src.utils import parse_dates


df_cleaned = parse_dates(df_cleaned, "date_column_name")