import pandas as pd
import numpy as np
from pandas._testing import assert_frame_equal
from src.features.build_features import clean_data


def test_clean_data():
    # given
    dataframe = pd.DataFrame(
        {
            "col1": [1, 2, 3, 1],
            "col2": ["A", "B", np.nan, "A"],
            "irrelevant_col": [4, 5, 6, 4],
        }
    )

    # when
    cleaned_dataframe = clean_data(dataframe, columns=["irrelevant_col"])

    # then
    assert_frame_equal(
        cleaned_dataframe, pd.DataFrame({"col1": [1, 2, 3], "col2": ["A", "B", np.nan]})
    )
