import polars as pl


def playing_time_rename_cols(df: pl.DataFrame) -> pl.DataFrame:
    """Renames playing time stats columns

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        pl.DataFrame: fbref dataframe with renamed columns
    """
    rename_cols = {
        "90s": "ninety_mins_played",
        "min": "mins_played",
        "mn_mp": "mins_per_match",
        "min_pct": "mins_played_pct",
        "mn_start": "mins_per_start",
        "compl": "complete_matches_played",
        "mn_sub": "mins_per_sub",
        "unsub": "unused_sub",
        "ppm": "points_per_match",
        "ong": "team_goals_while_on_pitch",
        "onga": "team_goals_conceded_while_on_pitch",
        "_": "goals_minus_conceded_while_on_pitch",
        "_90": "goals_minus_conceded_while_on_pitch_per_90",
        "on_off": "net_goals_on_minus_off_pitch_per_90",
        "onxg": "team_xg_while_on_pitch",
        "onxga": "team_xg_conceded_while_on_pitch",
        "xg_": "team_xg_minus_xga_while_on_pitch",
        "xg_90": "team_xg_minus_xga_while_on_pitch_per_90",
        "on_off_1": "net_xg_on_minus_off_pitch_per_90",
    }
    df = df.rename(rename_cols)
    return df
