import polars as pl


def gca_rename_cols(df: pl.DataFrame) -> pl.DataFrame:
    """Renames goal contributing actions stats columns

    Args:
        df (pl.DataFrame): fbref dataframe

    Returns:
        pl.DataFrame: fbref dataframe with renamed columns
    """
    rename_cols = {
        "sca": "shot_creating_actions",
        "90s": "ninety_mins_played",
        "sca90": "sca_per_90",
        "passlive": "pass_live_sca",
        "passdead": "pass_dead_sca",
        "to": "take_on_sca",
        "sh": "shot_sca",
        "fld": "foul_drawn_sca",
        "def": "defensive_action_sca",
        "gca": "goal_creating_actions",
        "gca90": "gca_per_90",
        "passlive_1": "pass_live_gca",
        "passdead_1": "pass_dead_gca",
        "to_1": "take_on_gca",
        "sh_1": "shot_gca",
        "fld_1": "foul_drawn_gca",
        "def_1": "defensive_action_gca",
    }
    return df.rename(rename_cols)
