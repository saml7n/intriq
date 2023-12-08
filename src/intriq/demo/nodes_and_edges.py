from streamlit_agraph import agraph, Edge, Node as stNode
from dataclasses import dataclass, field
from enum import Enum


class Mode(Enum):
    ALL_NODES = 'All Nodes'
    HIGHLIGHT_VALUE_LEVERS = 'Highlight Value Levers'
    FINANCIAL_KPIS_ONLY = 'Financial KPIs Only'


@dataclass
class Node:
    node_data: stNode
    modes: list[Mode] = field(default_factory=list)


NODES = []
EDGES = []
ok_node_styling_dict = dict(
    size=25,
    shape="dot",
    color={
        'border': 'lightgray', 'background': '#10a3fc',
        'highlight': {'background': '#83c9ff', 'border': '#10a3fc'}},
    borderWidth=2,
    font={'color': '#212121', 'face': 'Helvetica', 'size': 16},
    shadow={'enabled': True,
            'color': 'rgba(0, 0, 0, 0.5)', 'size': 5, 'x': 3, 'y': 3}
)

fk_node_styling_dict = dict(
    size=25,
    shape="diamond",
    color={
        'border': '#fff', 'background': '#00C853', 'weight': 'light',
        'highlight': {'background': '#00E676', 'border': '#00C853'}},
    borderWidth=2,
    font={'color': '#212121', 'face': 'Helvetica', 'size': 16},
    shadow={'enabled': True,
            'color': 'rgba(0, 0, 0, 0.5)', 'size': 5, 'x': 3, 'y': 3}
)

lever_node_styling_dict = dict(
    size=25,
    shape="square",
    color={
        'border': '#fff',  # Red border for emphasis
        'background': '#ff4b4b',  # Standard operational node background
        'highlight': {'background': '#fa9999', 'border': '#ff4b4b'}},  # Highlight changes
    borderWidth=4,  # Thicker and brighter border
    font={'color': '#212121', 'face': 'Helvetica',
          'size': 16, 'bold': True},  # Font adjustments
    shadow={'enabled': True,
            'color': 'rgba(0, 0, 0, 0.5)', 'size': 5, 'x': 3, 'y': 3},
    title="Value Lever Node"  # Tooltip on hover
)

edge_styling_dict = dict(
    arrows='to',
    smooth={'enabled': True, 'type': 'dynamic'},
    font={'color': '#212121', 'face': 'Helvetica', 'size': 10},
    shadow={'enabled': True,
            'color': 'rgba(0, 0, 0, 0.5)', 'size': 5, 'x': 3, 'y': 3},
    width=2,
    length=400,
    hoverWidth=0.5,
    selectionWidth=2,
    title="Connection"  # Tooltip on hover
)

operational_lever_edge_styling_dict = dict(
    color='#ff4b4b',  # Distinctive color for operational lever edge
    arrows='to',
    smooth={'enabled': True, 'type': 'dynamic'},
    font={'color': '#ff4b4b', 'face': 'Helvetica',
          'size': 12, 'bold': True},  # Bigger, bolder text
    shadow={'enabled': True,
            'color': 'rgba(0, 0, 0, 0.5)', 'size': 5, 'x': 3, 'y': 3},
    width=3,  # Thicker line
    length=400,
    hoverWidth=0.5,
    selectionWidth=2,
    title="Operational Lever Connection"  # Tooltip on hover
)

# Financial nodes
NODES.append(
    Node(
        node_data=stNode(
            id="FK1",
            label="Net Sales",
            **fk_node_styling_dict
        ),
        modes=[
            Mode.FINANCIAL_KPIS_ONLY,
            Mode.HIGHLIGHT_VALUE_LEVERS]
    )
)
NODES.append(
    Node(
        node_data=stNode(
            id="FK2",
            label="Gross Profit",
            **fk_node_styling_dict
        ),
        modes=[Mode.FINANCIAL_KPIS_ONLY]
    )
)
NODES.append(
    Node(
        node_data=stNode(
            id="FK3",
            label="Reported EBITDA",
            **fk_node_styling_dict
        ),
        modes=[Mode.FINANCIAL_KPIS_ONLY]
    )
)
NODES.append(
    Node(
        node_data=stNode(
            id="FK4",
            label="Reported Net Income",
            **fk_node_styling_dict
        ),
        modes=[Mode.FINANCIAL_KPIS_ONLY]
    )
)
NODES.append(
    Node(
        node_data=stNode(
            id="FK5",
            label="EBITDA Growth %",
            **fk_node_styling_dict
        ),
        modes=[Mode.FINANCIAL_KPIS_ONLY]
    )
)
NODES.append(
    Node(
        node_data=stNode(
            id="FK6",
            label="EBITDA Margin %",
            **fk_node_styling_dict
        ),
        modes=[Mode.FINANCIAL_KPIS_ONLY]
    )
)

