from dataclasses import dataclass, field
from enum import Enum
from typing import List
from streamlit_agraph import agraph, Edge, Node as stNode
import streamlit as st
import time
import random
from loguru import logger


class Mode(Enum):
    ALL_NODES = 'All Nodes'
    HIGHLIGHT_VALUE_LEVERS = 'Highlight Value Levers'
    FINANCIAL_KPIS_ONLY = 'Financial KPIs Only'


@dataclass
class Node:
    node_data: stNode
    modes: list[Mode] = field(default_factory=list)


def get_nodes_and_edges(mode, financial_kpi_options=None):
    nodes = []
    edges = []
    ok_node_styling_dict = dict(
        size=25,
        shape="circle",
        color={
            'border': 'lightgray', 'background': 'dodgerblue',
            'highlight': {'background': 'lightskyblue', 'border': 'gray'}},
        borderWidth=2,
        font={'color': 'white', 'face': 'Courier New', 'size': 12},
        shadow={'enabled': True,
                'color': 'rgba(0, 0, 0, 0.5)', 'size': 5, 'x': 3, 'y': 3}
    )

    fk_node_styling_dict = dict(
        size=25,
        shape="circle",
        color={
            'border': 'lightgray', 'background': 'mediumseagreen',
            'highlight': {'background': 'lightgreen', 'border': 'gray'}},
        borderWidth=2,
        font={'color': 'white', 'face': 'Courier New', 'size': 12},
        shadow={'enabled': True,
                'color': 'rgba(0, 0, 0, 0.5)', 'size': 5, 'x': 3, 'y': 3}
    )

    lever_node_styling_dict = dict(
        size=25,
        shape="circle",
        color={
            'border': 'red',  # Red border for emphasis
            'background': 'dodgerblue',  # Standard operational node background
            'highlight': {'background': 'lightskyblue', 'border': 'red'}},  # Highlight changes
        borderWidth=4,  # Thicker and brighter border
        font={'color': 'white', 'face': 'Helvetica',
              'size': 14, 'bold': True},  # Font adjustments
        shadow={'enabled': True,
                'color': 'rgba(0, 0, 0, 0.3)', 'size': 5, 'x': 3, 'y': 3},
        title="Value Lever Node"  # Tooltip on hover
    )

    edge_styling_dict = dict(
        arrows='to',
        smooth={'enabled': True, 'type': 'dynamic'},
        font={'color': 'black', 'face': 'Arial', 'size': 10},
        shadow={'enabled': True,
                'color': 'rgba(0, 0, 0, 0.5)', 'size': 5, 'x': 3, 'y': 3},
        width=2,
        length=400,
        hoverWidth=0.5,
        selectionWidth=2,
        title="Connection"  # Tooltip on hover
    )

    operational_lever_edge_styling_dict = dict(
        color='darkred',  # Distinctive color for operational lever edge
        arrows='to',
        smooth={'enabled': True, 'type': 'dynamic'},
        font={'color': 'darkred', 'face': 'Arial',
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
    nodes.append(
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
    nodes.append(
        Node(
            node_data=stNode(
                id="FK2",
                label="Gross Profit",
                **fk_node_styling_dict
            ),
            modes=[Mode.FINANCIAL_KPIS_ONLY]
        )
    )
    nodes.append(
        Node(
            node_data=stNode(
                id="FK3",
                label="Reported EBITDA",
                **fk_node_styling_dict
            ),
            modes=[Mode.FINANCIAL_KPIS_ONLY]
        )
    )
    nodes.append(
        Node(
            node_data=stNode(
                id="FK4",
                label="Reported Net Income",
                **fk_node_styling_dict
            ),
            modes=[Mode.FINANCIAL_KPIS_ONLY]
        )
    )
    nodes.append(
        Node(
            node_data=stNode(
                id="FK5",
                label="EBITDA Growth %",
                **fk_node_styling_dict
            ),
            modes=[Mode.FINANCIAL_KPIS_ONLY]
        )
    )
    nodes.append(
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
    nodes.append(
        Node(
            node_data=stNode(
                id="OK1",
                label="Visitors",
                **ok_node_styling_dict
            )
        )
    )
    nodes.append(
        Node(
            node_data=stNode(
                id="OK2",
                label="Ticketing percap",
                **ok_node_styling_dict)
        )
    )
    nodes.append(
        Node(
            node_data=stNode(
                id="OK3",
                label="In-Park Revenue",
                **ok_node_styling_dict)
        )
    )
    nodes.append(
        Node(
            node_data=stNode(
                id="OK4",
                label="Safety Incidents",
                **ok_node_styling_dict
            ),
            modes=[Mode.HIGHLIGHT_VALUE_LEVERS]
        )
    )
    nodes.append(
        Node(
            node_data=stNode(
                id="OK5",
                label="Customer Satisfaction",
                **ok_node_styling_dict)
        )
    )
    nodes.append(
        Node(
            node_data=stNode(
                id="OK6",
                label="Employee Productivity",
                **lever_node_styling_dict
            ),
            modes=[Mode.HIGHLIGHT_VALUE_LEVERS]
        )
    )
    nodes.append(
        Node(
            node_data=stNode(
                id="OK7",
                label="Marketing Effectiveness",
                **ok_node_styling_dict
            )
        )
    )
    nodes.append(
        Node(
            node_data=stNode(
                id="OK8",
                label="Season Pass Sales",
                **ok_node_styling_dict
            ),
            modes=[Mode.HIGHLIGHT_VALUE_LEVERS]
        )
    )
    nodes.append(
        Node(
            node_data=stNode(
                id="OK9",
                label="Customer Loyalty",
                **ok_node_styling_dict
            )
        )
    )

    edges.append(Edge(source="OK1",
                      label="Increases",
                      target="FK2",
                      color='gray',
                      **edge_styling_dict
                      )
                 )
    edges.append(Edge(source="OK2",
                      label="Increases",
                      target="FK2",
                      color='gray',
                      **edge_styling_dict
                      )
                 )
    # Visitor impact on sales
    edges.append(Edge(source="OK1",
                      label="Increases",
                      target="FK1",
                      color='gray',
                      **edge_styling_dict

                      )
                 )
    # Ticketing percap impact on Net Sales
    edges.append(Edge(source="OK2",
                      label="Impacts",
                      target="FK1",
                      color='gray',
                      **edge_styling_dict
                      )
                 )
    # In-Park Revenue impact on Net Sales
    edges.append(Edge(source="OK3",
                      label="Boosts",
                      target="FK1",
                      color='gray',
                      **edge_styling_dict
                      )
                 )
    # Safety Incidents impact on Customer Satisfaction
    edges.append(Edge(source="OK4",
                      label="Negatively affects",
                      target="OK6",
                      color='gray',
                      **edge_styling_dict
                      )
                 )
    # Customer Satisfaction impact on Net Sales
    edges.append(Edge(source="OK6",
                      label="Increases",
                      target="FK1",
                      color='gray',
                      **edge_styling_dict
                      )
                 )
    # Employee Productivity impact on Reported EBITDA
    edges.append(Edge(source="OK7",
                      label="Improves",
                      target="FK3",
                      color='gray',
                      **edge_styling_dict))
    # Marketing Effectiveness impact on Visitors
    edges.append(Edge(source="OK8",
                      label="Attracts more",
                      target="OK1",
                      color='gray',
                      **edge_styling_dict))
    edges.append(Edge(source="OK9",
                      label="Contributes to",
                      target="FK1",
                      color='gray',
                      **edge_styling_dict))
    edges.append(Edge(source="OK9",
                      label="Boosts",
                      target="OK10",
                      color='gray',
                      **edge_styling_dict))
    edges.append(Edge(source="OK10",
                      label="Enhances",
                      target="FK2",
                      color='gray',
                      **edge_styling_dict))
    edges.append(Edge(source="OK7",
                      label="Increases",
                      target="FK1",
                      color='gray',
                      **edge_styling_dict))
    edges.append(Edge(source="OK6",  # Customer Satisfaction
                      label="Increases",
                      target="FK1",  # Net Sales
                      color='gray',
                      **edge_styling_dict))
    edges.append(Edge(source="OK6",  # Customer Satisfaction
                      label="Boosts",
                      target="OK10",  # Customer Loyalty
                      color='gray',
                      **edge_styling_dict))
    edges.append(Edge(source="OK6",  # Customer Satisfaction
                      label="Enhances",
                      target="OK8",  # Marketing Effectiveness
                      color='gray',
                      **edge_styling_dict))

    # Example of a Feedback Loop (Customer Satisfaction to Net Sales to Marketing Effectiveness)
    edges.append(Edge(source="OK6",  # Customer Satisfaction
                      label="Improves",
                      target="FK1",
                      color='orange',
                      **edge_styling_dict,  # Net Sales
                      )
                 )
    edges.append(Edge(source="FK1",  # Net Sales
                      label="Increases budget for",
                      target="OK8",  # Marketing Effectiveness
                      color='orange',
                      **edge_styling_dict)
                 )
    edges.append(Edge(source="OK8",  # Marketing Effectiveness
                      label="Enhances",
                      target="OK6",  # Customer Satisfaction
                      color='orange',
                      **edge_styling_dict
                      )
                 )
    # Edge showing leverage point impact
    edges.append(Edge(source="OK7",  # Employee Productivity
                      label="Significantly improves",
                      target="FK3",  # Reported EBITDA
                      **operational_lever_edge_styling_dict)
                 )
    mode = Mode(mode)

    # Incredibly hacky way of doing this, but it works for now
    return_nodes = []
    for node in nodes:
        if 'FK' in node.node_data.id:
            if node.node_data.label not in financial_kpi_options:
                continue
        if mode == Mode.ALL_NODES:
            return_nodes.append(node.node_data)
        elif mode in node.modes:
            return_nodes.append(node.node_data)

    return_node_ids = [n.id for n in return_nodes]
    return_edges = [
        e for e in edges if e.source in return_node_ids and e.to in return_node_ids
    ]
    return return_nodes, return_edges


def display_loading_bar():
    progress_text = "Analysing financial data."
    my_bar = st.progress(0, text="Analysing financial data.")
    for percent_complete in range(10):
        sleep_time = random.randint(1, 10) / 100
        time.sleep(sleep_time)
        my_bar.progress(percent_complete + 1, text="Analysing financial data.")

    for percent_complete in range(20, 40):
        sleep_time = random.randint(1, 10) / 100
        time.sleep(sleep_time)
        my_bar.progress(percent_complete + 1,
                        text="Analysing operational data.")

    for percent_complete in range(40, 60):
        sleep_time = random.randint(1, 10) / 200
        time.sleep(sleep_time)
        my_bar.progress(percent_complete + 1, text="Evaluating relationships.")

    for percent_complete in range(60, 70):
        sleep_time = random.randint(1, 10) / 100
        time.sleep(sleep_time)
        my_bar.progress(percent_complete + 1,
                        text="Contemplating the fragility of life.")

    for percent_complete in range(70, 100):
        sleep_time = random.randint(1, 10) / 100
        time.sleep(sleep_time)
        my_bar.progress(percent_complete + 1, text="Creating data mappings.")

    time.sleep(1)
    my_bar.empty()
