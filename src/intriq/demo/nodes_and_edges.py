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


fk_node_styling_dict = dict(
    size=25,
    shape='diamond',
    color={
        'border': '#fff', 'background': '#00C853', 'weight': 'light',
        'highlight': {'background': '#00E676', 'border': '#00C853'}},
    borderWidth=2,
    font={'color': '#212121', 'face': 'Helvetica', 'size': 16},
    shadow={'enabled': True,
            'color': 'rgba(0, 0, 0, 0.5)', 'size': 5, 'x': 3, 'y': 3}
)


ok_node_styling_dict = dict(
    size=25,
    shape='dot',
    color={
        'border': 'lightgray', 'background': '#10a3fc',
        'highlight': {'background': '#83c9ff', 'border': '#10a3fc'}},
    borderWidth=2,
    font={'color': '#212121', 'face': 'Helvetica', 'size': 16},
    shadow={'enabled': True,
            'color': 'rgba(0, 0, 0, 0.5)', 'size': 5, 'x': 3, 'y': 3}
)

edge_styling_dict = dict(
    arrows='to',
    smooth={'enabled': True, 'type': 'dynamic'},
    font={'color': '#212121', 'face': 'Helvetica', 'size': 10},
    shadow={'enabled': True,
            'color': 'rgba(0, 0, 0, 0.5)', 'size': 5, 'x': 3, 'y': 3},
    length=400,
    hoverWidth=0.5,
    selectionWidth=2,
    title='Connection'  # Tooltip on hover
)

operational_lever_edge_styling_dict = dict(
    color='#ff4b4b',  # Distinctive color for operational lever edge
    arrows='to',
    smooth={'enabled': True, 'type': 'dynamic'},
    font={'color': '#ff4b4b', 'face': 'Helvetica',
          'size': 12, 'bold': True},  # Bigger, bolder text
    shadow={'enabled': True,
            'color': 'rgba(0, 0, 0, 0.5)', 'size': 5, 'x': 3, 'y': 3},
    length=400,
    hoverWidth=0.5,
    selectionWidth=2,
    title='Operational Lever Connection'  # Tooltip on hover
)

NODES = []

PRIMARY_KPIS = ['Revenue', 'Gross Margin', 'EBITDA']

# Primary KPI nodes
for i, label in enumerate(PRIMARY_KPIS, start=1):
    NODES.append(Node(node_data=stNode(
        id=f'PK{i}', label=label, **fk_node_styling_dict)))

FINANCIAL_METRICS = [
    'Retail Sales', 'E-commerce Sales', 'Miscellaneous Revenue', 'Employee Salary Costs', 'Retail Revenue'
]

# Financial KPI nodes
for i, label in enumerate(FINANCIAL_METRICS, start=1):
    NODES.append(Node(node_data=stNode(
        id=f'FK{i}', label=label, **fk_node_styling_dict)))

# Operational KPI nodes
OPERATIONAL_METRICS = [
    'Inventory Turnover', 'Supply Chain Efficiency', 'Customer Footfall',
    'Online Sales Growth', 'Product Return Rate', 'Employee Satisfaction',
    'Marketing ROI', 'Customer Lifetime Value', 'Retail Space Utilization',
    'Seasonal Sales Performance', 'Retail Collections', 'Workforce Management', 'Pricing', 'Sales Conversion', 'Fitting Room Footfall', 'Store Footfall'
]

for i, label in enumerate(OPERATIONAL_METRICS, start=1):
    NODES.append(Node(node_data=stNode(
        id=f'OK{i}', label=label, **ok_node_styling_dict)))

