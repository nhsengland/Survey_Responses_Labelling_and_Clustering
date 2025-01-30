import pandas as pd
import pytest

from src import utils

pytestmark = pytest.mark.no_data_needed


class TestNormaliseColumnNames:
    """
    Tests for the utils.normalise_column_names function
    """

    @pytest.fixture()
    def input_df(self) -> pd.DataFrame:
        """
        Returns a dataframe with messy column names
        """
        data = {
            " Column A ": [1, 2],
            "Column-B": [3, 4],
            "Column(C)": [5, 6],
            "Column/D": [7, 8],
            "Column.E": [9, 10],
            "Column F": [11, 12],
        }
        df = pd.DataFrame(data)
        return df

    @pytest.mark.parametrize(
        "expected_columns, to_lower, strip, replace_values",
        [
            (
                ["column_a", "columnb", "columnc", "column_d", "column_e", "column_f"],
                True,
                True,
                None,
            ),
            (
                ["Column_A", "ColumnB", "ColumnC", "Column_D", "Column_E", "Column_F"],
                False,
                True,
                None,
            ),
            (
                ["_column_a_", "columnb", "columnc", "column_d", "column_e", "column_f"],
                True,
                False,
                None,
            ),
            (
                ["column a", "column-b", "column(c)", "column/d", "column.e", "column f"],
                True,
                True,
                {" ": " "},
            ),
        ],
    )
    def test_normalise_column_names(
        self, input_df, expected_columns, to_lower, strip, replace_values
    ):
        """
        Test the normalise_column_names function. Cases to test:
            1. Check that the column names are normalised under default conditions
            2. Check that the column names are not cast to lower case
            3. Check that the column names are not stripped
            4. Check that the column names are normalised with a custom replace_values dictionary
        """
        result_df = utils.normalise_column_names(
            df=input_df, to_lower=to_lower, strip=strip, replace_values=replace_values
        )
        assert list(result_df.columns) == expected_columns