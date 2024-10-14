import polars as pl
import re

def clean_column_names(df: pl.DataFrame) -> pl.DataFrame:
    """Cleans column names

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        pl.DataFrame: fbref dataframe with cleaned column names
    """
    def clean_name(name: str) -> str:
        return re.sub(r"[^a-zA-Z0-9]+", "_", name.replace("%", "_pct")).lower()
    
    new_names = {col: clean_name(col) for col in df.columns}
    return df.rename(new_names)
