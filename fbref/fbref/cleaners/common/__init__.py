from ._clean_age_column import clean_age_column
from ._clean_column_names import clean_column_names
from ._clean_competition_column import clean_comp_column
from ._clean_xg_difference_cols import clean_xg_difference_cols
from ._drop_matches_column import drop_matches_column
from ._remove_row_headers import remove_row_headers
from ._trim_nation_column import trim_nation_column

common_cleaners = [
    clean_column_names,
    clean_age_column,
    clean_comp_column,
    trim_nation_column,
    remove_row_headers,
    drop_matches_column,
]


common_plus_xg_cleaners = common_cleaners + [clean_xg_difference_cols]

wage_cleaners = [clean_column_names, trim_nation_column]
