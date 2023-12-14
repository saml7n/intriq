import streamlit as st
from loguru import logger
import time


def add_new_company():
    with st.form("new_company_form"):
        st.subheader("Add New Portfolio Company")

        # Input fields for the form
        company_name = st.text_input("Company Name")
        company_type = st.selectbox(
            "Company Type", ["Public", "Private", "Startup", "Financial Institution"])
        sector = st.text_input("Sector")
        valuation = st.number_input(
            "Valuation (in $ millions)", min_value=0.0, step=1.0)
        key_kpis = st.text_area("Key KPIs (comma-separated)")
        strategic_goals = st.text_area("Strategic Goals")

        uploaded_file = st.file_uploader(
            "Upload any initial documents here",
            help="Various File formats are supported",
            accept_multiple_files=True
        )

        if uploaded_file:
            logger.info("Files uploaded successfully!")
            with st.spinner("Uploading data..."):
                time.sleep(2)
            st.success("Files uploaded successfully!")
            st.session_state['data_sources'][uploaded_file.name] = 'file-earmark'
            st.rerun()

        # Form submission button
        submitted = st.form_submit_button("Add Company")
        if submitted:
            # Processing after form submission
            st.success(f"Company '{company_name}' added successfully!")
            # Here you can add the code to store these details, e.g., in a database or a file
            st.session_state['portfolio_companies'].append(company_name)
            st.rerun()
