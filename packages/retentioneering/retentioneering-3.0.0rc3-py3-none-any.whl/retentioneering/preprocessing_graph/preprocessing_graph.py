from __future__ import annotations

import json
from typing import Any, List, Literal, Optional, TypedDict, cast

import networkx
from IPython.core.display import HTML, DisplayHandle, display
from pydantic import ValidationError

from retentioneering.backend import JupyterServer, ServerManager
from retentioneering.backend.callback import list_dataprocessor, list_dataprocessor_mock
from retentioneering.eventstream.types import EventstreamType
from retentioneering.exceptions.server import ServerErrorWithResponse
from retentioneering.exceptions.widget import WidgetParseError
from retentioneering.preprocessing_graph.nodes import (
    EventsNode,
    MergeNode,
    Node,
    SourceNode,
    build_node,
)
from retentioneering.templates import PreprocessingGraphRenderer


class NodeData(TypedDict):
    name: str
    pk: str
    description: Optional[str]
    processor: Optional[dict]


class NodeLink(TypedDict):
    source: str
    target: str


class Payload(TypedDict):
    directed: bool
    nodes: list[NodeData]
    links: list[NodeLink]


class CombineHandlerPayload(TypedDict):
    node_pk: str


class FieldErrorDesc(TypedDict):
    field: str
    msg: str


class CreateNodeErrorDesc(TypedDict):
    type: Literal["node_error"]
    node_pk: str
    msg: Optional[str]
    fields_errors: List[FieldErrorDesc]


