from utils import wrap_in_column
import pandas as pd
import streamlit as st
import plotly.express as px
from components.add_company import add_new_company
from utils import generate_performance_numbers, wrap_in_column


@wrap_in_column
def overview_dashboard():
    st.title('Welcome to intriq')
    with st.container():
        portfolio_overview()
    with st.container():
        company_overview()


def portfolio_overview():
    display_portfolio_kpi_summary()
    st.markdown("#")
    with st.expander('View Portfolio Performance'):
        display_portfolio_details()


def display_portfolio_kpi_summary():

    # Sample data for RAG status counts and change from last month
    rag_status = {
        "Green": {"count": 12, "change": "2 ⬆️"},
        "Amber": {"count": 7, "change": "-3 ⬇️"},
        "Red": {"count": 5, "change": "1 ⬆️"}
    }

    # Create a banner with HTML and CSS
    st.markdown(f"""
        <div style="background-color: #f4f4f4; padding: 10px; border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);">
            <h3 style="color: #333; text-align: center;">Initiative summary</h3>
            <div style="display: flex; justify-content: space-around;">
                <div>
                    <h3 style="color: #4caf50; margin-bottom: 0;">🟢 On Track</h3>
                    <strong style="margin-top: 5px;">Count: {rag_status['Green']['count']} (Change: {rag_status['Green']['change']})</strong>
                </div>
                <div>
                    <h3 style="color: #ff9800; margin-bottom: 0;">🟠 At Risk</h3>
                    <strong style="margin-top: 5px;">Count: {rag_status['Amber']['count']} (Change: {rag_status['Amber']['change']})</strong>
                </div>
                <div>
                    <h3 style="color: #f44336; margin-bottom: 0;">🔴 Requires Attention</h3>
                    <strong style="margin-top: 5px;">Count: {rag_status['Red']['count']} (Change: {rag_status['Red']['change']})</strong>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


def display_portfolio_details():
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
    st.plotly_chart(fig, use_container_width=True)


def company_overview():
    # Dropdown to select company
    col1, col2 = st.columns([6, 1])
    with col1:
        selected_company = st.selectbox(
            'Select Company', st.session_state['portfolio_companies'])
    with col2:
        st.markdown('<div class="small_gap"></div>', unsafe_allow_html=True)
        add_new_clicked = st.button('➕ Add New', use_container_width=True)
    if add_new_clicked:
        add_new_company()

    if selected_company:
        st.subheader(f"{selected_company} Overview")

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                'Company Profile',
                'Historical Financial Overview',
                'Budget - Financial Outlook',
                'Operational KPIs'
            ]
        )
        with tab1:
            display_company_profile(selected_company)
        with tab2:
            display_historical_financial_overview(selected_company)
        with tab3:
            display_budget_financial_outlook(selected_company)
        with tab4:
            display_operational_kpis(selected_company)


def display_company_profile(company):
    # Using columns to display key metrics
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            "<h3 style='text-align: center;'>Industry</h3>", unsafe_allow_html=True)
        st.markdown(
            "<h2 style='text-align: center; color: #1E90FF;'>Retail</h2>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            "<h3 style='text-align: center;'>No. of employees</h3>", unsafe_allow_html=True)
        st.markdown(
            "<h2 style='text-align: center; color: #2E8B57;'>592</h2>", unsafe_allow_html=True)

    # with col3:
    #     st.markdown(
    #         "<h3 style='text-align: center;'>Shareholder(s)</h3>", unsafe_allow_html=True)
    #     st.markdown(
    #         "<h2 style='text-align: center; color: #708090;'>XYZ Holdings</h2>", unsafe_allow_html=True)

    st.divider()
    # Dummy data
    revenue_streams = {"Stream": [
        "Online Sales", "In-Store Sales", "Wholesale"], "Revenue": [1500000, 1200000, 800000]}
    top_customers = ["Customer A", "Customer B",
                     "Customer C", "Customer D", "Customer E"]
    top_suppliers = {
        "Supplier": [
            "GlobaText Fabrics Ltd.", "StyleCraft Tailors Inc.", "EcoWeave Textiles Co.", "FastMove Logistics & Distribution",
            "BlueWave Denim Mills"
        ], "Annual Spend": [500000, 400000, 300000, 250000, 200000]}
    revenue_by_geo = pd.DataFrame({
        "Region": ["North America", "Europe", "Asia"],
        # Example latitudes for USA, France, Japan
        "Latitude": [37.76, 48.8566, 35.6895],
        # Example longitudes for USA, France, Japan
        "Longitude": [-122.4, 2.3522, 139.6917],
        "Revenue": [1200000, 1000000, 800000]  # Revenue in each region
    })

    # Creating columns
    col1, col2 = st.columns([2, 1])

    # Top Three Revenue Streams - Bar chart
    with col1:
        st.markdown("#### Top Revenue Streams")
        fig = px.bar(revenue_streams, x='Stream', y='Revenue', color='Stream')
        st.plotly_chart(fig, use_container_width=True)

    # # Top Five Customers - Pie chart
    # with col2:
    #     st.markdown("#### Top Customers")
    #     customer_data = pd.DataFrame(
    #         {"Customer": top_customers, "Value": [20, 20, 20, 20, 20]})
    #     fig = px.pie(customer_data, names='Customer', values='Value')
    #     st.plotly_chart(fig, use_container_width=True)

    # Top Five Suppliers - Custom HTML list
    with col2:
        st.markdown("#### Top Supplier Annual Spend")
        st.markdown("#")
        st.markdown(f"""
        <ul>
            <li><b>{top_suppliers['Supplier'][0]}:</b> ${top_suppliers['Annual Spend'][0]:,}</li>
            <li><b>{top_suppliers['Supplier'][1]}:</b> ${top_suppliers['Annual Spend'][1]:,}</li>
            <li><b>{top_suppliers['Supplier'][2]}:</b> ${top_suppliers['Annual Spend'][2]:,}</li>
            <li><b>{top_suppliers['Supplier'][3]}:</b> ${top_suppliers['Annual Spend'][3]:,}</li>
            <li><b>{top_suppliers['Supplier'][4]}:</b> ${top_suppliers['Annual Spend'][4]:,}</li>
        </ul>
        """, unsafe_allow_html=True)

    # Revenue by Geography
    st.markdown("#### Revenue by Geography")

    col1, col2 = st.columns([4, 7])
    with col1:
        fig = px.pie(revenue_by_geo, names='Region', values='Revenue')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Dummy data for demonstration purposes
        # Replace with actual latitudes and longitudes of regions

        # Adjust the size for visualization purposes
        # Adjust the divisor for better sizing

        # Plotting on the map
        st.map(revenue_by_geo,
               latitude='Latitude',
               longitude='Longitude',
               size='Revenue')


def display_historical_financial_overview(company):
    # 1. Primary driving factors of financials
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Primary Factor", "Online Sales Growth", "+30%")
    with col2:
        st.metric("Secondary Factor", "New Store Openings", "+20%")

    # 2. Historical trends - largest peaks/troughs
    historical_data = pd.DataFrame({
        "Year": ["2018", "2019", "2020", "2021", "2022", "2023"],
        "Revenue": [1000000, 1100000, 1050000, 1200000, 1400000, 1500000],
        "Gross Margin": [400000, 420000, 390000, 430000, 450000, 470000]
    })
    fig = px.line(historical_data, x="Year", y=[
                  "Revenue", "Gross Margin"], title="Revenue and Gross Margin Over Time")
    fig.update_layout(yaxis_title="USD", xaxis_title="Year",
                      xaxis=dict(type='category'))
    st.plotly_chart(fig, use_container_width=True)

    # 3. Breakdown of granular data
    st.markdown("#### Breakdown by region")
    st.selectbox("Select Year", ["2023", "2022",
                 "2021", "2020", "2019", "2018"])
    granular_data = pd.DataFrame({
        "Category": ["North America", "Europe", "Asia", "Retail", "Wholesale"],
        "Revenue": [600000, 400000, 300000, 700000, 400000],
        "Gross Margin": [45000, 32000, 40000, 47000, 44000]
    })
    fig = px.bar(granular_data, x="Category", y=[
                 "Revenue", "Gross Margin"], title="Revenue & Gross Margin by Category")
    st.plotly_chart(fig, use_container_width=True)

    # 4. Spend buckets - split of overheads
    st.markdown("#### Spend Buckets")
    spend_data = pd.DataFrame({
        "Overhead Category": ["Marketing", "R&D", "Administration", "Operations"],
        "Spend": [200000, 150000, 100000, 250000]
    })
    fig = px.pie(spend_data, names='Overhead Category',
                 values='Spend', title="Overhead Spend Distribution")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)


def display_budget_financial_outlook(company):
    # Column layout for Trends and Assumptions
    col1, col2 = st.columns([2, 1])
    with col1:
        # Example dummy data
        data = {
            'Year': ['2019', '2020', '2021', '2022', '2023', '2024'],
            'Historical Revenue': [300000, 400000, 500000, 600000, None, None],
            'Forecast Revenue': [None, None, None, 600000, 700000, 800000]
        }
        df = pd.DataFrame(data)

        # Melting the DataFrame for use with Plotly
        df_melted = df.melt(id_vars='Year', var_name='Type',
                            value_name='Revenue')

        # Plotting the graph
        fig = px.line(df_melted, x='Year', y='Revenue',
                      color='Type', markers=True)

        # Adding annotations for key points
        annotations = [
            dict(x='2022', y=600000, xref='x', yref='y',
                 text='Highest historical revenue', showarrow=True, arrowhead=1),
            dict(x='2024', y=800000, xref='x', yref='y',
                 text='Projected revenue peak', showarrow=True, arrowhead=1)
        ]
        fig.update_layout(annotations=annotations)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # 4.2 Underlying assumptions for Budget - Styled HTML elements
        st.markdown("#### Underlying Assumptions")
        st.markdown("""
            <div style="background-color:lightblue;padding:10px;border-radius:5px;">
                <h4 style="margin:0;">Increased Online Sales</h4>
                <p>20% increase due to marketing initiatives.</p>
            </div>
            <div style="background-color:lightgreen;padding:10px;margin-top:10px;border-radius:5px;">
                <h4 style="margin:0;">New Store Openings</h4>
                <p>Expansion in Europe and Asia.</p>
            </div>
            <div style="background-color:lightcoral;padding:10px;margin-top:10px;border-radius:5px;">
                <h4 style="margin:0;">Cost Reductions</h4>
                <p>5% savings in supply chain optimizations.</p>
            </div>
        """, unsafe_allow_html=True)

    # 4.3 Top 5 Takeaways from Budget - Displayed as an interactive list
    st.markdown("#### Top 5 Takeaways from Budget")
    takeaways = [
        'Projected 10% Revenue Growth in 2022',
        'Significant investment in digital transformation',
        'Expansion in international markets',
        'Enhanced focus on customer retention programs',
        'Initiatives to streamline operational costs'
    ]
    for takeaway in takeaways:
        st.button(takeaway)


def display_operational_kpis(company):
    # 5.1 Highlight main KPIs - largest financial impact
    st.markdown("#### Main KPIs - Largest Financial Impact")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### KPI: Online Sales Growth")
        st.markdown("📈 **15% increase** in last quarter")
        st.markdown(
            "🚀 **Primary drivers:** Improved website UX, targeted marketing campaigns")
        st.progress(75)
    with col2:
        st.markdown("##### KPI: Customer Retention Rate")
        st.markdown("📉 **5% decrease** in last quarter")
        st.markdown(
            "🔍 **Primary drivers:** Increased competition, market saturation")
        st.progress(40)

    # 5.2 Overview of all KPIs split by division
    st.markdown("#### KPI Overview by Division")
    kpi_data = {
        'Division': ['Sales', 'Marketing', 'Supply Chain', 'HR', 'IT'],
        'KPI Score': [80, 75, 70, 85, 65],
        'Trend': ['📈', '📉', '📈', '📉', '📈']
    }
    kpi_df = pd.DataFrame(kpi_data)
    fig = px.bar(kpi_df, x='Division', y='KPI Score', text='Trend',
                 title='KPI Scores by Division')
    fig.update_layout(showlegend=False,
                      yaxis_title="KPI Score", xaxis_title="Division")
    st.plotly_chart(fig, use_container_width=True)

    # # Historical vs. forecasted KPIs
    # st.markdown("#### Historical vs. Forecasted KPIs")
    # historical_forecast_data = {
    #     'Date': pd.date_range('2021-01', periods=12, freq='M'),
    #     'Historical KPI': [60, 62, 63, 65, 64, 66, 67, 69, 70, 72, 73, 75],
    #     'Forecasted KPI': [75, 76, 77, 78, 80, 81, 82, 84, 85, 87, 88, 90]
    # }
    # hf_df = pd.DataFrame(historical_forecast_data)
    # fig_hf = px.line(hf_df, x='Date', y=['Historical KPI', 'Forecasted KPI'],
    #                  title='Historical vs Forecasted KPIs')
    # fig_hf.update_layout(yaxis_title="KPI Score", xaxis_title="Date")
    # st.plotly_chart(fig_hf, use_container_width=True)


# def display_financial_forecast(company):
#     # Dummy Forecast Data
#     forecast_data = pd.DataFrame({
#         'Month': pd.date_range('2022-01', periods=12, freq='M'),
#         'Forecast Revenue': [100 + i*10 for i in range(12)],
#         'Current Revenue': [95 + i*9 for i in range(12)]
#     })

#     # Forecast vs. Current
#     st.markdown("#### Forecast vs. Current Performance")
#     display_forecast_vs_current(forecast_data)

#     # Dummy Variance Data
#     variance_data = pd.DataFrame({
#         'Month': pd.date_range('2022-01', periods=12, freq='M'),
#         'Variance': [5 - i for i in range(12)]
#     })

#     # Variance vs. Budget
#     st.markdown("#### % Variance vs. Budget")
#     fig = px.bar(variance_data, x='Month', y='Variance',
#                  title='% Variance vs. Budget')
#     st.plotly_chart(fig, use_container_width=True)

#     # Impact on Liquidity and Shareholder Returns
#     st.markdown("#### Impact on Liquidity & Shareholder Returns")
#     display_liquidity_and_returns(company)


# def display_forecast_vs_current(forecast_data):
#     fig = px.line(forecast_data, x='Month', y=[
#                   'Forecast Revenue', 'Current Revenue'], title='Forecast vs. Current Revenue')
#     st.plotly_chart(fig, use_container_width=True)


# def display_liquidity_and_returns(company):
#     # Dummy data for liquidity and shareholder returns
#     liquidity_data = {
#         'Metric': ['Current Ratio', 'Quick Ratio'],
#         'Value': [1.5, 1.2]  # Example values
#     }
#     returns_data = {
#         'Metric': ['ROI', 'Shareholder Return'],
#         'Value': [20, 5]  # Example values, in percentage
#     }

#     # Display liquidity data using a bar chart
#     fig_liquidity = px.bar(liquidity_data, x='Metric',
#                            y='Value', title='Liquidity Metrics')
#     st.plotly_chart(fig_liquidity, use_container_width=True)

#     # Display shareholder returns using a bar chart
#     fig_returns = px.bar(returns_data, x='Metric', y='Value',
#                          title='Shareholder Returns (%)')
#     st.plotly_chart(fig_returns, use_container_width=True)

#     # Additional annotations or notes
#     st.write("Note: ROI is tracking at 20%, aligning closely with our strategic goals. Shareholder returns are currently at 5x the initial investment.")


# def display_initiative_summary(company):
#     # Dummy data for initiative performance (RAG status)
#     initiative_performance = {
#         "Initiative": ["Digital Upgrade", "Eco Packaging", "Customer Loyalty Program"],
#         "Status": ["On Track", "At Risk", "Requires Attention"],
#         "Impact": [80, 65, 50]  # Example impact values
#     }
#     initiative_df = pd.DataFrame(initiative_performance)

#     # RAG status count and display
#     rag_status = {
#         "Green": {"count": 12, "change": "2"},
#         "Amber": {"count": 7, "change": "-3"},
#         "Red": {"count": 5, "change": "1"}
#     }
#     st.subheader("Initiative RAG Status")
#     col1, col2, col3 = st.columns(3)
#     col1.metric("🟢 On Track", rag_status["Green"
#                                          ]["count"], rag_status["Green"]["change"])
#     col2.metric("🟠 At Risk", rag_status["Amber"
#                                         ]["count"], rag_status["Amber"]["change"])
#     col3.metric("🔴 Requires Attention",
#                 rag_status["Red"]["count"], rag_status["Red"]["change"])

#     # Display initiatives with their status and impact
#     st.markdown("#### Initiative Performance")
#     fig = px.bar(initiative_df, x="Initiative",
#                  y="Impact", color="Status", text="Impact")
#     fig.update_layout(showlegend=False, xaxis_title="",
#                       yaxis_title="Impact Score", plot_bgcolor="rgba(0,0,0,0)")
#     st.plotly_chart(fig, use_container_width=True)
