from typing import Dict, List

import pandas as pd  # type: ignore

sample_raw_data: List[Dict] = [
    {"Shop": "Walmart", "Order": "200.35"},
    {"Shop": "Amazon", "Order": "120.46"},
    {"Shop": "Zalando", "Commissions": "80.65"},
    {"Shop": "Shopify", "Commissions": "467.23"},
]


def transform_raw_data(raw_data: List[Dict]) -> pd.DataFrame:
    """Transforms raw data into a pandas DataFrame.

    Args:
        raw_data (List[Dict]): A list of dictionaries representing the raw data.

    Returns:
        pd.DataFrame: The transformed data in the form of a pandas DataFrame.

    Raises:
        ValueError: If the input raw_data is empty.
    """
    if len(raw_data) > 0:
        df_transformed: pd.DataFrame = pd.DataFrame(raw_data)
        df_transformed["Shop"] = df_transformed["Shop"].str.replace("_|+|,", "")
        df_transformed["Commissions"] = df_transformed["Commissions"].astype(float)
    else:
        raise ValueError("The input data should not be empty")
    return df_transformed
