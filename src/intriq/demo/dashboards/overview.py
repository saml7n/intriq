import pandas as pd
import streamlit as st
import plotly.express as px
from components.add_company import add_new_company
from utils import generate_performance_numbers, wrap_in_column


@wrap_in_column
def overview_dashboard():
    # Header
    st.title('Welcome to intriq')
    st.subheader('*One tool for all your transformation diagnostic needs*')
    portfolio_tab, company_tab = st.tabs(['Portfolio', 'Company'])
    with portfolio_tab:
        portfolio_overview()
    with company_tab:
        company_overview()


def portfolio_overview():
    st.header('Portfolio Overview')
    option = st.selectbox(
        'Select metric',
        ('Revenue', 'Gross Margin', 'EBITDA'),
        key='portfolio_metric'
    )
    graph_df = pd.DataFrame(
        generate_performance_numbers(
            st.session_state['portfolio_companies'], option
        ),
        index=pd.date_range(
            '2022-12-01', periods=12, freq='M'
        )
    )
    graph_df.index.name = 'Date'
    fig = px.line(
        graph_df,
        labels={'value': f'{option} (% change)'}
    )

    # Display the line chart
    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    display_portfolio_kpi_summary(option)


def company_overview():
    st.subheader('Company Overview')
    # add_new_clicked = False
    col1, col2 = st.columns([6, 1])
    with col1:
        selected_company = st.selectbox(
            'Select Company', st.session_state['portfolio_companies'])
    with col2:
        # small gap before the button to align with the selectbox
        st.markdown("""
                    <style>
                    .small_gap {
                        margin-top: 1px;
                    }
                    </style>
        """, unsafe_allow_html=True)
        st.markdown('<div class="small_gap"></div>', unsafe_allow_html=True)
        add_new_clicked = st.button('➕ Add New', use_container_width=True)

    if add_new_clicked:
        selected_company = None
        add_new_company()

    if selected_company:
        st.subheader(f"{selected_company} Financial Forecast")
        display_financial_forecast(selected_company)

        st.subheader(f"{selected_company} Initiative Summary")
        display_initiative_summary(selected_company)


def display_portfolio_kpi_summary(metric):
    st.header("Initiative Summary")

    # Sample data for RAG status counts and change from last month
    rag_status = {
        "Green": {"count": 12, "change": "2"},
        "Amber": {"count": 7, "change": "-3"},
        "Red": {"count": 5, "change": "1"}
    }

    st.subheader("Initiative RAG Status")
    col1, col2, col3 = st.columns(3)

    # Display RAG status using st.metric
    col1.metric("🟢 On track",
                rag_status["Green"]["count"], rag_status["Green"]["change"])
    col2.metric("🟠 At risk",
                rag_status["Amber"]["count"], rag_status["Amber"]["change"])
    col3.metric("🔴 Requires attention",
                rag_status["Red"]["count"], rag_status["Red"]["change"])

    # Top Performing Initiatives (Dummy data)
    initiative_data = {
        "Initiative": [
            "RFID Inventory Tracking (Lakeland)",
            "Supplier Portal (Crew Clothing)", "AI-Powered Customer Service (Paperchase)"],
        "Impact": [75, 85, 90]
    }
    st.markdown('#')
    # Top Performing initiatives Section
    st.subheader("Top Performing Initiatives This Month")
    fig = px.bar(initiative_data, x="Initiative", y="Impact",
                 color="Initiative", text=f"Impact")
    fig.update_layout(showlegend=False, xaxis_title="",
                      yaxis_title=f"{metric} Impact", plot_bgcolor="rgba(0,0,0,0)")
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True)


def display_financial_forecast(company):
    # Dummy Forecast Data
    forecast_data = pd.DataFrame({
        'Month': pd.date_range('2022-01', periods=12, freq='M'),
        'Forecast Revenue': [100 + i*10 for i in range(12)],
        'Current Revenue': [95 + i*9 for i in range(12)]
    })

    # Forecast vs. Current
    st.markdown("#### Forecast vs. Current Performance")
    display_forecast_vs_current(forecast_data)

    # Dummy Variance Data
    variance_data = pd.DataFrame({
        'Month': pd.date_range('2022-01', periods=12, freq='M'),
        'Variance': [5 - i for i in range(12)]
    })

    # Variance vs. Budget
    st.markdown("#### % Variance vs. Budget")
    fig = px.bar(variance_data, x='Month', y='Variance',
                 title='% Variance vs. Budget')
    st.plotly_chart(fig, use_container_width=True)

    # Impact on Liquidity and Shareholder Returns
    st.markdown("#### Impact on Liquidity & Shareholder Returns")
    display_liquidity_and_returns(company)


def display_forecast_vs_current(forecast_data):
    fig = px.line(forecast_data, x='Month', y=[
                  'Forecast Revenue', 'Current Revenue'], title='Forecast vs. Current Revenue')
    st.plotly_chart(fig, use_container_width=True)


def display_liquidity_and_returns(company):
    # Dummy data for liquidity and shareholder returns
    liquidity_data = {
        'Metric': ['Current Ratio', 'Quick Ratio'],
        'Value': [1.5, 1.2]  # Example values
    }
    returns_data = {
        'Metric': ['ROI', 'Shareholder Return'],
        'Value': [20, 5]  # Example values, in percentage
    }

    # Display liquidity data using a bar chart
    fig_liquidity = px.bar(liquidity_data, x='Metric',
                           y='Value', title='Liquidity Metrics')
    st.plotly_chart(fig_liquidity, use_container_width=True)

    # Display shareholder returns using a bar chart
    fig_returns = px.bar(returns_data, x='Metric', y='Value',
                         title='Shareholder Returns (%)')
    st.plotly_chart(fig_returns, use_container_width=True)

    # Additional annotations or notes
    st.write("Note: ROI is tracking at 20%, aligning closely with our strategic goals. Shareholder returns are currently at 5x the initial investment.")


def display_initiative_summary(company):
    # Dummy data for initiative performance (RAG status)
    initiative_performance = {
        "Initiative": ["Digital Upgrade", "Eco Packaging", "Customer Loyalty Program"],
        "Status": ["On Track", "At Risk", "Requires Attention"],
        "Impact": [80, 65, 50]  # Example impact values
    }
    initiative_df = pd.DataFrame(initiative_performance)

    # RAG status count and display
    rag_status = {
        "Green": {"count": 12, "change": "2"},
        "Amber": {"count": 7, "change": "-3"},
        "Red": {"count": 5, "change": "1"}
    }
    st.subheader("Initiative RAG Status")
    col1, col2, col3 = st.columns(3)
    col1.metric("🟢 On Track", rag_status["Green"
                                         ]["count"], rag_status["Green"]["change"])
    col2.metric("🟠 At Risk", rag_status["Amber"
                                        ]["count"], rag_status["Amber"]["change"])
    col3.metric("🔴 Requires Attention",
                rag_status["Red"]["count"], rag_status["Red"]["change"])

    # Display initiatives with their status and impact
    st.markdown("#### Initiative Performance")
    fig = px.bar(initiative_df, x="Initiative",
                 y="Impact", color="Status", text="Impact")
    fig.update_layout(showlegend=False, xaxis_title="",
                      yaxis_title="Impact Score", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)
