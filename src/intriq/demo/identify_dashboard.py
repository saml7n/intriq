import pandas as pd
import streamlit as st
from loguru import logger
from nodes_and_edges import EDGES
from utils import Initiative, display_loading_bar, generate_color_map, generate_performance_numbers, generate_random_numbers_summing_to_100, get_node_labels_from_ids, get_nodes_and_edges, wrap_in_column
from streamlit_agraph import agraph, Config
import plotly.express as px

@wrap_in_column
def display_analysis_dashboard():
    st.subheader("Visualise your Operations")
    if st.session_state['new_data_added']:
        with st.form('new_data_added_form'):
            st.info(
                'New data sources have been added. Click to update graph', icon="ℹ️"
            )
            if st.form_submit_button("Update Graph"):
                st.session_state['new_data_added'] = False
                display_loading_bar()
                st.rerun()
    display_knowledge_graph(updated=not st.session_state['new_data_added'])


def display_knowledge_graph(updated):
    if updated:
        st.info('New value levers have been identified!')
    display_value_levers = st.toggle(
        '🔎 Value lever view',
        value=False,
        key="toggle"
    )
    graph_display_mode = 'Highlight Value Levers' if display_value_levers else 'All Nodes'
    financial_kpi_options = st.multiselect(
        'Select which financial KPIs to display:',
        [
            'Gross Profit',
            'Reported EBITDA',
            'Reported Net Income',
            'EBITDA Growth %',
            'EBITDA Margin %',
            'Net Sales'
        ],
        default='Net Sales',
        key="financial_kpi_options"
    )

    # Define or get your nodes and edges based on the selected mode
    nodes, edges = get_nodes_and_edges(
        graph_display_mode, financial_kpi_options, short_list=not updated
    )

    # Graph configuration
    config = Config(width=1500,
                    height=450,
                    directed=True,
                    nodeHighlightBehavior=True,
                    highlightColor="#F7A7A6",
                    collapsible=True,
                    physics={'enabled': False})

    # Render the graph
    selected_node_id = agraph(nodes=nodes,
                              edges=edges,
                              config=config)
    st.divider()
    if graph_display_mode == 'Highlight Value Levers':
        display_value_lever_suggestions()
    if selected_node_id:
        selected_node_label = get_node_labels_from_ids([selected_node_id])[0]
        with st.expander(f'View {selected_node_label} details'):
            display_kpi_details(selected_node_id)


def display_kpi_details(selected_node_id):
    logger.info(f"Selected node id: {selected_node_id}")
    selected_node_label = get_node_labels_from_ids([selected_node_id])[0]

    # KPI Contributions Section
    st.subheader("KPI Contributions")
    connected_node_ids = [e.source for e in EDGES if e.to == selected_node_id]
    connected_node_labels = get_node_labels_from_ids(connected_node_ids)

    data = {
        'Operational Factors': connected_node_labels,
        'Values': generate_random_numbers_summing_to_100(len(connected_node_labels))
    }
    fig = px.pie(data, names='Operational Factors', values='Values')
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    display_kpi_performance(selected_node_id, selected_node_label,
                            connected_node_labels)


