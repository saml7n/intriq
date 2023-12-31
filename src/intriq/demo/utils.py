from dataclasses import Field, asdict, dataclass, field
from enum import Enum, auto
from typing import List
import numpy as np
from streamlit_agraph import Node as stNode
import streamlit as st
import time
import random
from loguru import logger
import plotly.express as px
import pandas as pd

from nodes_and_edges import EDGES, NODES, NODES_TRUNCATED, Mode

# TODO: Split into 3 classes


class MenuOption(Enum):
    OVERVIEW = 'Overview'
    CONNECT_DATA = 'Connect Data'
    ANALYSE = 'Analyse'
    TRACK = 'Track'
    ABOUT = 'About'

    def to_index(self):
        return list(MenuOption).index(self)


@dataclass
class Initiative:
    name: str
    department: str
    timeframe: str
    kpis: List[str]
    impact_on_profitability: str = None

    # for in progress initiatives
    status: str = 'Not Started'
    progress: str = '0%'
    status_color: str = '⚪️'

    # from suggestion panel
    ease_of_implementation: str = None
    description: str = None

    def to_dict(self,):
        # Converts the data class to a dictionary for the purpose of filling the tracking table. Very hacky!
        return {
            'Initiative Name': self.name,
            'Department': self.department,
            'Timeframe': self.timeframe,
            'Current Status': self.status,
            'Progress': self.progress,
            'RAG Status': self.status_color,
            'Impact': self.impact_on_profitability,
        }


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
def generate_performance_numbers(categories, option, num_months=12, l_bound=-5, u_bound=15):
    performance_data = {}
    for category in categories:
        monthly_increases = []
        # Starting with a small positive value
        last_increase = random.uniform(0, 5)
        for _ in range(num_months):
            # Ensuring subsequent values are correlated with the previous ones
            # Random change to introduce some variation
            change = random.uniform(-3, 3)
            next_increase = max(min(last_increase + change, u_bound), l_bound)
            monthly_increases.append(round(next_increase, 2))
            last_increase = next_increase

        performance_data[category] = monthly_increases

    return performance_data


def get_node_labels_from_ids(node_ids):
    return [n.node_data.label for n in NODES if n.node_data.id in node_ids]


def generate_color_map(kpi_list):
    colors = px.colors.qualitative.Plotly  # Or any other color palette you prefer
    return {kpi: colors[i % len(colors)] for i, kpi in enumerate(kpi_list)}


def wrap_in_column(func):
    def wrapper(*args, **kwargs):
        col1, col2, col3 = st.columns([1, 6, 1])
        with col2:
            func(*args, **kwargs)
    return wrapper
