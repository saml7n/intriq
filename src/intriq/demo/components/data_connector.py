import streamlit as st
from loguru import logger
import time


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
