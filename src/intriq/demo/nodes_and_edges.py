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

FINANCIAL_METRICS = ['Revenue', 'Gross Margin', 'EBITDA']
NODES = []
# Financial nodes
for i, label in enumerate(FINANCIAL_METRICS, start=1):
    NODES.append(Node(node_data=stNode(
        id=f"FK{i}", label=label, **fk_node_styling_dict)))

# Operational nodes
OPERATIONAL_METRICS = [
    "Inventory \nTurnover", "Supply\nChain\nEfficiency", "Customer\nFootfall",
    "Online\nSales Growth", "Product\nReturn Rate", "Employee\nSatisfaction",
    "Marketing\nROI", "Customer\nLifetime\nValue", "Retail\nSpace\nUtilization",
    "Seasonal\nSales\nPerformance"
]

for i, label in enumerate(OPERATIONAL_METRICS, start=1):
    NODES.append(Node(node_data=stNode(
        id=f"OK{i}", label=label, **ok_node_styling_dict)))

# Edges
EDGES = [
    Edge(source="OK3", label="Impacts", target="FK1",
         color='gray', **edge_styling_dict),
    Edge(source="OK4", label="Boosts", target="FK1",
         color='gray', **edge_styling_dict),
    Edge(source="OK7", label="Influences", target="FK1",
         color='gray', **edge_styling_dict),
    Edge(source="OK5", label="Reduces", target="FK2",
         color='gray', **edge_styling_dict),
    Edge(source="OK1", label="Optimizes", target="FK2",
         color='gray', **edge_styling_dict),
    Edge(source="OK2", label="Enhances", target="FK2",
         color='gray', **edge_styling_dict),
    Edge(source="OK8", label="Increases", target="FK3",
         color='gray', **edge_styling_dict),
    Edge(source="OK6", label="Supports", target="FK3",
         color='gray', **edge_styling_dict),
    Edge(source="OK10", label="Varies", target="FK3",
         color='gray', **edge_styling_dict),
    Edge(source="OK9", label="Improves", target="FK3",
         color='gray', **edge_styling_dict),
    # Additional edges to represent interconnections between operational KPIs
    Edge(source="OK1", label="Influences", target="OK2",
         color='gray', **edge_styling_dict),
    Edge(source="OK3", label="Correlates with",
         target="OK4", color='gray', **edge_styling_dict)
    # Add more edges as required
]

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

feedback_loop_edges = [
    Edge(source="OK6", label="Improves", target="FK1", color='orange',
         **edge_styling_dict),  # Customer Satisfaction to Net Sales
    Edge(source="FK1", label="Increases budget for", target="OK8", color='orange',
         **edge_styling_dict),  # Net Sales to Marketing Effectiveness
    Edge(source="OK8", label="Enhances", target="OK6", color='orange', **
         edge_styling_dict)  # Marketing Effectiveness to Customer Satisfaction
]

# Value Lever nodes
NODES[0].modes.append(Mode.HIGHLIGHT_VALUE_LEVERS)
NODES[5] = Node(
    node_data=stNode(
        id="OK3",
        label="Customer\nFootfall",
        **lever_node_styling_dict
    ),
    modes=[Mode.HIGHLIGHT_VALUE_LEVERS],

)
NODES[6].modes.append(Mode.HIGHLIGHT_VALUE_LEVERS)

# Leverage Point Edge
leverage_point_edge = Edge(
    source="OK3",
    label="Significantly improves",
    target="FK1",
    **operational_lever_edge_styling_dict
)  # Employee Productivity to Reported EBITDA

# Append these special edges to the existing EDGES list
EDGES.extend(feedback_loop_edges)
EDGES.append(leverage_point_edge)

NODES_TRUNCATED = NODES[:5]
