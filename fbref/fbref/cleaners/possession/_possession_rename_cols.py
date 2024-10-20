import polars as pl


def possession_rename_cols(df: pl.DataFrame) -> pl.DataFrame:
    """Renames possession stats columns

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        pl.DataFrame: fbref dataframe with renamed columns
    """
    rename_cols = {
        "90s": "ninety_mins_played",
        "def_pen": "def_pen_area_touches",
        "def_3rd": "def_third_touches",
        "mid_3rd": "mid_third_touches",
        "att_3rd": "att_third_touches",
        "att_pen": "att_pen_area_touches",
        "live": "live_ball_touches",
        "att": "take_ons_attempted",
        "succ": "take_ons_successful",
        "succ_pct": "take_on_succ_pct",
        "tkld": "take_ons_tackled",
        "tkld_pct": "take_on_tackled_pct",
        "totdist": "total_distance_carried",
        "prgdist": "progressive_carries_distance",
        "prgc": "progressive_carries",
        "1_3": "carries_into_final_third",
        "cpa": "carries_into_penalty_area",
        "mis": "miscontrols",
        "dis": "dispossessed",
        "rec": "passes_received",
        "prgr": "progressive_passes_received",
    }
    df = df.rename(rename_cols)
    return df