# Edges
EDGES = [
    # FKs feeding into PKs
    Edge(source='FK1', label='Strong +', target='PK1',
         width=4, color='gray', **edge_styling_dict),
    Edge(source='FK2', label='Strong +', target='PK1',
         width=4, color='gray', **edge_styling_dict),
    Edge(source='FK3', label='Strong +', target='PK1',
         width=4, color='gray', **edge_styling_dict),
    Edge(source='FK4', label='Strong -', target='PK2',
         width=4, color='gray', **edge_styling_dict),
    Edge(source='FK5', label='Strong -', target='PK1',
         width=4, color='gray', **edge_styling_dict),

    # Interconnections between Financial KPIs
    Edge(source='FK1', label='Strong +', target='FK5',
         width=4, color='gray', **edge_styling_dict),

    # OKs feeding into FKs (focused on PK1 - Revenue)
    Edge(source='OK1', label='Medium +', target='FK1',
         width=4, color='gray', **edge_styling_dict),
    Edge(source='OK2', label='Medium +', target='FK2',
         width=4, color='gray', **edge_styling_dict),
    Edge(source='OK3', label='Medium +', target='FK3',
         width=4, color='gray', **edge_styling_dict),
    Edge(source='OK4', label='Medium +', target='FK4',
         width=4, color='gray', **edge_styling_dict),
    Edge(source='OK5', label='Medium -', target='FK5',
         width=4, color='gray', **edge_styling_dict),
    Edge(source='OK6', label='Strong +', target='FK1',
         width=6, color='gray', **edge_styling_dict),
    Edge(source='OK7', label='Medium +', target='FK2',
         width=4, color='gray', **edge_styling_dict),
    Edge(source='OK8', label='Weak +', target='FK3',
         width=2, color='gray', **edge_styling_dict),
    Edge(source='OK9', label='Strong +', target='FK4',
         width=6, color='gray', **edge_styling_dict),
    Edge(source='OK10', label='Weak -', target='FK5',
         width=2, color='gray', **edge_styling_dict),

    # Interconnections between Operational KPIs
    Edge(source='OK11', label='Medium +', target='OK12',
         width=4, color='gray', **edge_styling_dict),
    Edge(source='OK13', label='Medium +', target='OK14',
         width=4, color='gray', **edge_styling_dict),
    Edge(source='OK16', label='Medium +', target='OK15',
         width=2, color='gray', **edge_styling_dict),

    # Additional insightful connections (OKs to PKs)
    Edge(source='OK1', label='Medium +', target='PK1',
         width=4, color='gray', **edge_styling_dict),
    Edge(source='OK3', label='Medium +', target='PK2',
         width=4, color='gray', **edge_styling_dict),
    Edge(source='OK5', label='Strong -', target='PK3',
         width=6, color='gray', **edge_styling_dict),
    Edge(source='OK7', label='Weak +', target='PK1',
         width=2, color='gray', **edge_styling_dict),
    Edge(source='OK9', label='Medium +', target='PK2',
         width=4, color='gray', **edge_styling_dict),
    Edge(source='OK11', label='Weak +', target='PK3',
         width=2, color='gray', **edge_styling_dict),


    # New Edges Based on Additional Points
    # 1. Linking Revenue with its components
    Edge(source='FK1', label='Strong +', target='PK1', width=6,
         color='gray', **edge_styling_dict),  # Retail Sales to Revenue
    Edge(source='FK2', label='Strong +', target='PK1', width=6,
         color='gray', **edge_styling_dict),  # E-commerce Sales to Revenue
    Edge(source='FK3', label='Strong +', target='PK1', width=6,
         color='gray', **edge_styling_dict),  # Miscellaneous Revenue to Revenue

    # 2. & 3. Linking Retail Collections to Retail Sales and Employee Salary Costs
    Edge(
        source='OK11', label='Strong -', target='FK1', width=6, color='gray', **edge_styling_dict),  # Retail Collections negatively impacting Retail Sales
    Edge(
        source='OK11', label='Medium +', target='FK4', width=4, color='gray', **edge_styling_dict),  # Retail Collections leading to increased Employee Salary Costs

    # 4. Linking Conversion to Retail Revenue
    Edge(source='OK13', label='Strong +', target='FK5', width=6, color='gray',
         **edge_styling_dict),  # Sales Conversion (Tx) to Retail Revenue
    Edge(source='OK14', label='Strong +', target='FK5', width=6, color='gray',
         **edge_styling_dict),  # Sales Conversion (£) to Retail Revenue

    # 5. Fitting Room Footfall vs Store Footfall
    Edge(source='OK15', label='Medium +', target='OK3', width=4, color='gray',
         **edge_styling_dict),  # Fitting Room Footfall influencing Store Footfall
    Edge(source='OK15', label='Weak +', target='FK5', width=2, color='gray', **
         edge_styling_dict),   # Fitting Room Footfall weakly influencing Retail Revenue
]


# Feedback Loop for Sales Conversion and Retail Revenue
EDGES.extend([
    Edge(source='FK5', label='Medium +', target='OK3', width=4, color='orange',
         **edge_styling_dict),  # Retail Revenue to Customer Experience
    Edge(source='OK3', label='Medium +', target='OK16', width=4, color='orange',
         **edge_styling_dict),  # Customer Experience to Store Footfall
    Edge(source='OK16', label='Medium +', target='FK5', width=4, color='orange',
         **edge_styling_dict),  # Store Footfall to Sales Conversion (£)
    Edge(source='OK14', label='Medium +', target='FK5', width=4, color='orange',
         **edge_styling_dict),  # Sales Conversion (£) back to Retail Revenue
])

# Value Lever Edges
EDGES.extend([
    Edge(source='OK15', label='Strong +', target='FK5', width=6, **
         operational_lever_edge_styling_dict),  # Fitting Room Experience to Retail Revenue
    # Optimizing Retail Collections to Employee Salary Costs
    Edge(source='OK11', label='Strong -', target='FK4',
         width=4, **operational_lever_edge_styling_dict),
    # Reduced Employee Salary Costs to Retail Revenue
    Edge(source='FK4', label='Strong +', target='FK5',
         width=2, **operational_lever_edge_styling_dict),
])

value_lever_node_ids = ['OK16', 'OK15', 'PK1', 'FK5']

feedback_loop_edges = [
    Edge(source='OK6', label='Improves', target='FK1', color='orange',
         **edge_styling_dict),  # Customer Satisfaction to Net Sales
    Edge(source='FK1', label='Increases budget for', target='OK8', color='orange',
         **edge_styling_dict),  # Net Sales to Marketing Effectiveness
    Edge(source='OK8', label='Enhances', target='OK6', color='orange', **
         edge_styling_dict)  # Marketing Effectiveness to Customer Satisfaction
]

# Value Lever nodes
for node in NODES:
    if node.node_data.id in value_lever_node_ids:
        node.modes.append(Mode.HIGHLIGHT_VALUE_LEVERS)


truncate_node_ids = [
    'PK1', 'FK1', 'FK2', 'OK1', 'OK2', 'OK3', 'OK4', 'OK5', 'OK6',
    'OK7', 'OK8', 'OK9', 'OK10', 'OK11', 'OK12', 'OK13', 'OK14', 'OK15', 'OK16'
]
NODES_TRUNCATED = [
    node for node in NODES if node.node_data.id in truncate_node_ids
]
