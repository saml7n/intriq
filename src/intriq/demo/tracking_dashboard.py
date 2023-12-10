from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode, AgGridTheme
from chat import display_chatbot
import streamlit as st
import plotly.express as px
import pandas as pd
from data_dict import PORTFOLIO_COMPANIES
from utils import Initiative, generate_performance_numbers


def display_tracking_dashboard():
    st.header("Value Creation Tracking")
    col1, col2, = st.columns([2, 5])
    with col1:
        st.selectbox('Select Company', PORTFOLIO_COMPANIES, key='company')

    st.subheader("Your Initiatives")
    col1, col2, colx = st.columns([3, 3, 10])
    # Add any quick action buttons or links here
    with col1:
        st.button("➕ Add New Initiative", use_container_width=True)
    with col2:
        st.button("📄 Generate Report", use_container_width=True)

        # Example in-progress initiatives
        in_progress_initiatives = [
            Initiative("Digital Transformation for Inventory Management", "Technology", "1 year", [
                       "Inventory Accuracy", "Stock Turnover Rate"], "In Progress", "30%", "🟠"),
            Initiative("Employee Training Program for Enhanced Customer Service", "Human Resources", "9 months",
                       ["Customer Satisfaction", "Employee Skill Level"], "In Progress", "50%", "🟢"),
            Initiative("Sustainability Initiative for Eco-Friendly Packaging", "Operations", "6 months",
                       ["Waste Reduction", "Customer Eco-Satisfaction"], "In Progress", "40%", "🟢"),
            Initiative("Development of a Loyalty Program", "Marketing", "8 months", [
                       "Customer Retention Rate", "Repeat Purchase Rate"], "In Progress", "20%", "🟠"),
            Initiative("Expansion of E-commerce Platform", "E-Commerce", "1 year",
                       ["Online Sales Growth", "Website Traffic"], "In Progress", "35%", "🟠"),
            Initiative("Optimization of Supply Chain Logistics", "Supply Chain", "1.5 years", ["Logistics Cost Reduction", "Delivery Time"], "In Progress", "60%", "🟢")] + st.session_state.get('initiatives', [])

    # Convert data class objects to DataFrame for AgGrid
    data = [initiative.to_dict()
            for initiative in in_progress_initiatives]
    df = pd.DataFrame(data)

    # Customize AgGrid
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection('single')  # Enable single row selection
    grid_options = gb.build()

    # Customizing the grid's appearance
    grid_response = AgGrid(
        df,
        gridOptions=grid_options,
        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
        theme=AgGridTheme.ALPINE,
        fit_columns_on_grid_load=True)
    # Handling selection
    selected = grid_response['selected_rows']
    if selected:
        selected_row_data = selected[0]  # Assuming single row selection
        display_vci_details(selected_row_data)


def display_vci_details(vci_data):
    # Display basic VCI information with better formatting and icons
    st.subheader(f"{vci_data['Initiative Name']} Details")
    col1, col2, col3 = st.columns(3)
    col1.metric("Timeframe", vci_data["Timeframe"], "🕒")
    col2.metric("Current Status", vci_data["Current Status"], "📊")
    col3.metric("Progress", vci_data["Progress"], "🚀")

    # Sample performance data
    performance_df = pd.DataFrame(
        generate_performance_numbers(
            ['Inventory Accuracy', 'Stock Turnover Rate', 'Revenue'],
            ''
        ),
        index=pd.date_range(
            '2022-12-01', periods=12, freq='M'
        ),
    )
    performance_df.index.name = 'Date'

    # Creating a graph to show performance with Plotly Express
    fig = px.line(
        performance_df,
        labels={'value': f'% improvement'},
    )
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',
                      xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=False))

    st.plotly_chart(fig, use_container_width=True)

    # More Information section
    with st.expander("🔍 More Information & KPIs"):
        st.write("### Detailed Description")
        st.write(f"This section provides an in-depth look at the '{vci_data['Initiative Name']}' initiative, "
                 "including strategic importance, implementation steps, expected challenges, and long-term vision for this project.")

        # Display relevant KPIs with RAG status
        st.write("### Relevant KPIs and RAG Status")
        kpis = {
            "Inventory Accuracy": "🟢",
            "Stock Turnover Rate": "🟠",
        }
        for kpi, status in kpis.items():
            st.write(f"{kpi}: {status}")
        col1, col2, col3 = st.columns([3, 3, 18])
        with col1:
            st.button('➕ Add New')
        with col2:
            st.button('🔧 Edit')

    with st.expander("💬 Ask the Chatbot"):
        display_chatbot()

     # Tracking Expander
    with st.expander("📊 Tracking Progress"):
        st.write("### How Progress is Tracked")
        st.write(f"""
            The progress of the '{vci_data['Initiative Name']}' initiative is tracked using specific operational data sources and key metrics. Here are some examples:

            - **Sales Data Source:** Tracking the number of new leads and conversion rates. This data helps in assessing the effectiveness of the 'Optimize Sales Funnel' initiative.
            - **Operational Efficiency Metrics:** Utilizing data from logistics systems to measure improvements in delivery times and cost savings.
            - **Customer Feedback:** Analyzing customer feedback data to gauge the impact of the 'New Marketing Campaign' on customer satisfaction.

            **Link a Data Source:**
            - Connect relevant data sources to continuously monitor and analyze the performance of this initiative.
        """)

        if st.button("Link New Data Source", key=f"link_data_{vci_data['Initiative Name']}"):
            st.write("Link data source functionality goes here.")
            # Implement functionality to link a data source

    # Links to supporting documents with icons
    with st.expander("📄 Supporting Documents"):
        st.markdown("""
            - 📑 [Digital Transformation Project Plan](#)
            - 📋 [Inventory Management System Requirements Specification](#)
            - 📒 [Change Management and Training Guide](#)
        """)
