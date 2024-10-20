import polars as pl


def rename_keeper_adv_cols(df: pl.DataFrame) -> pl.DataFrame:
    """Renames advanced keeper stats columns

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        pl.DataFrame: fbref dataframe with renamed columns
    """
    rename_cols = {
        "pka": "penalties_allowed",
        "fk": "free_kick_goals_allowed",
        "ck": "corner_goals_allowed",
        "90s": "ninety_mins_played",
        "og": "own_goals",
        "psxg": "post_shot_xg",
        "psxg_sot": "post_shot_xg_on_target",
        "psxg_": "post_shot_xg_minus_ga",
        "_90": "post_shot_xg_minus_ga_per_90",
        "cmp": "passes_completed_plus_40_yards",
        "att": "passes_attempted_plus_40_yards",
        "cmp_pct": "passes_pct_plus_40_yards",
        "att_gk_": "total_passes_attempted",
        "thr": "throws_attempted",
        "avglen": "avg_pass_length",
        "att_1": "goal_kicks_attempted",
        "launch_pct_1": "goal_kick_launch_pct",
        "avglen_1": "avg_goal_kick_length",
        "opp": "crosses_faced",
        "stp": "crosses_stopped",
        "stp_pct": "crosses_stopped_pct",
        "_opa": "defensive_actions_outside_penalty_area",
        "_opa_90": "defensive_opa_per_90",
        "avgdist": "avg_defensive_action_distance",
    }
    df = df.rename(rename_cols)
    return df
