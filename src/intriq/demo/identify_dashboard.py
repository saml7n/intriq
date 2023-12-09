import pandas as pd
import streamlit as st
from loguru import logger
from data_dict import PORTFOLIO_COMPANIES
from nodes_and_edges import EDGES, FINANCIAL_METRICS, NODES, NODES_TRUNCATED, Mode
from utils import Initiative, display_loading_bar, generate_color_map, generate_performance_numbers, generate_random_numbers_summing_to_100, get_node_labels_from_ids, wrap_in_column
from streamlit_agraph import agraph, Config
import plotly.express as px


@wrap_in_column
def display_analysis_dashboard():
    col1, col2, = st.columns([1, 4])
    with col1:
        st.selectbox('Select Company', PORTFOLIO_COMPANIES)
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
                st.rerun()
    display_knowledge_graph(updated=not st.session_state['new_data_added'])


def display_knowledge_graph(updated):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("##")
        display_value_levers = st.toggle(
            '🔍 Value Lever View',
            value=False,
            key="toggle"
        )
        graph_display_mode = 'Highlight Value Levers' if display_value_levers else 'All Nodes'
    with col2:
        financial_kpi_options = st.multiselect(
            'Select which financial KPIs to display:',
            FINANCIAL_METRICS,
            default=FINANCIAL_METRICS[0],
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
                    physics={'enabled': False},
                    hierarchical={'enabled': True},
                    nodeSpacing=5000)

    # Render the graph
    selected_node_id = agraph(nodes=nodes,
                              edges=edges,
                              config=config)
    st.divider()
    if selected_node_id:
        selected_node_label = get_node_labels_from_ids([selected_node_id])[0]
        with st.expander(f'View {selected_node_label} details'):
            display_kpi_details(selected_node_id)
    if graph_display_mode == 'Highlight Value Levers':
        display_value_lever_suggestions()


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
            name="Enhancing In-Store Experience",
            department="Retail Operations",
            timeframe="6 months",
            kpis=["Customer Satisfaction",
                  "In-Store Sales Growth", "Repeat Customer Rate"],
            ease_of_implementation="Medium",
            impact_on_profitability="$120,000",
            description="Redesign and enhance the in-store experience to increase customer engagement and sales. This includes optimizing store layouts, improving product placements, and implementing interactive displays. The initiative aims to convert foot traffic into higher sales and repeat customers."
        ),
        Initiative(
            name="Optimizing Online Sales Platform",
            department="E-Commerce",
            timeframe="4 months",
            kpis=["Online Sales Conversion Rate",
                  "Website Traffic", "Average Order Value"],
            ease_of_implementation="Medium",
            impact_on_profitability="$95,000",
            description="Improve the online shopping experience by optimizing the e-commerce platform. Enhancements include website redesign for user-friendliness, personalized product recommendations, and streamlined checkout processes. The goal is to boost online sales conversions and customer retention."
        )

    ]

    st.markdown("""
            <div style="padding: 1rem; background-color: #ffcccc; border-radius: 0.5rem; text-align: center;">
                <h4 style="margin: 0; color: #cc0000;">⚠️ New Value Levers Identified! ⚠️</h4>
            </div>
            """, unsafe_allow_html=True)

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
                display_graph_for_initiative(initiative.name)

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


def get_nodes_and_edges(mode, financial_kpi_options=None, short_list=True):
    mode = Mode(mode)
    logger.info(f"Mode: {mode}")
    # Incredibly hacky way of doing this, but it works for now
    return_nodes = []
    nodes = NODES_TRUNCATED if short_list else NODES
    for node in nodes:
        if 'FK' in node.node_data.id:
            if node.node_data.label not in financial_kpi_options:
                continue
        if mode == Mode.ALL_NODES:
            return_nodes.append(node.node_data)
        elif mode in node.modes:
            return_nodes.append(node.node_data)

    return_node_ids = [n.id for n in return_nodes]
    return_edges = [
        e for e in EDGES if e.source in return_node_ids and e.to in return_node_ids
    ]
    return return_nodes, return_edges


# Function to display graph based on selected initiative
def display_graph_for_initiative(initiative_name):
    if initiative_name == "Enhancing In-Store Experience":
        graph_data = pd.DataFrame({
            'Metric': ['In-Store Sales Growth', 'Customer Satisfaction Score', 'Repeat Customer Rate'],
            'Impact (%)': [50, 15, 35]  # Dummy values
        })
    elif initiative_name == "Optimizing Online Sales Platform":
        graph_data = pd.DataFrame({
            'Metric': ['Online Conversion Rate', 'Average Order Value', 'Website Traffic Growth'],
            'Impact (%)': [30, 45, 25]  # Dummy values
        })
    else:
        return

    fig = px.bar(graph_data, x='Metric', y='Impact (%)', text='Impact (%)')
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', xaxis=dict(
        showgrid=False), yaxis=dict(showgrid=False))
    st.plotly_chart(fig, use_container_width=True)