class PreprocessingGraph:
    """
    Collection of methods for preprocessing graph construction and calculation.

    Parameters
    ----------
    source_stream : EventstreamType
        Source eventstream.

    Notes
    -----
    See :doc:`Preprocessing user guide</user_guides/preprocessing>` for the details.

    """

    root: SourceNode
    combine_result: EventstreamType | None
    _ngraph: networkx.DiGraph
    __server_manager: ServerManager | None = None
    __server: JupyterServer | None = None

    def __init__(self, source_stream: EventstreamType) -> None:
        self.root = SourceNode(source=source_stream)
        self.combine_result = None
        self._ngraph = networkx.DiGraph()
        self._ngraph.add_node(self.root)

    def add_node(self, node: Node, parents: List[Node]) -> None:
        """
        Add node to ``PreprocessingGraph`` instance.

        Parameters
        ----------
        node : Node
            An instance of either ``EventsNode`` or ``MergeNode``.
        parents : list of Nodes

            - If ``node`` is ``EventsNode`` - only 1 parent must be defined.
            - If ``node`` is ``MergeNode`` - at least 2 parents have to be defined.

        Returns
        -------
        None

        See Also
        --------
        PreprocessingGraph.combine : Start PreprocessingGraph recalculation.
        .EventsNode : Regular nodes of a preprocessing graph.
        .MergeNode : Merge nodes of a preprocessing graph.

        """
        self.__valiate_already_exists(node)
        self.__validate_not_found(parents)

        if node.events is not None:
            self.__validate_schema(node.events)

        if not isinstance(node, MergeNode) and len(parents) > 1:
            raise ValueError("multiple parents are only allowed for merge nodes!")

        self._ngraph.add_node(node)

        for parent in parents:
            self._ngraph.add_edge(parent, node)

    def combine(self, node: Node) -> EventstreamType:
        """
        Run calculations from the ``SourceNode`` up to the specified ``node``.

        Parameters
        ----------
        node : Node
            Instance of either ``SourceNode``, ``EventsNode`` or ``MergeNode``.

        Returns
        -------
        EventstreamType
            ``Eventstream`` with all changes applied by data processors.
        """
        self.__validate_not_found([node])

        if isinstance(node, SourceNode):
            return node.events.copy()

        if isinstance(node, EventsNode):
            return self._combine_events_node(node)

        return self._combine_merge_node(node)

    def _combine_events_node(self, node: EventsNode) -> EventstreamType:
        parent = self._get_events_node_parent(node)
        parent_events = self.combine(parent)
        events = node.processor.apply(parent_events)
        parent_events._join_eventstream(events)
        return parent_events

    def _combine_merge_node(self, node: MergeNode) -> EventstreamType:
        parents = self._get_merge_node_parents(node)
        curr_eventstream: Optional[EventstreamType] = None

        for parent_node in parents:
            if curr_eventstream is None:
                curr_eventstream = self.combine(parent_node)
            else:
                new_eventstream = self.combine(parent_node)
                curr_eventstream.append_eventstream(new_eventstream)

        node.events = curr_eventstream

        return cast(EventstreamType, curr_eventstream)

    def get_parents(self, node: Node) -> List[Node]:
        """
        Show parents of the specified ``node``.

        Parameters
        ----------
        node : Node
            Instance of one of the classes SourceNode, EventsNode or MergeNode.

        Returns
        -------
        list of Nodes

        """
        self.__validate_not_found([node])
        parents: List[Node] = []

        for parent in self._ngraph.predecessors(node):
            parents.append(parent)
        return parents

    def _get_merge_node_parents(self, node: MergeNode) -> List[Node]:
        parents = self.get_parents(node)
        if len(parents) == 0:
            raise ValueError("orphan merge node!")

        return parents

    def _get_events_node_parent(self, node: EventsNode) -> Node:
        parents = self.get_parents(node)
        if len(parents) > 1:
            raise ValueError("invalid graph: events node has more than 1 parent")

        return parents[0]

    def __validate_schema(self, eventstream: EventstreamType) -> bool:
        return self.root.events.schema.is_equal(eventstream.schema)

    def __valiate_already_exists(self, node: Node) -> None:
        if node in self._ngraph.nodes:
            raise ValueError("node already exists!")

    def __validate_not_found(self, nodes: List[Node]) -> None:
        for node in nodes:
            if node not in self._ngraph.nodes:
                raise ValueError("node not found!")

    def display(self, width: int = 960, height: int = 600) -> DisplayHandle:
        """
        Show constructed ``PreprocessingGraph``.

        Parameters
        ----------
        width : int, default 960
            Width of plot in pixels.
        height : int, default 600
            Height of plot in pixels.

        Returns
        -------
            Rendered preprocessing graph.
        """
        if not self.__server_manager:
            self.__server_manager = ServerManager()

        if not self.__server:
            self.__server = self.__server_manager.create_server()
            self.__server.register_action("list-dataprocessor-mock", list_dataprocessor_mock)
            self.__server.register_action("list-dataprocessor", list_dataprocessor)
            self.__server.register_action("set-graph", self._set_graph_handler)
            self.__server.register_action("get-graph", self.export)
            self.__server.register_action("combine", self._combine_handler)

        render = PreprocessingGraphRenderer()
        return display(
            HTML(
                render.show(
                    server_id=self.__server.pk, env=self.__server_manager.check_env(), width=width, height=height
                )
            )
        )

    def export(self, payload: dict[str, Any]) -> dict:
        """
        Show ``PreprocessingGraph`` as a dict.

        Parameters
        ----------
        payload : dict

        Returns
        -------
        dict

        """
        source, target, link = "source", "target", "links"
        graph = self._ngraph
        data = {
            "directed": graph.is_directed(),
            "nodes": [n.export() for n in graph],
            link: [{source: u.pk, target: v.pk} for u, v, d in graph.edges(data=True)],
        }
        return data

    def _export_to_json(self) -> str:
        data = self.export(payload=dict())
        return json.dumps(data)

    def _combine_handler(self, payload: CombineHandlerPayload) -> None:
        node = self._find_node(payload["node_pk"])
        if not node:
            raise ServerErrorWithResponse(message="node not found!", type="unexpected_error")
        self.combine_result = self.combine(node)

    def _set_graph_handler(self, payload: Payload) -> dict:
        current_graph = self._ngraph
        current_root = self.root

        def restore_graph() -> None:
            self._ngraph = current_graph
            self.root = current_root

        try:
            self._set_graph(payload=payload)
            return self.export({})
        except ServerErrorWithResponse as err:
            restore_graph()
            raise err
        except Exception as err:
            restore_graph()
            raise ServerErrorWithResponse(message=str(err), type="unexpected_error")

    def _set_graph(self, payload: Payload) -> None:
        """
        Payload example:

        {
            "nodes": [
                {
                    "name": "SourceNode",
                    "pk": "0dc3b706-e6cc-401e-96f7-6a45d3947d5c"
                },
                {
                    "name": "EventsNode",
                    "pk": "07921cb0-60b8-45af-928d-272d1b622b25",
                    "processor": {
                        "name": "SimpleGroup",
                        "values": {"event_name": "add_to_cart", "event_type": "group_alias"},
                    },
                },
                {
                    "name": "EventsNode",
                    "pk": "114251ae-0f03-45e6-a163-af51bb02dfd5",
                    "processor": {
                        "name": "SimpleGroup",
                        "values": {"event_name": "logout", "event_type": "group_alias"},
                    },
                },
            ],
            "links": [
                {
                    'source': '0dc3b706-e6cc-401e-96f7-6a45d3947d5c',
                    'target': '07921cb0-60b8-45af-928d-272d1b622b25'
                },
                {
                    'source': '07921cb0-60b8-45af-928d-272d1b622b25',
                    'target': '114251ae-0f03-45e6-a163-af51bb02dfd5'
                }
            ]
        }

        """
        errors: List[CreateNodeErrorDesc] = []
        nodes: List[Node] = []

        # create nodes & validate params
        for node in payload["nodes"]:
            node_pk = node["pk"]
            processor = node.get("processor", {})
            processor_name = processor.get("name", None) if processor else None
            processor_params = processor.get("values", None) if processor else None
            description = node.get("description", None)

            try:
                actual_node = build_node(
                    source_stream=self.root.events,
                    pk=node_pk,
                    node_name=node["name"],
                    processor_name=processor_name,
                    processor_params=processor_params,
                    descriptionn=description,
                )
                nodes.append(actual_node)
            except Exception as error:
                error_desc = self._build_node_error_desc(node_pk=node_pk, error=error)
                errors.append(error_desc)

        if errors:
            raise ServerErrorWithResponse(message="set graph error", type="create_nodes_error", errors=errors)

        self._ngraph = networkx.DiGraph()

        # add nodes
        for created_node in nodes:
            if isinstance(created_node, SourceNode):
                self.root = created_node
            self._ngraph.add_node(created_node)

        # add links
        # @TODO: validate links (graph structure)
        for link in payload["links"]:
            source = self._find_node(link["source"])
            target = self._find_node(link["target"])
            if not source:
                raise ServerErrorWithResponse(message="source not found", type="create_link_error")
            if not target:
                raise ServerErrorWithResponse(message="target not found", type="create_link_error")
            self._ngraph.add_edge(source, target)

    def _build_node_error_desc(self, node_pk: str, error: Exception) -> CreateNodeErrorDesc:
        if isinstance(error, ValidationError):
            return self._build_pydantic_error_desc(
                node_pk=node_pk,
                validation_error_exception=error,
            )

        if isinstance(error, WidgetParseError):
            field_errors: List[FieldErrorDesc] = (
                [{"field": error.field_name, "msg": str(error)}] if error.field_name else []
            )
            return {
                "type": "node_error",
                "msg": str(error),
                "node_pk": node_pk,
                "fields_errors": field_errors,
            }

        return {
            "type": "node_error",
            "msg": str(error),
            "node_pk": node_pk,
            "fields_errors": [],
        }

    def _build_pydantic_error_desc(
        self, node_pk: str, validation_error_exception: ValidationError
    ) -> CreateNodeErrorDesc:
        raw_errs = validation_error_exception.errors()
        result_errors: List[FieldErrorDesc] = []

        for raw_err in raw_errs:
            loc = raw_err.get("loc", ())
            field = next(iter(loc), None)
            msg = raw_err.get("msg")

            result_errors.append(
                {
                    "field": str(field),
                    "msg": msg,
                }
            )

        return {"type": "node_error", "node_pk": node_pk, "msg": "node error", "fields_errors": result_errors}

    def _find_parents_by_links(self, target_node: str, link_list: list[NodeLink]) -> list[Node]:
        parents: list[str] = []
        for node in link_list:
            if node["target"] == target_node:
                parents.append(node["source"])

        parent_nodes = [self._find_node(parent) for parent in parents]
        return parent_nodes  # type: ignore

    def _find_node(self, pk: str) -> Node | None:
        for node in self._ngraph:
            if node.pk == pk:
                return node
        else:
            return None
