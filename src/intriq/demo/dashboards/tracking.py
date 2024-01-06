import numpy as np
from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode, AgGridTheme
from components.chat import display_chatbot
import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime
from utils import Initiative, generate_performance_numbers


def display_tracking_dashboard():
    st.header("Value Creation Tracking")
    col1, col2, = st.columns([2, 5])
    with col1:
        st.selectbox('Select Company',
                     st.session_state['portfolio_companies'], key='company')
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
                       "Inventory Accuracy", "Stock Turnover Rate"], "$1.6M", "In Progress", "30%", "🟠"),
            Initiative("Employee Training Program for Enhanced Customer Service", "Human Resources", "9 months",
                       ["Customer Satisfaction", "Employee Skill Level"], "$0.3M", "In Progress", "50%", "🟢"),
            Initiative("Sustainability Initiative for Eco-Friendly Packaging", "Operations", "6 months",
                       ["Waste Reduction", "Customer Eco-Satisfaction"], "$0.8M", "In Progress", "40%", "🟢"),
            Initiative("Development of a Loyalty Program", "Marketing", "8 months", [
                       "Customer Retention Rate", "Repeat Purchase Rate"], "$1.9M", "In Progress", "20%", "🟠"),
            Initiative("Expansion of E-commerce Platform", "E-Commerce", "1 year",
                       ["Online Sales Growth", "Website Traffic"], "$0.7M", "In Progress", "35%", "🟠",),
            Initiative("Optimization of Supply Chain Logistics", "Supply Chain", "1.5 years", ["Logistics Cost Reduction", "Delivery Time"],  "$0.3M", "In Progress", "60%", "🟢")] + st.session_state.get('initiatives', [])

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

    impact_df, performance_df = generate_financial_data()

    show_absolute = st.toggle(
        "Show financial impact",
        key='graph_type',
    )

    # Modify performance data based on selected graph type

    if show_absolute:
        graph_df = impact_df
        # Adjust the label as needed
        y_label = 'Impact on Revenue ($ in thousands)'
    else:
        # For % change, use the existing performance data
        graph_df = performance_df
        y_label = '% Change'

    # Plot the graph
    fig = px.line(
        graph_df,
        labels={'value': y_label},
        markers=True
    )

    initiative_start_date = pd.to_datetime('2023-12-01')
    fig.add_vline(x=initiative_start_date, line_dash="dash")

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
    )

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
            latest_percentage_change = int(performance_df[kpi].iloc[-1])
            latest_dollar_impact = impact_df[kpi].iloc[-1]

            col1, col2, col3, col4 = st.columns([1, 1, 1, 4])
            with col1:
                st.markdown(f"<b>{kpi}: {status}</b>", unsafe_allow_html=True)
            with col2:
                st.markdown(
                    f"<b>% Change:</b> {latest_percentage_change}%", unsafe_allow_html=True)
            with col3:
                st.markdown(
                    f"<b>$ Impact:</b> {latest_dollar_impact}", unsafe_allow_html=True)

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


def generate_financial_data():
    # Parameters for financial impact
    start_inventory_acc_impact, end_inventory_acc_impact, fluctuation_inventory_acc_impact = 300, 580, 50
    start_stock_turnover_impact, end_stock_turnover_impact, fluctuation_stock_turnover_impact = 200, 400, 30

    start_inventory_acc_pct, end_inventory_acc_pct, fluctuation_inventory_acc_pct = 5, 8, 1
    start_stock_turnover_pct, end_stock_turnover_pct, fluctuation_stock_turnover_pct = 3, 6, 1
    start_revenue_pct, end_revenue_pct, fluctuation_revenue_pct = 2, 4, 5

    # Generate financial impact data
    inventory_accuracy_impact = generate_realistic_impact(
        start_inventory_acc_impact, end_inventory_acc_impact, fluctuation_inventory_acc_impact, 'investory_accuracy')
    stock_turnover_rate_impact = generate_realistic_impact(
        start_stock_turnover_impact, end_stock_turnover_impact, fluctuation_stock_turnover_impact, 'stock_turnover_rate')

    # Generate percentage change data
    inventory_accuracy_pct = generate_realistic_impact(
        start_inventory_acc_pct, end_inventory_acc_pct, fluctuation_inventory_acc_pct, 'inventory_accuracy')
    stock_turnover_rate_pct = generate_realistic_impact(
        start_stock_turnover_pct, end_stock_turnover_pct, fluctuation_stock_turnover_pct, 'stock_turnover_rate')
    revenue_pct = generate_realistic_impact(
        start_revenue_pct, end_revenue_pct, fluctuation_revenue_pct, 'revenue')

    impact_df = pd.DataFrame(
        {
            'Inventory Accuracy': inventory_accuracy_impact,
            'Stock Turnover Rate': stock_turnover_rate_impact
        },
        index=[*pd.date_range('2023-06-01', periods=6, freq='M'), *pd.date_range('2023-12-01', periods=3, freq='Q')])

    pct_df = pd.DataFrame({
        'Inventory Accuracy': inventory_accuracy_pct,
        'Stock Turnover Rate': stock_turnover_rate_pct,
        'Revenue': revenue_pct,
    }, index=impact_df.index)

    return impact_df, pct_df


@st.cache_data(ttl=60*60*24)
def generate_realistic_impact(start_value, end_value, fluctuation, key):
    return np.round([*np.linspace(start_value, end_value*0.5, 6) + np.random.uniform(-fluctuation, fluctuation, 6), *np.linspace(end_value*0.5, end_value, 3) + np.random.uniform(-fluctuation*2, fluctuation*2, 3)], 2)
