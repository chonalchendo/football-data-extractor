import polars as pl


def wages_rename_cols(df: pl.DataFrame) -> pl.DataFrame:
    rename_cols = {"pos": "position"}
    return df.rename(rename_cols)
