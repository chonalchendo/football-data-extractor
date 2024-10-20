import polars as pl


def drop_matches_column(df: pl.DataFrame) -> pl.DataFrame:
    """Drops columns from dataframe

    Args:
        df (pd.DataFrame): fbref dataframe

    Returns:
        pd.DataFrame: fbref dataframe with dropped columns
    """
    return df.drop("matches")
