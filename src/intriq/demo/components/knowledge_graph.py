import pandas as pd
import streamlit as st
from loguru import logger
from nodes_and_edges import EDGES, FINANCIAL_METRICS, NODES, NODES_TRUNCATED, PRIMARY_KPIS, Mode
from utils import Initiative, generate_color_map, generate_performance_numbers, generate_random_numbers_summing_to_100, get_node_labels_from_ids
from streamlit_agraph import agraph, Config
import plotly.express as px

DUMMY_DATA_SOURCES = {
    "PK1": [
        {
            "name": "Annual Financial Report",
            "extraction_method": "Text Analysis",
            "last_updated": "2023-09-01",
            "quality_score": "92%",
            "data_preview": pd.DataFrame({
                    "Metric": ["Revenue", "Cost of Goods Sold", "Operating Expenses"],
                    "2022": [1500000, 500000, 300000],
                    "2023": [1700000, 550000, 350000]
            }),
            "notes": "This report provides a comprehensive overview of the annual financial performance."
        }, {
            "name": "Sales Database",
            "extraction_method": "API Integration",
            "last_updated": "2023-08-15",
            "quality_score": "88%",
            "data_preview": pd.DataFrame({
                "Month": ["Jan", "Feb", "Mar", "Apr"],
                "Sales": [120000, 135000, 140000, 150000],
                "Expenses": [30000, 35000, 33000, 37000]
            }),
            "notes": "Sales data provides insights into monthly performance and expenditure."
        }, {
            "name": "Employee Satisfaction Survey",
            "extraction_method": "Manual Entry",
            "last_updated": "2023-07-20",
            "quality_score": "95%",
            "data_preview": pd.DataFrame({
                "Department": ["Sales", "HR", "Tech", "Admin"],
                "Satisfaction Score": [85, 90, 88, 82]
            }),
            "notes": "The survey highlights employee satisfaction across different departments."
        }, {
            "name": "Customer Feedback Data",
            "extraction_method": "Feedback Form",
            "last_updated": "2023-06-30",
            "quality_score": "90%",
            "data_preview": pd.DataFrame({
                "Feedback Category": ["Product Quality", "Delivery Time", "Customer Service", "Pricing"],
                "Positive Responses": [200, 180, 230, 150],
                "Negative Responses": [50, 70, 40, 80]
            }),
            "notes": "Customer feedback provides valuable insights into various aspects of business operations and product offerings."
        }, {
            "name": "Market Analysis Report",
            "extraction_method": "Third-Party Analysis",
            "last_updated": "2023-05-10",
            "quality_score": "89%",
            "data_preview": pd.DataFrame({
                "Market Segment": ["Retail", "Technology", "Healthcare", "Finance"],
                "Growth Rate (%)": [5.2, 7.8, 4.6, 6.1]
            }),
            "notes": "This report provides a breakdown of growth rates in different market segments."
        }],
    "PK2": [{
        "name": "Sales Database",
        "extraction_method": "API Integration",
        "last_updated": "2023-08-15",
        "quality_score": "85%",
        "data_preview": pd.DataFrame({
            "Month": ["Jan", "Feb", "Mar", "Apr"],
            "Sales": [120000, 135000, 140000, 150000],
            "Expenses": [30000, 35000, 33000, 37000]
        })
    }],
    # Additional data sources
    "PK3": [{
        "name": "Customer Feedback System",
        "extraction_method": "Survey Analysis",
        "last_updated": "2023-08-30",
        "quality_score": "88%",
        "data_preview": pd.DataFrame({
            "Month": ["Jan", "Feb", "Mar", "Apr"],
            "Customer Satisfaction": [92, 89, 93, 90],
            "Net Promoter Score": [40, 42, 45, 43]
        })
    }],
}


