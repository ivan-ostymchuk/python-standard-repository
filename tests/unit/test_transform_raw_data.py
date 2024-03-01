from typing import Dict, List

import pandas as pd  # type: ignore
import pytest

from src.extractor import transform_raw_data


@pytest.fixture(scope="session")
def mock_data() -> List[Dict]:
    return [
        {"Shop": "Walmart", "Order": "200.35"},
        {"Shop": "Amazon", "Order": "120.46"},
        {"Shop": "Zalando", "Commissions": "80.65"},
        {"Shop": "Shopify", "Commissions": "467.23"},
    ]


def test_transform_raw_data(mock_data) -> None:
    df_result: pd.DataFrame = transform_raw_data(mock_data)
    list_of_banned_characters: List[str] = [",", "+", "_"]
    number_of_records_with_banned_characters: int = len(
        df_result[df_result["Shop"].isin(list_of_banned_characters)]
    )

    assert (
        number_of_records_with_banned_characters == 0
    ), "Some of the characters do not get trimmed correctly"
    assert (
        df_result.dtypes["Commissions"] == "float64"
    ), "Commissions column should be of float64 type"


def test_raise_error_transform_raw_data() -> None:
    with pytest.raises(ValueError):
        (
            transform_raw_data([]),
            "The function should raise a ValueError on empty dataframe",
        )
