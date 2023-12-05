from dataclasses import dataclass, field
from enum import Enum
from typing import List
import numpy as np
from streamlit_agraph import Node as stNode
import streamlit as st
import time
import random
from loguru import logger
import plotly.express as px
import pandas as pd

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
    return True


def generate_random_numbers_summing_to_100(N):
    # Generate N-1 random numbers
    random_numbers = [random.randint(1, 100) for _ in range(N - 1)]

    # Include 0 and 100 in the list and sort
    random_numbers.extend([0, 100])
    random_numbers.sort()

    # Calculate the differences between successive numbers
    return [random_numbers[i+1] - random_numbers[i] for i in range(N)]


@st.cache_data(ttl=60*60*24)
def generate_performance_numbers(categories, option):
    performance_data = {}
    for category in categories:
        monthly_increases = []
        # Starting with a small positive value
        last_increase = random.uniform(0, 5)
        for _ in range(12):
            # Ensuring subsequent values are correlated with the previous ones
            # Random change to introduce some variation
            change = random.uniform(-3, 3)
            # Limiting the range between -5% to 15%
            next_increase = max(min(last_increase + change, 15), -5)
            monthly_increases.append(round(next_increase, 2))
            last_increase = next_increase

        performance_data[category] = monthly_increases

    return performance_data


def get_node_labels_from_ids(node_ids):
    return [n.node_data.label for n in NODES if n.node_data.id in node_ids]


def generate_color_map(kpi_list):
    colors = px.colors.qualitative.Plotly  # Or any other color palette you prefer
    return {kpi: colors[i % len(colors)] for i, kpi in enumerate(kpi_list)}

# Dummy data for demonstration purposes


def get_sample_performance_data():
    return pd.DataFrame({
        "Date": pd.date_range(start='2021-01-01', periods=30, freq='D'),
        "Operational KPI": np.random.randint(70, 100, 30),
        "Financial Metric": np.random.randint(200000, 300000, 30),
    })