def display_knowledge_graph(updated):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("##")
        display_value_levers = st.toggle(
            '🔍 New Value Levers',
            value=False,
            key="toggle"
        )
        graph_display_mode = 'Highlight Value Levers' if display_value_levers else 'All Nodes'
    with col2:
        financial_kpi_option = st.selectbox(
            'Select which financial KPI to display:',
            PRIMARY_KPIS,
            key="financial_kpi_options"
        )

    # Define or get your nodes and edges based on the selected mode
    nodes, edges = get_nodes_and_edges(
        graph_display_mode, financial_kpi_option, short_list=not updated
    )

    # Graph configuration
    config = Config(
        height=800,
        physics=False,
        directed=True,
    )

    # Render the graph
    selected_node_id = agraph(nodes=nodes,
                              edges=edges,
                              config=config)
    if selected_node_id:
        display_kpi_details(selected_node_id)
    if graph_display_mode == 'Highlight Value Levers':
        display_value_lever_suggestions()


def display_kpi_details(selected_node_id):
    logger.info(f"Selected node id: {selected_node_id}")
    selected_node_label = get_node_labels_from_ids([selected_node_id])[0]
    connected_node_ids = [
        e.source for e in EDGES if e.to == selected_node_id]
    connected_node_labels = get_node_labels_from_ids(connected_node_ids)

    # KPI Performance Analysis
    display_kpi_performance(selected_node_id, selected_node_label,
                            connected_node_labels)

    # st.divider()

    # KPI Contributions Section
    st.subheader(f"{selected_node_label} KPI Contributions")
    data = {
        'Operational Factors': connected_node_labels,
        'Impact Values': generate_random_numbers_summing_to_100(len(connected_node_labels))
    }
    fig = px.pie(data, names='Operational Factors', values='Impact Values')
    st.plotly_chart(fig, use_container_width=True)

    # Data Source Insights
    if selected_node_id.startswith("PK"):
        st.subheader("Data Source Insights")
        display_data_source_insights(DUMMY_DATA_SOURCES, selected_node_id)


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


def display_data_source_insights(data_sources, selected_node_id):
    if selected_node_id in data_sources:
        # Create tabs for each data source
        node_data_sources = data_sources[selected_node_id]
        tabs = st.tabs(
            [source['name'] for source in node_data_sources]
        )

        for tab, data_source in zip(tabs, node_data_sources):
            with tab:
                # Displaying the title and basic info in a visually appealing layout
                st.markdown(f"### {data_source['name']}")
                col1, col2, col3 = st.columns(3)
                col1.metric("Extraction Method",
                            data_source['extraction_method'])
                col2.metric("Last Updated", data_source['last_updated'])
                col3.metric("Quality Score", data_source['quality_score'])

                # Displaying the data preview with Plotly charts
                if 'data_preview' in data_source:
                    df = data_source['data_preview']
                    fig = px.bar(df, x=df.columns[0], y=df.columns[1:])
                    st.plotly_chart(fig, use_container_width=True)

                # Additional info or notes
                if 'notes' in data_source:
                    st.write(data_source['notes'])

                st.markdown("""
                    - 📑 [Download source](#)
                """)


