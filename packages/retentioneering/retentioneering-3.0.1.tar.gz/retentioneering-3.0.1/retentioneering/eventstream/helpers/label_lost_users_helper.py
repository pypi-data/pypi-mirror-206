from __future__ import annotations

from typing import List, Optional, Tuple

from retentioneering.backend.tracker import track
from retentioneering.constants import DATETIME_UNITS

from ..types import EventstreamType


class LabelLostUsersHelperMixin:
    @track(  # type: ignore
        tracking_info={"event_name": "helper"},
        scope="label_lost_users",
        event_value="combine",
        allowed_params=[
            "timeout",
            "lost_users_list",
        ],
    )
    def label_lost_users(
        self, timeout: Optional[Tuple[float, DATETIME_UNITS]] = None, lost_users_list: Optional[List[int]] = None
    ) -> EventstreamType:
        """
        A method of ``Eventstream`` class that creates one
        of the synthetic events in each user's path: ``lost_user`` or ``absent_user`` .

        Parameters
        ----------
        See parameters description
            :py:class:`.LabelLostUsers`

        Returns
        -------
        Eventstream
             Input ``eventstream`` with new synthetic events.



        """

        # avoid circular import
        from retentioneering.data_processors_lib import (
            LabelLostUsers,
            LabelLostUsersParams,
        )
        from retentioneering.preprocessing_graph import PreprocessingGraph
        from retentioneering.preprocessing_graph.nodes import EventsNode

        p = PreprocessingGraph(source_stream=self)  # type: ignore

        node = EventsNode(
            processor=LabelLostUsers(
                params=LabelLostUsersParams(timeout=timeout, lost_users_list=lost_users_list)  # type: ignore
            )
        )
        p.add_node(node=node, parents=[p.root])
        result = p.combine(node)
        del p
        return result
