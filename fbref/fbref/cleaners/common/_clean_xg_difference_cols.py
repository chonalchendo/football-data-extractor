import polars as pl


def clean_xg_difference_cols(df: pl.DataFrame) -> pl.DataFrame:
    """Cleans xg difference columns

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        pl.DataFrame: fbref dataframe with cleaned xg difference columns
    """
    cols = [col for col in df.columns if "minus" in col]
    for col in cols:
        df[col] = df[col].str.replace("+", "")
    return df
