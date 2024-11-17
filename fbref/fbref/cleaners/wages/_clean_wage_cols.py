import polars as pl


def clean_wage_cols(df: pl.DataFrame, comp: str) -> pl.DataFrame:

    for wage in ["annual_wages", "weekly_wages"]:
        if comp != "Premier-League":
            df = df.with_columns(
                pl.col(wage)
                .str.split(" (")
                .list.get(-1)
                .replace("€ ", "")
                .replace(",", "")
            )

        else:
            df = df.with_columns(
                pl.col(wage)
                .str.split(" (")
                .list.get(-1)
                .str.split(", ")
                .list.get(0)
                .replace("€ ", "")
                .replace(",", "")
            )

        df = df.rename({wage: f"{wage}_euros"})
    return df
