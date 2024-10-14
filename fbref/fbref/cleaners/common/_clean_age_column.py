import polars as pl

def clean_age_column(df: pl.DataFrame) -> pl.DataFrame:
    """Cleans age column

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        pl.DataFrame: fbref dataframe with cleaned age column
    """
    return df.with_columns(
        pl.col("age").str.split("-").list.first().alias("age")
    )
