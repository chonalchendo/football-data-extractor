import polars as pl


def remove_row_headers(df: pl.DataFrame) -> pl.DataFrame:
    """
    Remove the row headers from the DataFrame.

    Args:
        df (pl.DataFrame): The DataFrame to remove the row headers from.

    Returns:
        pl.DataFrame: The DataFrame without the row headers.
    """ 
    return df.filter((pl.arange(0, df.height) - 25) % 26 != 0)




