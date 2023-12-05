import pandas as pd
import streamlit as st
from loguru import logger
from chat import display_chatbot
from nodes_and_edges import EDGES, NODES
from utils import display_loading_bar, generate_color_map, generate_performance_numbers, generate_random_numbers_summing_to_100, get_node_labels_from_ids, get_nodes_and_edges, get_sample_performance_data
from streamlit_option_menu import option_menu
from streamlit_agraph import agraph, Config
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode


def display_company_dashboard():
    tab1, tab2, tab3 = st.tabs(
        [
            "📂 Connect Data",
            "🗺️ View Data Map",
            "🎚️ Value Lever Control Center"
        ]
    )

    with tab1:
        connect_data_section()

    with tab2:
        view_graph_section()

    with tab3:
        control_center_section()


def connect_data_section():
    ds_selection = option_menu(
        'Connect your Data Sources', [
            *list(st.session_state['data_sources'].keys()), 'Add New'
        ],
        icons=[
            *list(st.session_state['data_sources'].values()), 'plus-circle'],
        menu_icon='database-add',
        default_index=-1,
        orientation='horizontal'
    )
    if ds_selection == 'Add New':
        with st.expander("New connection"):
            add_new_data_source()


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
            st.success("Files uploaded successfully!")
            display_loading_bar()
            st.button("Rerun analysis")
            st.session_state['data_sources'][uploaded_file.name] = 'file-earmark'


def view_graph_section():
    st.subheader("Visualise your Data Knowledge Graph")

    # Using columns to organize the layout
    col1, col2 = st.columns(2)

    # Radio buttons for selecting the graph display mode in the first column
    with col1:
        graph_display_mode = st.radio(
            "Select Graph Display Mode:",
            ('All Nodes', 'Highlight Value Levers', 'Financial KPIs Only'),
            key="graph_display_mode",
        )

    # Multi-select for financial KPIs in the second column
    with col2:
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
        graph_display_mode, financial_kpi_options
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
    if selected_node_id:
        selected_node_label = get_node_labels_from_ids([selected_node_id])[0]
        with st.expander(f'View {selected_node_label} details'):
            display_kpi_details(selected_node_id)


def control_center_section():
    st.write("### Value Creation Initiatives in Progress")

    # Example data structure - replace with your actual data retrieval logic
    data = [
        {"Initiative Name": "Optimize Sales Funnel", "Department": "Sales", "Timeframe": "6 months",
            "Current Status": "On Track", "Progress": "40%", "RAG Status": "🟢"},
        {"Initiative Name": "Streamline Logistics", "Department": "Operations", "Timeframe": "3 months",
            "Current Status": "Minor Delays", "Progress": "25%", "RAG Status": "🟠"},
        {"Initiative Name": "New Marketing Campaign", "Department": "Marketing", "Timeframe": "2 months",
            "Current Status": "Behind Schedule", "Progress": "10%", "RAG Status": "🔴"}
    ]

    df = pd.DataFrame(data)

    # Set up AgGrid
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection('single')  # Enable single row selection
    grid_options = gb.build()

    grid_response = AgGrid(df, gridOptions=grid_options,
                           fit_columns_on_grid_load=True, columns_auto_size_mode=ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW)

    selected = grid_response['selected_rows']
    if selected:
        selected_row_data = selected[0]  # Assuming single row selection
        with st.container():
            display_vci_details(selected_row_data)


