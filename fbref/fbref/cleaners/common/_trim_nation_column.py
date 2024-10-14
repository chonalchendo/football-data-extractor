import polars as pl

def trim_nation_column(df: pl.DataFrame) -> pl.DataFrame:
    """Trim the nation column to only include the nation name.

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        pl.DataFrame: fbref dataframe with cleaned nation column
    """
    return df.with_columns(
        pl.col("nation").str.split(" ").list.get(-1)
    )
