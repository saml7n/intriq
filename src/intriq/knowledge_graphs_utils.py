from dataclasses import dataclass, field
from enum import Enum
from typing import List
from streamlit_agraph import Node as stNode
import streamlit as st
import time
import random
from loguru import logger

from nodes_and_edges import EDGES, NODES, Mode


def get_nodes_and_edges(mode, financial_kpi_options=None):
    mode = Mode(mode)

    # Incredibly hacky way of doing this, but it works for now
    return_nodes = []
    for node in NODES:
        if 'FK' in node.node_data.id:
            if node.node_data.label not in financial_kpi_options:
                continue
        if mode == Mode.ALL_NODES:
            return_nodes.append(node.node_data)
        elif mode in node.modes:
            return_nodes.append(node.node_data)

    return_node_ids = [n.id for n in return_nodes]
    return_edges = [
        e for e in EDGES if e.source in return_node_ids and e.to in return_node_ids
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


def generate_random_numbers_summing_to_100(N):
    # Generate N-1 random numbers
    random_numbers = [random.randint(1, 100) for _ in range(N - 1)]

    # Include 0 and 100 in the list and sort
    random_numbers.extend([0, 100])
    random_numbers.sort()

    # Calculate the differences between successive numbers
    return [random_numbers[i+1] - random_numbers[i] for i in range(N)]