# Operational nodes
NODES.append(
    Node(
        node_data=stNode(
            id="OK1",
            label="Visitors",
            **ok_node_styling_dict
        )
    )
)
NODES.append(
    Node(
        node_data=stNode(
            id="OK2",
            label="Ticketing percap",
            **ok_node_styling_dict)
    )
)
NODES.append(
    Node(
        node_data=stNode(
            id="OK3",
            label="In-Park Revenue",
            **ok_node_styling_dict)
    )
)
NODES.append(
    Node(
        node_data=stNode(
            id="OK4",
            label="Safety Incidents",
            **ok_node_styling_dict
        ),
        modes=[Mode.HIGHLIGHT_VALUE_LEVERS]
    )
)
NODES.append(
    Node(
        node_data=stNode(
            id="OK5",
            label="Customer Satisfaction",
            **ok_node_styling_dict)
    )
)
NODES.append(
    Node(
        node_data=stNode(
            id="OK6",
            label="Employee Productivity",
            **lever_node_styling_dict
        ),
        modes=[Mode.HIGHLIGHT_VALUE_LEVERS]
    )
)
NODES.append(
    Node(
        node_data=stNode(
            id="OK7",
            label="Marketing Effectiveness",
            **ok_node_styling_dict
        )
    )
)
NODES.append(
    Node(
        node_data=stNode(
            id="OK8",
            label="Season Pass Sales",
            **ok_node_styling_dict
        ),
        modes=[Mode.HIGHLIGHT_VALUE_LEVERS]
    )
)
NODES.append(
    Node(
        node_data=stNode(
            id="OK9",
            label="Customer Loyalty",
            **ok_node_styling_dict
        )
    )
)

EDGES.append(Edge(source="OK1",
                  label="Increases",
                  target="FK2",
                  color='gray',
                  **edge_styling_dict
                  )
             )
EDGES.append(Edge(source="OK2",
                  label="Increases",
                  target="FK2",
                  color='gray',
                  **edge_styling_dict
                  )
             )
# Visitor impact on sales
EDGES.append(Edge(source="OK1",
                  label="Increases",
                  target="FK1",
                  color='gray',
                  **edge_styling_dict

                  )
             )
# Ticketing percap impact on Net Sales
EDGES.append(Edge(source="OK2",
                  label="Impacts",
                  target="FK1",
                  color='gray',
                  **edge_styling_dict
                  )
             )
# In-Park Revenue impact on Net Sales
EDGES.append(Edge(source="OK3",
                  label="Boosts",
                  target="FK1",
                  color='gray',
                  **edge_styling_dict
                  )
             )
# Safety Incidents impact on Customer Satisfaction
EDGES.append(Edge(source="OK4",
                  label="Negatively affects",
                  target="OK6",
                  color='gray',
                  **edge_styling_dict
                  )
             )
# Customer Satisfaction impact on Net Sales
EDGES.append(Edge(source="OK6",
                  label="Increases",
                  target="FK1",
                  color='gray',
                  **edge_styling_dict
                  )
             )
# Employee Productivity impact on Reported EBITDA
EDGES.append(Edge(source="OK7",
                  label="Improves",
                  target="FK3",
                  color='gray',
                  **edge_styling_dict))
# Marketing Effectiveness impact on Visitors
EDGES.append(Edge(source="OK8",
                  label="Attracts more",
                  target="OK1",
                  color='gray',
                  **edge_styling_dict))
EDGES.append(Edge(source="OK9",
                  label="Contributes to",
                  target="FK1",
                  color='gray',
                  **edge_styling_dict))
EDGES.append(Edge(source="OK9",
                  label="Boosts",
                  target="OK10",
                  color='gray',
                  **edge_styling_dict))
EDGES.append(Edge(source="OK10",
                  label="Enhances",
                  target="FK2",
                  color='gray',
                  **edge_styling_dict))
EDGES.append(Edge(source="OK7",
                  label="Increases",
                  target="FK1",
                  color='gray',
                  **edge_styling_dict))
EDGES.append(Edge(source="OK6",  # Customer Satisfaction
                  label="Increases",
                  target="FK1",  # Net Sales
                  color='gray',
                  **edge_styling_dict))
EDGES.append(Edge(source="OK6",  # Customer Satisfaction
                  label="Boosts",
                  target="OK10",  # Customer Loyalty
                  color='gray',
                  **edge_styling_dict))
EDGES.append(Edge(source="OK6",  # Customer Satisfaction
                  label="Enhances",
                  target="OK8",  # Marketing Effectiveness
                  color='gray',
                  **edge_styling_dict))

# Example of a Feedback Loop (Customer Satisfaction to Net Sales to Marketing Effectiveness)
EDGES.append(Edge(source="OK6",  # Customer Satisfaction
                  label="Improves",
                  target="FK1",
                  color='orange',
                  **edge_styling_dict,  # Net Sales
                  )
             )
EDGES.append(Edge(source="FK1",  # Net Sales
                  label="Increases budget for",
                  target="OK8",  # Marketing Effectiveness
                  color='orange',
                  **edge_styling_dict)
             )
EDGES.append(Edge(source="OK8",  # Marketing Effectiveness
                  label="Enhances",
                  target="OK6",  # Customer Satisfaction
                  color='orange',
                  **edge_styling_dict
                  )
             )
# Edge showing leverage point impact
EDGES.append(Edge(source="OK7",  # Employee Productivity
                  label="Significantly improves",
                  target="FK3",  # Reported EBITDA
                  **operational_lever_edge_styling_dict)
             )

NODES_TRUNCATED = NODES[1:2] + NODES[7:11]