def display_kpi_performance(
        selected_node_id, selected_node_label, connected_node_labels
):
    st.subheader("KPI Performance")
    color_map = generate_color_map(
        connected_node_labels + [selected_node_label]
    )

    # Multiselect checkbox for choosing connected KPIs
    st.subheader("Compare with Other KPIs")
    selected_comparison_kpis = st.multiselect(
        "Select KPIs to compare:",
        connected_node_labels,
        default=connected_node_labels[0] if connected_node_labels else None
    )

    selected_kpis = tuple([selected_node_label] +
                          selected_comparison_kpis)  # Convert list to tuple

    # Massive hack to get around the fact these are random numbers cached based on list entries and change for the same kpis when the selection is changed
    performance_data_dict = {}
    for kpi in connected_node_labels + [selected_node_label]:
        performance_data_dict[kpi] = generate_performance_numbers(
            [kpi], selected_node_id
        )[kpi]

    graph_df = pd.DataFrame(
        {k: v for k, v in performance_data_dict.items() if k in selected_kpis},
        index=pd.date_range('2022-12-01', periods=12, freq='M')
    )
    graph_df.index.name = 'Date'

    # Prepare data for Plotly Express
    long_df = graph_df.reset_index().melt(
        id_vars='Date', var_name='KPI', value_name='Value')

    # Create a line chart with Plotly Express
    fig = px.line(
        long_df,
        x='Date',
        y='Value',
        color='KPI',
        labels={'Value': f'% improvement'},
        color_discrete_map={
            k: v for k, v in color_map.items() if k in selected_kpis}
    )

    # Apply custom styling to highlight the selected node label
    fig.for_each_trace(
        lambda trace: trace.update(
            line=dict(width=4)) if trace.name == selected_node_label else (),
    )
    st.plotly_chart(fig, use_container_width=True)


def display_value_lever_suggestions():

    # Example data - replace with real data
    initiatives = [
        Initiative(
            name="Optimize Sales Funnel",
            department="Sales",
            timeframe="6 months",
            kpis=["Sales Growth", "Customer Retention"],
            ease_of_implementation="Medium",
            impact_on_profitability="$100,000",
            description="Revise the sales strategy to focus on high-margin products..."
        ),
        Initiative(
            name="Streamline Logistics",
            department="Operations",
            timeframe="3 months",
            kpis=["Operational Efficiency", "Logistics Cost Reduction"],
            ease_of_implementation="High",
            impact_on_profitability="$75,000",
            description="Implement a lean management system in the logistics department..."
        ),
        Initiative(
            name="New Marketing Campaign",
            department="Marketing",
            timeframe="2 months",
            kpis=["Market Reach", "Lead Generation"],
            ease_of_implementation="Low",
            impact_on_profitability="$50,000",
            description="Launch a targeted digital marketing campaign..."
        )
    ]

    st.markdown(
        '<h1 style="color: Red;">New Opportunities</h3>', unsafe_allow_html=True)

    for i, initiative in enumerate(initiatives):
        with st.container():
            st.subheader(initiative.name)
            cols = st.columns([2, 1])
            with cols[0]:
                st.write(f"**Department:** {initiative.department}")
                st.write(
                    f"**Ease of Implementation:** {initiative.ease_of_implementation}")
                st.write(f"**Timeframe:** {initiative.timeframe}")
                st.write(
                    f"**Estimated Financial Impact:** {initiative.impact_on_profitability}")
                st.write(f"**Description:** {initiative.description}")
                st.write("**Relevant KPIs:**")
                st.table(pd.DataFrame(initiative.kpis, columns=['KPI']))

            with cols[1]:
                # Dummy graph data
                graph_data = pd.DataFrame({
                    'Metric': ['Value Created', 'ROI', 'Efficiency Gain'],
                    'Amount': [100, 200, 150]
                })
                fig = px.bar(graph_data, x='Metric', y='Amount', text='Amount')
                fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', xaxis=dict(
                    showgrid=False), yaxis=dict(showgrid=False))
                st.plotly_chart(fig, use_container_width=True)

            add_button = st.button(
                f"Add '{initiative.name}' to your initiatives", key=f"add_button_{i}")
            if add_button:
                add_to_initiatives_list(initiative)
            st.markdown("---")  # Separator


def get_kpi_data_for_initiative(initiative):
    # Dummy function - replace with real data retrieval
    kpi_data = pd.DataFrame({
        'KPI': ['KPI 1', 'KPI 2', 'KPI 3'],
        'Importance': ['High', 'Medium', 'Low']
    })
    return kpi_data


def add_to_initiatives_list(initiative):
    if 'initiatives' not in st.session_state:
        st.session_state['initiatives'] = []
    st.session_state['initiatives'].append(initiative)
    st.success('Initiative added to the list!')
