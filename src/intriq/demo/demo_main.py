import ssl
from loguru import logger
import streamlit as st
from dotenv import main
import nltk
from streamlit_option_menu import option_menu
from dashboards.analyse import display_analysis_dashboard
from dashboards.data_connection import display_connection_dashboard
from dashboards.tracking import display_tracking_dashboard
from dashboards.overview import overview_dashboard
from data_dict import INITIAL_PORTFOLIO_COMPANIES
from utils import MenuOption
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
        page_icon="🤖",
        layout='wide'
    )

    # Initialize 'current_page' in session state if not already set
    if 'current_page' not in st.session_state:
        st.session_state['current_page_switch'] = None
        st.session_state['current_page'] = MenuOption.OVERVIEW.name
        st.session_state['data_sources'] = {'Sage': 'cash-coin', 'SAP': 'gear'}
        st.session_state['portfolio_companies'] = INITIAL_PORTFOLIO_COMPANIES
        st.session_state['show_value_levers'] = False
        st.session_state['selected_company'] = None
        st.session_state["messages"] = [
            {"role": "assistant", "content": "How can I help you?"}]
        st.session_state['new_data_added'] = False

    # Options Menu
    with st.sidebar:
        selected = option_menu(
            'intriq', [option.value for option in MenuOption],
            icons=[
                'house',
                'plug',
                'eye',
                'graph-up',
                'info-circle'
            ],
            menu_icon='intersect',
            default_index=0,
        )
        # Update current page based on selection or switch
        logger.info(f'selected {selected}')
        if st.session_state['current_page_switch']:
            st.session_state['current_page'] = st.session_state['current_page_switch']
            st.session_state['current_page_switch'] = None

        else:
            st.session_state['current_page'] = MenuOption(selected).name

    # Display the selected dashboard
    switch_page(st.session_state['current_page'])


def switch_page(switch):
    logger.info(f"Switching to {switch}")
    if switch == MenuOption.OVERVIEW.name:
        overview_dashboard()
    if switch == MenuOption.CONNECT_DATA.name:
        display_connection_dashboard()
    if switch == MenuOption.ANALYSE.name:
        display_analysis_dashboard()
    if switch == MenuOption.TRACK.name:
        display_tracking_dashboard()


if __name__ == '__main__':
    main()
