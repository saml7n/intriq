from datetime import datetime
from streamlit_option_menu import option_menu
import streamlit as st
from loguru import logger
import time
from data_dict import PORTFOLIO_COMPANIES
from utils import wrap_in_column


@wrap_in_column
def display_connection_dashboard():
    col1, col2, = st.columns([1, 4])
    with col1:
        st.selectbox('Select Company', PORTFOLIO_COMPANIES)
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


def add_new_data_source():
    source_type = st.selectbox('Select data source type', [
        'Sage',
        'SAP',
        'SalesForce',
        'Oracle',
        'QuickBooks',
        'Xero',
        'File upload'
    ])
    if source_type == 'File upload':
        st.radio('Select data type', ['Financial', 'Operational'])

        uploaded_file = st.file_uploader(
            "Add data files here",
            help="Various File formats are supported",
        )
        if uploaded_file:
            logger.info("Files uploaded successfully!")
            with st.spinner("Uploading data..."):
                time.sleep(2)
            st.success("Files uploaded successfully!")
            st.session_state['data_sources'][uploaded_file.name] = 'file-earmark'
            st.session_state['new_data_added'] = True
            st.rerun()
