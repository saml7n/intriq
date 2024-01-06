import streamlit as st
from loguru import logger
from components.playbook import display_playbook_dashboard
from components.knowledge_graph import display_knowledge_graph
from nodes_and_edges import EDGES, FINANCIAL_METRICS, NODES, NODES_TRUNCATED
from utils import display_loading_bar, generate_color_map, generate_performance_numbers, generate_random_numbers_summing_to_100, get_node_labels_from_ids, wrap_in_column
from streamlit_agraph import agraph


@wrap_in_column
def display_analysis_dashboard():
    st.title("Operational and Financial KPI Analysis")

    col1, col2, = st.columns([1, 2])
    with col1:
        st.selectbox('Select Company', st.session_state['portfolio_companies'])

    st.subheader("Process Map")
    st.write(
        "The process map below shows the relations between operational processes and financial metrics for your company. Click on the nodes to see more information about each KPI."
    )
    if st.session_state['new_data_added']:
        with st.form('new_data_added_form'):
            st.info(
                'New data sources have been added. Click to update graph', icon="ℹ️"
            )
            if st.form_submit_button("Update Graph"):
                st.session_state['new_data_added'] = False
                display_loading_bar()
                st.experimental_rerun()
    display_knowledge_graph(updated=not st.session_state['new_data_added'])
