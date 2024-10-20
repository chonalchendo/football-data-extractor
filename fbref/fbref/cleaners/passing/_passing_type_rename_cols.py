import polars as pl


def passing_type_rename_cols(df: pl.DataFrame) -> pl.DataFrame:
    """Renames passing types stats columns

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        pl.DataFrame: fbref dataframe with renamed columns
    """
    rename_cols = {
        "90s": "ninety_mins_played",
        "att": "passes_attempted",
        "live": "live_ball_passes",
        "dead": "dead_ball_passes",
        "fk": "free_kick_passes",
        "tb": "through_balls",
        "sw": "switches",
        "crs": "crosses",
        "ti": "throw_ins",
        "ck": "corner_kicks",
        "in": "inswinging_corners",
        "out": "outswinging_corners",
        "str": "straight_corners",
        "cmp": "passes_completed",
        "off": "passes_offside",
        "blocks": "passes_blocked",
    }
    df = df.rename(rename_cols)
    return df
