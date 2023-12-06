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
from data_dict import PORTFOLIO_COMPANIES
from identify_dashboard import display_analysis_dashboard
from nodes_and_edges import EDGES, NODES
from streamlit_option_menu import option_menu
from data_connection_dashboard import display_connection_dashboard
from utils import display_loading_bar, generate_random_numbers_summing_to_100, generate_performance_numbers, get_nodes_and_edges, wrap_in_column
from tracking_dashboard import display_tracking_dashboard


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
        st.session_state['show_value_levers'] = False
        st.session_state['selected_company'] = None
        st.session_state["messages"] = [
            {"role": "assistant", "content": "How can I help you?"}]
        st.session_state['new_data_added'] = False

    # Options Menu
    with st.sidebar:
        selected = option_menu(
            'intriq', [
                'Overview',
                'Connect Data',
                'Identify',
                'Track',
                'Assistant',
                'About'
            ],
            icons=[
                'house',
                'plug',
                'eye',
                'graph-up',
                'robot',
                'info-circle'
            ],
            menu_icon='intersect',
            default_index=0
        )
    if selected == 'Overview':
        overview_dashboard()
    if selected == 'Connect Data':
        display_connection_dashboard()
    if selected == 'Identify':
        display_analysis_dashboard()
    if selected == 'Track':
        display_tracking_dashboard()


@wrap_in_column
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
    graph_df = pd.DataFrame(
        generate_performance_numbers(
            PORTFOLIO_COMPANIES, option
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
    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    display_kpi_summary()
    # Portfolio company panel
    st.divider()
    st.header('Explore Portfolio')

    # Generating clickable buttons for each company in grid
    # row 1
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        for i, company in enumerate(PORTFOLIO_COMPANIES[:4]):
            with locals()[f'col{i+1}']:
                if st.button(company, key=f'{i}', use_container_width=True, type='primary' if st.session_state['selected_company'] == company else 'secondary' ):
                    st.session_state['selected_company'] = company
    # row 2
    with st.container():
        col5, col6, col7, col8 = st.columns(4)
        for i, company in enumerate(PORTFOLIO_COMPANIES[4:], start=4):
            with locals()[f'col{i+1}']:
                if st.button(company, key=f'{i}', use_container_width=True, type='primary' if st.session_state['selected_company'] == company else 'secondary'):
                    st.session_state['selected_company'] = company


def display_kpi_summary():
    st.header("KPI Overview")

    # Sample data for RAG status counts and change from last month
    rag_status = {
        "Green": {"count": 12, "change": "2"},
        "Amber": {"count": 7, "change": "-3"},
        "Red": {"count": 5, "change": "1"}
    }

    st.subheader("Initiative RAG Status")
    col1, col2, col3 = st.columns(3)

    # Display RAG status using st.metric
    col1.metric("🟢 On track",
                rag_status["Green"]["count"], rag_status["Green"]["change"])
    col2.metric("🟠 At risk",
                rag_status["Amber"]["count"], rag_status["Amber"]["change"])
    col3.metric("🔴 Requires attention",
                rag_status["Red"]["count"], rag_status["Red"]["change"])

    # Top Performing KPIs (Dummy data)
    kpi_data = {
        "KPI": ["Sales Growth", "Operational Efficiency", "Customer Satisfaction"],
        "Value": [75, 85, 90]
    }
    st.markdown('#')
    # Top Performing KPIs Section
    st.subheader("Top Performing KPIs This Month")
    fig = px.bar(kpi_data, x="KPI", y="Value", color="KPI", text="Value")
    fig.update_layout(showlegend=False, xaxis_title="",
                      yaxis_title="Value", plot_bgcolor="rgba(0,0,0,0)")
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True)


if __name__ == '__main__':
    main()
