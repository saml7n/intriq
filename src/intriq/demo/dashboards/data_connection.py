from datetime import datetime
from streamlit_option_menu import option_menu
import streamlit as st
from loguru import logger
import time
from components.data_connector import add_new_data_source
from utils import wrap_in_column


@wrap_in_column
def display_connection_dashboard():
    col1, col2, = st.columns([2, 4])
    with col1:
        st.selectbox('Select Company', st.session_state['portfolio_companies'])
    ds_selection = option_menu(
        'Connect your Data Sources', [
            *list(st.session_state['data_sources'].keys()), 'Add New'
        ],
        icons=[
            *list(st.session_state['data_sources'].values()), 'plus-circle'],
        menu_icon='database-add',
        default_index=0,
        orientation='horizontal'
    )

    if ds_selection == 'Sage':
        display_sage_connection_info()
    if ds_selection == 'Add New':
        with st.expander("New connection"):
            add_new_data_source()


def display_sage_connection_info():
    # Dummy data for the Sage connection
    sage_connection_data = {
        "Connection Status": "Connected",
        "Connected Since": datetime(2023, 1, 1, 10, 0, 0).strftime("%Y-%m-%d %H:%M:%S"),
        "Last Synced": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Data Sync Frequency": "Daily"
    }

    st.write("### Sage Connection Details")

    # Display the connection details
    for key, value in sage_connection_data.items():
        st.text(f"{key}: {value}")

    # Button to disconnect
    if st.button("Disconnect Sage Connection"):
        st.session_state['sage_connected'] = False
        st.success("Sage connection has been disconnected.")
