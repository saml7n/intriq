import streamlit as st
from loguru import logger

from utils import MenuOption


def display_playbook_dashboard():
    st.subheader("Next Steps Checklist")
    with st.expander("❓ Help"):
        display_help()

    # Styling for the checklist items to make them stand out
    st.markdown("""
        <style>
        .checklist {
            padding: 0.5rem;
            background-color: #f0f2f6;
            border-left: 5px solid #0078D7;
            margin: 0.5rem 0;
            border-radius: 0.5rem;
        }
        .checklist h4 {
            color: #0078D7;
            margin-bottom: 0.25rem;
        }
        </style>
    """, unsafe_allow_html=True)

    next_steps = [
        {
            "title": "Upload Your First Piece of Financial Data",
            "detail": "Start by uploading the upcoming quarter's budget. This will help in setting a financial baseline for your analysis."
        },
        {
            "title": "Upload Your First Piece of Operational Data",
            "detail": "Consider integrating data on inventory turnover or daily sales. This operational metric can provide insights into product demand and supply chain efficiency."
        },
        {
            "title": "Conduct Your First Interview",
            "detail": "Schedule an interview with the head of retail operations. Focus on questions about customer foot traffic, sales conversion rates, and any recent operational changes."
        }
    ]

    for i, step in enumerate(next_steps, 1):
        st.markdown(f"""
            <div class="checklist">
                <h4>Step {i}: {step['title']}</h4>
                <p>{step['detail']}</p>
            </div>
        """, unsafe_allow_html=True)

    st.subheader("Interview Guide")
    st.write("Select a department or role to schedule your interview and get a customized set of questions.")

    # Dropdown to select the department/role
    department = st.selectbox("Choose a Department or Role", [
                              "Retail Operations", "Sales and Marketing", "Supply Chain Management", "Human Resources"])

    # Display interview questions based on the selection
    display_interview_questions(department)


def display_interview_questions(department):
    # Dictionary containing questions for each department
    interview_questions = {
        "Retail Operations": [
            "How do customer foot traffic patterns influence sales and operational decisions?",
            "Can you describe the most significant changes in retail operations over the past year?",
            "How do seasonal trends affect our inventory management and staffing?",
            "What are the key challenges in maintaining optimal stock levels?",
            "How effectively are we utilizing in-store promotions and displays?",
            "What feedback do we receive from customers regarding their in-store experience?",
            "How is technology being used to enhance the efficiency of in-store operations?",
            "Can you identify any bottlenecks or inefficiencies in our current retail operations?",
            "How do we measure the success of our retail strategies?",
            "What improvements would you suggest to enhance customer satisfaction and sales?"
        ],
        "Sales and Marketing": [
            "What strategies have proven most effective in converting leads to sales?",
            "How do our marketing efforts correlate with sales outcomes, and what metrics do we use?",
            "What challenges do we face in reaching our target audience?",
            "How do we track and analyze customer buying behavior?",
            "What digital marketing trends are we currently leveraging?",
            "How do customer feedback and market research influence our marketing strategies?",
            "What role does social media play in our marketing efforts?",
            "How do we measure the ROI of our marketing campaigns?",
            "What are our strategies for customer retention and loyalty?",
            "How do we adapt our sales and marketing strategies to changing market conditions?"
        ],
        # Add more departments and questions as necessary
    }

    questions = interview_questions.get(
        department, ["No questions available for this department."])

    st.write(f"### Interview Questions for {department}")
    for i, question in enumerate(questions, 1):
        st.markdown(f"{i}. {question}")

    if st.button('Upload your data here'):
        st.session_state['current_page'] = MenuOption.DATA_CONNECTION.name
        st.session_state['current_page_switch'] = True
        # st.rerun()
        logger.info(f'current page {st.session_state["current_page"]}')
        st.rerun()


def display_help():
    st.subheader("Data Integration Guide")

    # Instructions and steps for initial data input
    st.write("""
        ### Getting Started with Data Integration
        To leverage the full potential of this system, begin by integrating key data sources. 
        Here are the initial steps to build your operational and financial map:
        1. **Financial Data**: Input historical and current financial data, including budgets and P&L statements.
        2. **Operational Data**: Upload relevant operational metrics that are crucial for your business.
        3. **Stakeholder Interviews**: Conduct and record interviews with key stakeholders to gather qualitative insights.
        4. **Data Verification**: Ensure data accuracy and completeness before proceeding.
        As more data is added, the system will start to build a more comprehensive map of KPIs and their interrelationships.
        **Connect data by clicking on the button in the side-panel.**
    """)

    # Advanced Features Description
    st.write("""
        ### Advanced Analysis
        Once sufficient data is fed into the system:
        - The tool will start suggesting potential value levers based on data-driven insights.
        - You can explore quantitative relationships between operational KPIs and financial targets.
        - Clicking on a financial KPI will provide a detailed breakdown of its performance, influenced by operational metrics.
    """)
