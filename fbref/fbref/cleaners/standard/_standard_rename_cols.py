import polars as pl


def standard_rename_cols(df: pl.DataFrame) -> pl.DataFrame:
    """Renames standard stats columns

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        pl.DataFrame: fbref dataframe with renamed columns
    """
    rename_cols = {
        "90s": "ninety_mins_played",
        "gls": "goals",
        "ast": "assists",
        "g_a": "goals_assists",
        "g_pk": "non_penalty_goals",
        "pk": "penalty_kicks",
        "pkatt": "penalty_kicks_attempted",
        "crdy": "yellow_cards",
        "crdr": "red_cards",
        "npxg": "non_penalty_xg",
        "npxg_xag": "non_pen_xg_plus_xag",
        "prgc": "progressive_carries",
        "prgp": "progressive_passes",
        "prgr": "progressive_passes_received",
        "gls_1": "goals_per_90",
        "ast_1": "assists_per_90",
        "g_a_1": "goals_assists_per_90",
        "g_pk_1": "non_penalty_goals_per_90",
        "g_a_pk": "non_penalty_goals_assists_per_90",
        "xg_1": "xg_per_90",
        "xag_1": "xag_per_90",
        "xg_xag": "xg_plus_xag_per_90",
        "npxg_1": "non_penalty_xg_per_90",
        "npxg_xag_1": "non_penalty_xg_plus_xag_per_90",
    }
    df = df.rename(rename_cols)
    return df
