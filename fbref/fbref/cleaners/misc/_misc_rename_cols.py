import polars as pl


def misc_rename_cols(df: pl.DataFrame) -> pl.DataFrame:
    """Renames miscellaneous stats columns

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        pl.DataFrame: fbref dataframe with renamed columns
    """
    rename_cols = {
        "90s": "ninety_mins_played",
        "crdy": "yellow_cards",
        "crdr": "red_cards",
        "2crdy": "second_yellow_cards",
        "fls": "fouls",
        "fld": "fouls_drawn",
        "off": "offsides",
        "crs": "crosses",
        "int": "interceptions",
        "tklw": "tackles_won",
        "pkwon": "penalties_won",
        "pkcon": "penalties_conceded",
        "og": "own_goals",
        "recov": "ball_recoveries",
        "won": "aerials_won",
        "lost": "aerials_lost",
        "won_pct": "aerials_won_pct",
    }
    df = df.rename(rename_cols)
    return df
