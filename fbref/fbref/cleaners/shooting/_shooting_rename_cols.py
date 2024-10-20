import polars as pl


def shooting_rename_cols(df: pl.DataFrame) -> pl.DataFrame:
    """Renames shooting stats columns

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        pl.DataFrame: fbref dataframe with renamed columns
    """
    rename_cols = {
        "90s": "ninety_mins_played",
        "gls": "goals",
        "sh": "shots",
        "sot": "shots_on_target",
        "sot_pct": "shots_on_target_pct",
        "sh_90": "shots_per_90",
        "sot_90": "shots_on_target_per_90",
        "g_sh": "goals_per_shot",
        "g_sot": "goals_per_shot_on_target",
        "dist": "avg_shot_distance",
        "fk": "free_kick_shots",
        "pk": "penalty_kicks",
        "pkatt": "penalty_kicks_attempted",
        "npxg": "non_penalty_xg",
        "npxg_sh": "non_penalty_xg_per_shot",
        "g_xg": "goals_minus_xg",
        "np_g_xg": "non_penalty_goals_minus_xg",
    }
    df = df.rename(rename_cols)
    return df
