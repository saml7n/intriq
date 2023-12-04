import ssl
import streamlit as st
from dotenv import main
import nltk
from loguru import logger
from streamlit_agraph import agraph, Config
import plotly.express as px

from knowledge_graphs_utils import display_loading_bar, get_nodes_and_edges


main.load_dotenv()
_PARTITION_STRATEGY = 'hi_res'
_PARTITION_MODEL_NAME = 'yolox'
_OPEN_AI_MODEL_NAME = 'gpt-3.5-turbo-0613'

# Download necessary NLTK data
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('stopwords')


def clear_submit():
    """
    Clear the Submit Button State
    Returns:

    """
    st.session_state["submit"] = False


def main():
    st.set_page_config(
        page_title="intriq data diagnostics",
        page_icon="🤖"
    )
    st.title("intriq data diagnostics 🔍")

    # Initialize 'current_page' in session state if not already set
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'upload_data'

    # Sidebar Menu
    st.sidebar.title("Navigation")
    if st.sidebar.button('📂 Upload Data', use_container_width=True):
        st.session_state['current_page'] = 'upload_data'

    has_data = st.session_state.get(
        'financial_data') and st.session_state.get('operational_data')
    if st.sidebar.button('🗺️ View Data Map', use_container_width=True, disabled=not has_data):
        st.session_state['current_page'] = 'view_graph'
    if st.sidebar.button('🔍 Data explorer', use_container_width=True, disabled=not has_data):
        st.session_state['current_page'] = 'data_explorer'
    if st.sidebar.button('🎚️ Control Center', use_container_width=True, disabled=not has_data):
        st.session_state['current_page'] = 'control_center'

    # Display the current page based on session state
    if st.session_state['current_page'] == 'upload_data':
        upload_data_section()
    elif st.session_state['current_page'] == 'view_graph':
        view_graph_section()
    elif st.session_state['current_page'] == 'data_explorer':
        data_explorer_section()
    elif st.session_state['current_page'] == 'control_center':
        control_center_section()


def upload_data_section():
    st.subheader("Upload your data files 📂")
    uploaded_financials = st.file_uploader(
        "📊 Add financial data files here",
        accept_multiple_files=True,
        help="Various File formats are supported",
    )
    uploaded_operationals = st.file_uploader(
        "⚙️ Add operational data files here",
        accept_multiple_files=True,
        help="Various File formats are supported",
    )
    if uploaded_financials and uploaded_operationals:
        logger.info("Files uploaded successfully!")
        st.success("Files uploaded successfully!")
        process_uploaded_files(uploaded_financials, uploaded_operationals)


def process_uploaded_files(financials, operationals):
    # Example of storing in session state
    st.session_state['financial_data'] = financials
    st.session_state['operational_data'] = operationals
    display_loading_bar()
    st.button("Rerun analysis")


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
                    height=1200,
                    directed=True,
                    nodeHighlightBehavior=True,
                    highlightColor="#F7A7A6",
                    collapsible=True,
                    physics={'enabled': False})

    # Render the graph
    agraph(nodes=nodes,
           edges=edges,
           config=config)
    draw_pie_chart(financial_kpi_options[0])


def data_explorer_section():
    st.subheader("KPI Customization")
    # Code to allow users to select and customize KPIs for display
    # ... (use a form or multiselect to let users choose KPIs)


def control_center_section():
    st.subheader("Value Levers vs Data Anomalies")
    # Code to analyze value levers and identify anomalies
    # ... (implement analysis and visualization logic)


def draw_pie_chart(financial_kpi):
    data = {
        'Category': [
            'Category A',
            'Category B',
            'Category C',
            'Category D'
        ],
        'Values': [15, 30, 45, 10]
    }

    fig = px.pie(data, names='Category', values='Values')

    # Display the pie chart
    st.plotly_chart(fig)


if __name__ == "__main__":
    main()
