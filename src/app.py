import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------
model = joblib.load("student_performance_model.pkl")

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f172a, #1e293b);
    color: white;
}

/* MAIN TITLE */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #38bdf8;
    margin-bottom: 5px;
}

/* SUB TITLE */
.sub-title {
    text-align: center;
    font-size: 17px;
    color: #cbd5e1;
    margin-bottom: 20px;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* KPI CARDS */
.metric-card {
    background: rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    backdrop-filter: blur(10px);
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}

.metric-card h1 {
    font-size: 30px;
    color: #38bdf8;
}

.metric-card h2 {
    font-size: 18px;
    color: white;
}

/* BUTTON */
.stButton>button {
    background-color: #0ea5e9;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 18px;
    width: 100%;
    font-size: 15px;
}

.stButton>button:hover {
    background-color: #0284c7;
}

html, body, [class*="css"] {
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown(
    '<div class="main-title">🎓 Student Performance Prediction AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Advanced Machine Learning Dashboard for Predicting Student GPA</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("📘 Student Details")

Age = st.sidebar.slider(
    "Age",
    15,
    25,
    18
)

Gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

Gender = 1 if Gender == "Male" else 0

ParentalEducation = st.sidebar.selectbox(
    "Parental Education",
    [
        "0 - Uneducated",
        "1 - Primary School",
        "2 - High School",
        "3 - Intermediate",
        "4 - Bachelor's Degree",
        "5 - Master's Degree"
    ]
)

ParentalEducation = int(
    ParentalEducation.split(" - ")[0]
)

StudyTimeWeekly = st.sidebar.slider(
    "Study Time Weekly (Hours)",
    0.0,
    25.0,
    10.0
)

Absences = st.sidebar.slider(
    "Absences",
    0,
    30,
    5
)

Tutoring = st.sidebar.selectbox(
    "Tutoring",
    ["No", "Yes"]
)

Tutoring = 1 if Tutoring == "Yes" else 0

ParentalSupport = st.sidebar.selectbox(
    "Parental Support",
    [
        "0 - Very Low",
        "1 - Low",
        "2 - Moderate",
        "3 - Good",
        "4 - Excellent"
    ]
)

ParentalSupport = int(
    ParentalSupport.split(" - ")[0]
)

Extracurricular = st.sidebar.selectbox(
    "Extracurricular Activities",
    ["No", "Yes"]
)

Extracurricular = 1 if Extracurricular == "Yes" else 0

Sports = st.sidebar.selectbox(
    "Sports Participation",
    ["No", "Yes"]
)

Sports = 1 if Sports == "Yes" else 0

Music = st.sidebar.selectbox(
    "Music Activities",
    ["No", "Yes"]
)

Music = 1 if Music == "Yes" else 0

Volunteering = st.sidebar.selectbox(
    "Volunteering",
    ["No", "Yes"]
)

Volunteering = 1 if Volunteering == "Yes" else 0

GradeClass = st.sidebar.selectbox(
    "Previous Academic Performance",
    [
        "0 - Fail",
        "1 - Pass",
        "2 - Average",
        "3 - Good",
        "4 - Excellent"
    ]
)

GradeClass = int(
    GradeClass.split(" - ")[0]
)

# ---------------------------------------------------
# PREDICTION
# ---------------------------------------------------
if st.sidebar.button("🚀 Predict GPA"):

    features = np.array([
        Age,
        Gender,
        ParentalEducation,
        StudyTimeWeekly,
        Absences,
        Tutoring,
        ParentalSupport,
        Extracurricular,
        Sports,
        Music,
        Volunteering,
        GradeClass
    ]).reshape(1, -1)

    prediction = model.predict(features)

    predicted_gpa = round(
        float(prediction[0]),
        2
    )

    # ---------------------------------------------------
    # PERFORMANCE CATEGORY
    # ---------------------------------------------------
    if predicted_gpa >= 3.5:
        category = "Excellent"

    elif predicted_gpa >= 3.0:
        category = "Good"

    elif predicted_gpa >= 2.0:
        category = "Average"

    else:
        category = "Needs Improvement"

    attendance_score = max(
        0,
        100 - (Absences * 3)
    )

    # ---------------------------------------------------
    # KPI CARDS
    # ---------------------------------------------------
    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(f"""
        <div class="metric-card">
            <h2>🎯 Predicted GPA</h2>
            <h1>{predicted_gpa}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class="metric-card">
            <h2>🏆 Performance</h2>
            <h1>{category}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown(f"""
        <div class="metric-card">
            <h2>📅 Attendance Score</h2>
            <h1>{attendance_score}%</h1>
        </div>
        """, unsafe_allow_html=True)

    # ---------------------------------------------------
    # GAUGE CHART
    # ---------------------------------------------------
    st.markdown("## 📈 GPA Satisfaction Meter")

    gauge = go.Figure()

    gauge.add_trace(go.Indicator(

        mode="gauge+number",

        value=predicted_gpa,

        title={'text': "General Satisfaction"},

        gauge={

            'axis': {
                'range': [0, 5]
            },

            'bar': {
                'color': "#1d2088",
                'thickness': 0.45
            },

            'steps': [
                {'range': [0, 2], 'color': '#7dd3fc'},
                {'range': [2, 4], 'color': '#5eead4'},
                {'range': [4, 5], 'color': '#d1fae5'}
            ],

            'threshold': {
                'line': {
                    'color': "#991b1b",
                    'width': 6
                },
                'thickness': 0.75,
                'value': 4.5
            }
        }
    ))

    gauge.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font={
            'color': 'white',
            'size': 18
        },
        height=500
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

    # ---------------------------------------------------
    # BAR CHART
    # ---------------------------------------------------
    st.markdown("## 📊 Student Analytics Dashboard")

    chart_data = pd.DataFrame({

        "Factors": [
            "Study Time",
            "Attendance",
            "Parental Support",
            "Activities",
            "Tutoring"
        ],

        "Values": [
            min(StudyTimeWeekly * 4, 100),
            attendance_score,
            ParentalSupport * 25,
            Extracurricular * 100,
            Tutoring * 100
        ]
    })

    bar_chart = px.bar(

        chart_data,

        x="Factors",

        y="Values",

        text="Values",

        template="plotly_dark",

        height=450
    )

    bar_chart.update_traces(
        textposition='outside'
    )

    bar_chart.update_layout(

        paper_bgcolor='rgba(0,0,0,0)',

        plot_bgcolor='rgba(0,0,0,0)',

        font=dict(
            color='white',
            size=14
        ),

        xaxis_title="Student Factors",

        yaxis_title="Performance Percentage",

        showlegend=False
    )

    st.plotly_chart(
        bar_chart,
        use_container_width=True
    )

    # ---------------------------------------------------
    # RECOMMENDATIONS
    # ---------------------------------------------------
    st.markdown("## 💡 AI Recommendations")

    recommendations = []

    if StudyTimeWeekly < 8:

        recommendations.append(
            "Increase weekly study hours for better GPA performance."
        )

    if Absences > 10:

        recommendations.append(
            "Reducing absences can significantly improve academic outcomes."
        )

    if Tutoring == 0:

        recommendations.append(
            "Joining tutoring sessions may improve learning consistency."
        )

    if Extracurricular == 0:

        recommendations.append(
            "Participating in extracurricular activities can improve overall development."
        )

    if len(recommendations) == 0:

        recommendations.append(
            "Excellent habits detected. Maintain your current performance strategy."
        )

    for rec in recommendations:

        st.success(rec)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")

st.markdown(
    "<center>Developed using Streamlit • Machine Learning • Plotly • AI Analytics</center>",
    unsafe_allow_html=True
)