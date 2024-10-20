import polars as pl


def passing_rename_cols(df: pl.DataFrame) -> pl.DataFrame:
    """Renames passing stats columns

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        ppl.DataFrame: fbref dataframe with renamed columns
    """
    rename_cols = {
        "90s": "ninety_mins_played",
        "cmp": "passes_completed",
        "att": "passes_attempted",
        "cmp_pct": "pass_completion_pct",
        "totdist": "total_pass_distance",
        "prgdist": "progressive_pass_distance",
        "cmp_1": "short_passes_completed",
        "att_1": "short_passes_attempted",
        "cmp_pct_1": "short_pass_completion_pct",
        "cmp_2": "medium_passes_completed",
        "att_2": "medium_passes_attempted",
        "cmp_pct_2": "medium_pass_completion_pct",
        "cmp_3": "long_passes_completed",
        "att_3": "long_passes_attempted",
        "cmp_pct_3": "long_pass_completion_pct",
        "ast": "assists",
        "a_xag": "assists_minus_xag",
        "kp": "key_passes",
        "1_3": "passes_into_final_third",
        "ppa": "passes_into_penalty_area",
        "crspa": "crosses_into_penalty_area",
        "prgp": "progressive_passes",
    }

    df = df.rename(rename_cols)
    return df