def display_vci_details(vci_data):
    # Display basic VCI information with better formatting and icons
    st.subheader(f"{vci_data['Initiative Name']} Details")
    col1, col2, col3 = st.columns(3)
    col1.metric("Timeframe", vci_data["Timeframe"], "🕒")
    col2.metric("Current Status", vci_data["Current Status"], "📊")
    col3.metric("Progress", vci_data["Progress"], "🚀")

    # Sample performance data
    performance_data = get_sample_performance_data()

    # Creating a graph to show performance with Plotly Express
    fig = px.line(performance_data, x='Date')
    fig.add_scatter(
        x=performance_data['Date'], y=performance_data['Operational KPI'], mode='lines', name='Operational KPI')
    fig.add_scatter(
        x=performance_data['Date'], y=performance_data['Financial Metric'], mode='lines', name='Financial Metric')
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',
                      xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=False))

    st.plotly_chart(fig, use_container_width=True)

    # More Information section
    with st.expander("🔍 More Information & KPIs"):
        st.write("### Detailed Description")
        st.write("This section provides an in-depth look at the 'Optimize Sales Funnel' initiative, "
                 "including strategic importance, implementation steps, expected challenges, and long-term vision for this project.")

        # Display relevant KPIs with RAG status
        st.write("### Relevant KPIs and RAG Status")
        kpis = {
            "Customer Conversion Rate": "🟢",
            "Lead Generation": "🟠",
            "Customer Churn Rate": "🔴"
        }
        for kpi, status in kpis.items():
            st.write(f"{kpi}: {status}")

    with st.expander("💬 Ask the Chatbot"):
        display_chatbot()

    # Links to supporting documents with icons
    with st.expander("📄 Supporting Documents"):
        st.markdown("""
            - 📑 [Project Plan](#)
            - 📊 [Budget Report](#)
            - 📈 [Market Analysis](#)
        """)


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

    st.divider()

    identify_value_levers(selected_node_label, connected_node_labels)


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


def identify_value_levers(selected_node_label, connected_node_labels):
    if st.button('Identify Value Levers'):
        display_loading_bar()
        st.write('Analysis complete!')
        st.session_state['show_value_levers'] = True

    if st.session_state['show_value_levers']:
        # Example data - replace with real data
        example_data = [
            {
                "Department": "Sales",
                "Ease of Implementation": "Medium",
                "Projected Financial Impact": "$100,000",
                "Timeframe": "6 months",
                "Description": "Revise the sales strategy to focus on high-margin products. This includes retraining the sales team, revising sales scripts, and targeting more profitable market segments. Expected to increase sales conversion rates by 15%."
            },
            {
                "Department": "Operations",
                "Ease of Implementation": "High",
                "Projected Financial Impact": "$75,000",
                "Timeframe": "3 months",
                "Description": "Implement a lean management system in the logistics department to streamline operations. This will involve adopting just-in-time inventory practices and automating parts of the supply chain, aiming to reduce delivery times by 30%."
            },
            {
                "Department": "Marketing",
                "Ease of Implementation": "Low",
                "Projected Financial Impact": "$50,000",
                "Timeframe": "1 month",
                "Description": "Launch a targeted digital marketing campaign focusing on retargeting previous customers and engaging new leads through social media. Utilizing data analytics for precise targeting, this campaign aims to boost customer engagement rates by 25%."
            }
        ]

# Display in a grid
        for index, data in enumerate(example_data):
            with st.container():
                cols = st.columns([1, 2, 1, 2, 1])
                with cols[1]:
                    st.markdown(f"**Department:**\n{data['Department']}")
                    st.markdown(f"**Ease:**\n{data['Ease of Implementation']}")
                with cols[3]:
                    st.markdown(
                        f"**Impact:**\n{data['Projected Financial Impact']}")
                    st.markdown(f"**Timeframe:**\n{data['Timeframe']}")

                with cols[0], cols[2], cols[4]:  # Empty columns for spacing
                    st.write("")

                st.markdown(f"**Description:**\n{data['Description']}")

                add_button = st.button(
                    f"Add '{data['Department']}' Lever", key=f"add_button_{index}")
                logger.info(f"Button is added {add_button}")
                if add_button:
                    logger.info(f"Button is clicked")
                    add_to_value_levers_list(data)
            st.markdown("---")  # Separator

        # Display current list of value levers
        if 'value_levers' in st.session_state and st.session_state['value_levers']:
            st.write("### Current List of Value Levers")
            for lever in st.session_state['value_levers']:
                st.write(lever)


def add_to_value_levers_list(value_lever):
    if 'value_levers' not in st.session_state:
        st.session_state['value_levers'] = []
    st.session_state['value_levers'].append(value_lever)
    st.success('Value Lever added to the list!')
    logger.info(f"Session state value levers: {st.session_state['value_levers']}")
