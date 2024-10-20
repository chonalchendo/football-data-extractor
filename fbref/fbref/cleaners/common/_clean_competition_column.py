import polars as pl


def clean_comp_column(df: pl.DataFrame) -> pl.DataFrame:
    """Cleans comp column

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        pl.DataFrame: fbref dataframe with cleaned comp column
    """
    return (
        df.with_columns(
            pl.col("comp").str.splitn(" ", 2).struct[-1].alias("clean_comps")
        )
        .drop("comp")
        .rename({"clean_comps": "comp"})
    )