def display_value_lever_suggestions():
    # Example data - replace with real data
    initiatives = [
        Initiative(
            name="Retail Collections Efficiency Program",
            department="Operations",
            timeframe="8 months",
            kpis=["Retail Collections", "Workforce Efficiency",
                  "Employee Satisfaction"],
            ease_of_implementation="High",
            impact_on_profitability="$100,000",
            description="Implement a streamlined process for handling retail collections to improve operational efficiency. This includes training employees on efficient collection methods, introducing technology solutions to reduce time spent on collections, and restructuring team roles for better resource allocation. The goal is to reduce the workload on employees dealing with returns and collections, thereby increasing workforce efficiency and employee satisfaction."
        ),
        Initiative(
            name="Optimized Fitting Room Experience",
            department="Retail Operations",
            timeframe="1 year",
            kpis=["Fitting Room Footfall",
                  "Store Footfall", "Retail Sales Growth"],
            ease_of_implementation="Medium",
            impact_on_profitability="$150,000",
            description="Enhance the fitting room experience to increase store footfall conversion into sales. This initiative includes revamping the fitting room area with better lighting, quicker service, and digital features like smart mirrors. The aim is to make fitting rooms a pivotal point in the customer's shopping journey, thereby increasing retail sales."
        )

    ]

    st.markdown("""
            <div style="padding: 1rem; background-color: #6bc661; border-radius: 0.5rem; text-align: center;">
                <h4 style="margin: 0; color: #333;">New Value Levers Identified!</h4>
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


def add_to_initiatives_list(initiative):
    if 'initiatives' not in st.session_state:
        st.session_state['initiatives'] = []
    st.session_state['initiatives'].append(initiative)
    st.success('Initiative added to the list!')


def get_nodes_and_edges(mode, financial_kpi_option=None, short_list=True):
    mode = Mode(mode)
    logger.info(f"Mode: {mode}")
    # Incredibly hacky way of doing this, but it works for now
    return_nodes = []
    nodes = NODES_TRUNCATED if short_list else NODES
    root_node = [n.node_data for n in nodes if n.node_data.label ==
                 financial_kpi_option][0]
    for node in nodes:
        if 'PK' in node.node_data.id:
            if node.node_data.label != financial_kpi_option:
                continue
        if mode == Mode.ALL_NODES:
            return_nodes.append(node.node_data)
        elif mode in node.modes:
            return_nodes.append(node.node_data)

    logger.info(f'root node: {root_node.label}')
    logger.info([n.label for n in return_nodes])
    connected_nodes, _ = find_connected_elements(
        root_node.id, EDGES, return_nodes)

    connected_node_ids = [node.id for node in connected_nodes]

    connected_edges = [
        edge for edge in EDGES if edge.source in connected_node_ids and edge.to in connected_node_ids
    ]

    return connected_nodes, connected_edges


# Function to display graph based on selected initiative
def display_graph_for_initiative(initiative_name):
    if initiative_name == "Retail Collections Efficiency Program":
        graph_data = pd.DataFrame({
            'Metric': ['Retail Collections', 'Workforce Efficiency', 'Employee Satisfaction'],
            'Impact (%)': [50, 15, 35]  # Dummy values
        })
    elif initiative_name == "Optimized Fitting Room Experience":
        graph_data = pd.DataFrame({
            'Metric': ['Fitting Room Footfall', 'Store Footfall', 'Retail Sales Growth'],
            'Impact (%)': [30, 45, 25]  # Dummy values
        })
    else:
        return

    fig = px.bar(graph_data, x='Metric', y='Impact (%)', text='Impact (%)')
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', xaxis=dict(
        showgrid=False), yaxis=dict(showgrid=False))
    st.plotly_chart(fig, use_container_width=True)


def find_connected_elements(node_id, edges, permitted_nodes, visited=None, connected_nodes=None, connected_edges=None):
    if visited is None:
        visited = set()
    if connected_nodes is None:
        connected_nodes = []
    if connected_edges is None:
        connected_edges = []

    # Mark the current node as visited
    visited.add(node_id)

    # Extract permitted node IDs for comparison
    permitted_node_ids = [node.id for node in permitted_nodes]

    # Iterate over edges to find connections
    for edge in edges:
        if edge.source == node_id or edge.to == node_id:
            # Determine the connected node ID
            connected_node_id = edge.to if edge.source == node_id else edge.source

            # Check if connected node is permitted and not already added
            if connected_node_id in permitted_node_ids:
                connected_node = next(
                    (node for node in permitted_nodes if node.id == connected_node_id), None)

                if connected_node and connected_node not in connected_nodes:
                    connected_nodes.append(connected_node)
                    connected_edges.append(edge)

                    # Recursively find further connections if the node is unvisited
                    if connected_node_id not in visited:
                        find_connected_elements(
                            connected_node_id, edges, permitted_nodes, visited, connected_nodes, connected_edges)

    return connected_nodes, connected_edges
