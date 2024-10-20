import polars as pl


def defense_rename_cols(df: pl.DataFrame) -> pl.DataFrame:
    """Renames defensive stats columns

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        pl.DataFrame: fbref dataframe with renamed columns
    """
    rename_cols = {
        "pos": "position",
        "90s": "ninety_mins_played",
        "tkl": "tackles",
        "tklw": "tackles_won",
        "def_3rd": "def_third_tackles",
        "mid_3rd": "mid_third_tackles",
        "att_3rd": "att_third_tackles",
        "tkl_1": "dribblers_tackled",
        "att": "dribblers_challenged",
        "tkl_pct": "tackle_pct",
        "lost": "challenges_lost",
        "sh": "shots_blocked",
        "pass": "passes_blocked",
        "int": "interceptions",
        "tkl_int": "tackles_interceptions",
        "clr": "clearances",
        "err": "errors",
    }
    return df.rename(mapping=rename_cols)
