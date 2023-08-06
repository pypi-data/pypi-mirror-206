from __future__ import annotations

from os.path import dirname

import pandas as pd

from retentioneering.eventstream import Eventstream, EventstreamSchema, RawDataSchema

module_path = dirname(__file__)


def load_simple_shop(as_dataframe: bool = False) -> pd.DataFrame | Eventstream:
    """
    Load a `simple_shop` demonstration dataset.

    Parameters
    ----------
    as_dataframe : bool, default False
        - If ``False`` the dataset is returned as eventstream
        - If ``True`` the dataset is returned as pandas.DataFrame
    """
    df = pd.read_csv(module_path + "/data/simple-onlineshop.csv")
    if as_dataframe:
        return df
    else:
        stream = Eventstream(
            raw_data=df,
            raw_data_schema=RawDataSchema(event_name="event", event_timestamp="timestamp", user_id="user_id"),
            schema=EventstreamSchema(),
        )
        return stream


def load_simple_ab_test() -> pd.DataFrame:
    data = pd.read_csv(module_path + "/data/ab_test_demo.csv")
    data["transaction_ID"] = data["transaction_ID"].astype(str)
    data.loc[data["transaction_ID"] == "nan", "transaction_ID"] = None  # type: ignore
    data.loc[data["transaction_ID"].notna(), "transaction_ID"] = data.loc[
        data["transaction_ID"].notna(), "transaction_ID"
    ].apply(lambda x: x.replace(".0", ""))
    return data
