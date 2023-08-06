from __future__ import annotations

from typing import Any, Callable, List

import pandas as pd

from retentioneering.backend.tracker import track
from retentioneering.data_processor import DataProcessor
from retentioneering.eventstream.schema import EventstreamSchema
from retentioneering.eventstream.types import EventstreamType
from retentioneering.params_model import ParamsModel
from retentioneering.widget.widgets import ListOfString, ReteFunction

EventstreamFilter = Callable[[pd.DataFrame, EventstreamSchema], Any]


def _default_func(eventstream: EventstreamType, targets: List[str]) -> pd.DataFrame:
    """
    Filter rows with target events from the input eventstream.

    Parameters
    ----------
    eventstream : Eventstream
        Source eventstream or output from previous nodes.

    targets : list of str
        Each event from that list is associated with the bad result (scenario)
        of user's behaviour (experience) in the product.
        If there are several target events in user path - the event with minimum timestamp is taken.

    Returns
    -------
    pd.DataFrame
        Filtered DataFrame with targets and its timestamps.
    """
    user_col = eventstream.schema.user_id
    time_col = eventstream.schema.event_timestamp
    event_col = eventstream.schema.event_name
    df = eventstream.to_dataframe()

    targets_index = df[df[event_col].isin(targets)].groupby(user_col)[time_col].idxmin()  # type: ignore

    return df.loc[targets_index]  # type: ignore


class AddNegativeEventsParams(ParamsModel):
    """
    A class with parameters for :py:class:`.AddNegativeEvents` class.
    """

    targets: List[str]
    func: Callable = _default_func

    _widgets = {"func": ReteFunction(), "targets": ListOfString()}


class AddNegativeEvents(DataProcessor):
    """
    Create new synthetic events in paths of all users having the specified event(s):
    ``negative_target_RAW_EVENT_NAME``.

    Parameters
    ----------
    targets : list of str
        Define the list of events that we consider negative.
        If there are several target events in the user path, the event with the minimum timestamp is taken.

    func : Callable, default _default_func_negative
        Filter rows with target events from the input eventstream.

    Returns
    -------
    Eventstream
        ``Eventstream`` with new synthetic events only added to the users who fit the conditions.

        +--------------------------------+-----------------+-----------------------------+
        | **event_name**                 | **event_type**  | **timestamp**               |
        +--------------------------------+-----------------+-----------------------------+
        | negative_target_RAW_EVENT_NAME | negative_target | min(targets)                |
        +--------------------------------+-----------------+-----------------------------+

    Notes
    -----
    See :doc:`Data processors user guide</user_guides/dataprocessors>` for the details.


    """

    params: AddNegativeEventsParams

    @track(  # type: ignore
        tracking_info={"event_name": "init"},
        scope="add_negative_events",
        allowed_params=[],
    )
    def __init__(self, params: AddNegativeEventsParams):
        super().__init__(params=params)

    @track(  # type: ignore
        tracking_info={"event_name": "apply"},
        scope="add_negative_events",
        allowed_params=[],
    )
    def apply(self, eventstream: EventstreamType) -> EventstreamType:
        from retentioneering.eventstream.eventstream import Eventstream

        type_col = eventstream.schema.event_type
        event_col = eventstream.schema.event_name

        func = self.params.func
        targets = self.params.targets

        negative_targets = func(eventstream, targets)
        negative_targets[type_col] = "negative_target"
        negative_targets[event_col] = "negative_target_" + negative_targets[event_col]
        negative_targets["ref"] = None

        eventstream = Eventstream(
            raw_data_schema=eventstream.schema.to_raw_data_schema(),
            raw_data=negative_targets,
            relations=[{"raw_col": "ref", "eventstream": eventstream}],
        )
        return eventstream
