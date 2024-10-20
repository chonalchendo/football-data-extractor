import polars as pl


def rename_keeper_cols(df: pl.DataFrame) -> pl.DataFrame:
    """Renames keeper stats columns

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        pl.DataFrame: fbref dataframe with renamed columns
    """
    rename_cols = {
        "ga": "goals_against",
        "ga90": "ga_per_90",
        "90s": "ninety_mins_played",
        "sota": "shots_on_target_against",
        "w": "wins",
        "d": "draws",
        "l": "losses",
        "cs": "clean_sheets",
        "cs_pct": "clean_sheet_pct",
        "pkatt": "penalties_faced",
        "pka": "penalties_allowed",
        "pksv": "penalties_saved",
        "pkm": "penalties_missed",
        "save_pct_1": "penalty_save_pct",
    }
    df = df.rename(rename_cols)
    return df
