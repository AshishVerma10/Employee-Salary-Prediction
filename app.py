import streamlit as st
import joblib as jb
import pandas as pd
import time

# Initialize session state for theme
if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'

# Load the pretrained model
model = jb.load("salary_model.pkl")

# Set page configuration with a custom icon
st.set_page_config(page_title="💲 Salary Predictor", page_icon="💵", layout="centered")

# Custom CSS for dark and light modes
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Montserrat:wght@700&display=swap');

    .stApp {
        background: linear-gradient(45deg, #2C3E50, #3498DB, #8E44AD, #2980B9);
        background-size: 400%;
        animation: gradientFade 20s ease-in-out infinite;
        font-family: 'Poppins', sans-serif;
        color: #F0F0F0;
    }

    [data-theme="light"] .stApp {
        background: linear-gradient(45deg, #E6F0FA, #A3BFFA, #D6BCFA, #BEE3F8);
        color: #333333;
    }

    @keyframes gradientFade {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .title {
        font-family: 'Montserrat', sans-serif;
        font-size: 2.5em;
        text-align: center;
        margin-bottom: 0.5em;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }

    [data-theme="dark"] .title {
        color: #FFFFFF;
    }

    [data-theme="light"] .title {
        color: #333333;
    }

    .subtitle {
        font-family: 'Poppins', sans-serif;
        font-size: 1.2em;
        text-align: center;
        margin-bottom: 2em;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);
    }

    [data-theme="dark"] .subtitle {
        color: #F0F0F0;
    }

    [data-theme="light"] .subtitle {
        color: #555555;
    }

    .stButton>button {
        background-color: #3498DB;
        color: white;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        padding: 0.5em 2em;
        border-radius: 25px;
        border: none;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }

    [data-theme="light"] .stButton>button {
        background-color: #2B6CB0;
    }

    .stButton>button:hover {
        background-color: #2980B9;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
    }

    [data-theme="light"] .stButton>button:hover {
        background-color: #1A4971;
    }

    .stSelectbox, .stNumberInput, .stSlider {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 1em;
    }

    .stSelectbox label, .stNumberInput label, .stSlider label {
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        color: #333333;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8);
    }

    [data-theme="light"] .stSelectbox label, [data-theme="light"] .stNumberInput label, [data-theme="light"] .stSlider label {
        color: #333333;
    }

    .prediction-text {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.5em;
        text-align: center;
        margin-top: 1em;
        padding: 10px;
        border-radius: 10px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }

    [data-theme="dark"] .prediction-text {
        color: #FFFFFF;
        background-color: rgba(52, 152, 219, 0.9);
    }

    [data-theme="light"] .prediction-text {
        color: #333333;
        background-color: rgba(66, 153, 225, 0.8);
    }

    .stDataFrame {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 10px;
        padding: 10px;
    }

    .section-header {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.8em;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
    }

    [data-theme="dark"] .section-header {
        color: #FFFFFF;
    }

    [data-theme="light"] .section-header {
        color: #333333;
    }

    .stSidebar .stButton>button {
        width: 100%;
        margin-bottom: 1em;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown('<div class="title">Salary Predictor</div>', unsafe_allow_html=True)
page = st.sidebar.selectbox("Navigate", ["Home", "About Us", "Contact"], help="Select a page to view")

# Theme toggle button
if st.sidebar.button("Toggle Dark/Light Mode 🌙☀️"):
    st.session_state.theme = 'light' if st.session_state.theme == 'dark' else 'dark'

# Apply theme to the app
st.markdown(f'<div data-theme="{st.session_state.theme}"></div>', unsafe_allow_html=True)

# Page content
if page == "Home":
    # Title and description
    st.markdown('<div class="title">Employee Salary Prediction 💵</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Predict whether an employee earns above or below $50K based on their profile.</div>', unsafe_allow_html=True)

    # Input section
    st.markdown('<div class="section-header">Enter Employee Details 📋</div>', unsafe_allow_html=True)
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age 👤", min_value=18, max_value=70, value=30, help="Enter age between 18 and 70")
            education = st.selectbox("Education Level 🎓", [
                "Bachelors", "Masters", "Doctorate", "HS-grad", "Assoc-acdm", "Assoc-voc", "Some-college",
                "1st-4th", "5th-6th", "7th-8th", "9th", "10th", "11th", "12th", "Prof-school"
            ], help="Select the highest education level")
            occupation = st.selectbox("Occupation 💼", [
                "Prof-specialty", "Craft-repair", "Exec-managerial", "Adm-clerical", "Sales",
                "Other-service", "Machine-op-inspct", "Transport-moving", "Handlers-cleaners",
                "Farming-fishing", "Tech-support", "Protective-serv", "Priv-house-serv", "Armed-Forces"
            ], help="Select the occupation")
        with col2:
            workclass = st.selectbox("Organization 🏢", [
                "Private", "Self-emp-not-inc", "Local-gov", "State-gov", "Self-emp-inc",
                "Federal-gov", "Without-pay", "Never-worked"
            ], help="Select the workclass")
            hours_per_week = st.slider("Work Hours per Week ⏰", 1, 80, 40, help="Select hours worked per week (1-80)")

    # Create input DataFrame
    input_df = pd.DataFrame({
        'age': [age],
        'education': [education],
        'occupation': [occupation],
        'hours-per-week': [hours_per_week],
        'workclass': [workclass]
    })

    # Display input data
    st.markdown('<div class="section-header">Input Data Preview 📊</div>', unsafe_allow_html=True)
    st.dataframe(input_df, use_container_width=True)

    # Model performance chart
    st.markdown('<div class="section-header">Model Performance Comparison 📈</div>', unsafe_allow_html=True)
    model_results = {'Gradient Boosting': 0.8575, 'Random Forest': 0.84, 'Logistic Regression': 0.80}
    st.bar_chart(pd.DataFrame.from_dict(model_results, orient='index', columns=['Accuracy']))

    # Predict button for manual input
    if st.button("Predict Salary 🚀"):
        with st.spinner("Calculating prediction..."):
            time.sleep(1)  # Simulate processing time
            try:
                prediction = model.predict(input_df)[0]
                proba = model.predict_proba(input_df)[0]
                st.markdown(f'<div class="prediction-text">Predicted Income: <strong>{prediction}</strong> 💰</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="subtitle">Confidence: <=50K: {proba[0]:.2%}, >50K: {proba[1]:.2%}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Prediction failed: {str(e)}. Ensure input values match the model's training data.")

elif page == "About Us":
    st.markdown('<div class="title">About Us 📖</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="subtitle">
            Welcome to the Employee Salary Prediction App! This tool uses a Gradient Boosting model trained on the Adult Income dataset
            to predict whether an employee's income is above or below $50K based on features like age, education, occupation, workclass,
            and hours worked per week. Built with Streamlit and powered by AI/ML, this app provides an intuitive interface for exploring
            income predictions with confidence scores and model performance insights.
        </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="section-header">Features</div>', unsafe_allow_html=True)
    st.markdown("""
        - **Interactive Inputs**: Enter employee details to get instant predictions.
        - **Model Performance**: Visualize the accuracy of different models.
        - **Confidence Scores**: See the probability of each prediction.
        - **Modern UI**: Enjoy a sleek design with dark/light mode support.
    """, unsafe_allow_html=True)

elif page == "Contact":
    st.markdown('<div class="title">Contact Us 📧</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="subtitle">
            Have questions or feedback? Reach out to the creator of this app:
            <br><br>
            <strong>Ashish Kumar Verma</strong><br>
            <a href="https://www.linkedin.com/in/ashishverma2210/" target="_blank" style="color:#3498DB;text-decoration:underline;">LinkedIn Profile</a><br>
            Email: vashishverma10@gmail.com (for inquiries)<br><br>
            We’d love to hear your thoughts on improving the Salary Predictor!
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown('<div class="subtitle">© Built by <a href="https://www.linkedin.com/in/ashishverma2210/" target="_blank" style="color:#F0F0F0;text-decoration:underline;">Ashish Verma</a> | Powered by AI/ML</div>', unsafe_allow_html=True)