import json
import random
import ssl
import pandas as pd
import streamlit as st
from dotenv import main
import nltk
from loguru import logger
from streamlit_agraph import agraph, Config
import plotly.express as px
from company_dashboard import display_company_dashboard
from nodes_and_edges import EDGES, NODES
from streamlit_option_menu import option_menu

from utils import display_loading_bar, generate_random_numbers_summing_to_100, generate_performance_numbers, get_nodes_and_edges


main.load_dotenv()
_PARTITION_STRATEGY = 'hi_res'
_PARTITION_MODEL_NAME = 'yolox'
_OPEN_AI_MODEL_NAME = 'gpt-3.5-turbo-0613'

# Download necessary NLTK data
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('stopwords')


def clear_submit():
    """
    Clear the Submit Button State
    Returns:

    """
    st.session_state["submit"] = False


def main():
    st.set_page_config(
        page_title="intriq data diagnostics",
        page_icon="🤖"
    )

    # Initialize 'current_page' in session state if not already set
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'upload_data'
        st.session_state['data_sources'] = {'Sage': 'cash-coin'}
        st.session_state['selected_company'] = None
        st.session_state["messages"] = [
            {"role": "assistant", "content": "How can I help you?"}]

    # Options Menu
    with st.sidebar:
        selected = option_menu('intriq', ["Overview", 'Assistant', 'About'],
                               icons=['house', 'robot', 'info-circle'], menu_icon='intersect', default_index=0)
    if selected == 'Overview':
        overview_dashboard()


def overview_dashboard():
    # Header
    st.title('Welcome to intriq')
    st.subheader('*One tool for all your transformation diagnostic needs*')
    st.divider()
    st.header('Portfolio Overview')
    option = st.selectbox(
        'Select metric',
        ('EBITDA', 'Costs of Goods Sold', 'Revenue')
    )
    store_names = ['Fortnum & Mason', 'Lakeland', 'Boux Avenue',
                   'Crew Clothing', 'Paperchase', 'Whistles', 'Hobbs London', 'Clarks']
    graph_df = pd.DataFrame(
        generate_performance_numbers(
            store_names, option
        ),
        index=pd.date_range(
            '2022-12-01', periods=12, freq='M'
        )
    )
    graph_df.index.name = 'Date'
    fig = px.line(
        graph_df,
        labels={'value': f'{option} (% improvement)'}
    )

    # Display the line chart
    st.plotly_chart(fig)

    # Portfolio company panel
    st.divider()
    st.header('Explore Portfolio')

    # Generating clickable buttons for each company in grid
    # row 1
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        for i, company in enumerate(store_names[:4]):
            with locals()[f'col{i+1}']:
                if st.button(company, key=f'{i}', use_container_width=True):
                    st.session_state['selected_company'] = company
    # row 2
    with st.container():
        col5, col6, col7, col8 = st.columns(4)
        for i, company in enumerate(store_names[4:], start=4):
            with locals()[f'col{i+1}']:
                if st.button(company, key=f'{i}', use_container_width=True):
                    st.session_state['selected_company'] = company

    # Show company dashboard if company clicked
    if st.session_state['selected_company']:
        with st.container():
            display_company_dashboard()


if __name__ == '__main__':
    main()
