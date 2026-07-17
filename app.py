import streamlit as st
from datetime import datetime
import joblib
import pandas as pd

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet



# ===========================
# LOAD MODEL
# ===========================

@st.cache_resource
def load_model():
    return joblib.load("models/disease_prediction_model.pkl")

model = load_model()

# ==========================================================
# PDF REPORT FUNCTION
# ==========================================================

def create_pdf(patient_name, disease, confidence):

    pdf_file = "Patient_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>SMART HOSPITAL ANALYTICS SYSTEM</b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Patient Name :</b> {patient_name}", styles["BodyText"]))

    story.append(Paragraph(f"<b>Predicted Disease :</b> {disease}", styles["BodyText"]))

    story.append(Paragraph(f"<b>Confidence :</b> {confidence:.2f}%", styles["BodyText"]))

    story.append(Paragraph(f"<b>Date :</b> {datetime.now().strftime('%d-%m-%Y')}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>AI Health Recommendation</b>", styles["Heading2"]))

    story.append(Paragraph(
        "This prediction is generated using a Machine Learning model. "
        "Please consult a qualified doctor before making any medical decisions.",
        styles["BodyText"]
    ))

    doc.build(story)

    return pdf_file





# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Smart Hospital Analytics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* Sirf toolbar (deploy button, menu) hide karo, poora header nahi
   - isse sidebar ka collapse/expand arrow hamesha kaam karega */
[data-testid="stToolbar"] {
    visibility: hidden;
}

/* Hide Main Menu */
#MainMenu{
    visibility:hidden;
}

/* Hide Footer */
footer{
    visibility:hidden;
}

/* Remove top padding */
.block-container{
    padding-top:4rem;
}

</style>
""", unsafe_allow_html=True)




# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main{
    background-color:#f5f7fa;
}

[data-testid="stSidebar"]{
    background-color:#0E1117;           
}
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div {
    color: white !important;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:12px;
    padding:15px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.15);
}

.big-title{
    font-size:50px;
    font-weight:800;
    color:#1976D2;
    line-height:1.2;
    margin-bottom:10px;
    letter-spacing:0.5px;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    overflow-x:auto;
}

.sub-title{
    font-size:20px;
    color:#666666;
    font-weight:500;
    margin-bottom:5px;
}

.footer{
    text-align:center;
    color:gray;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)



# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.image(
    "https://img.icons8.com/color/96/hospital-3.png",
    width=90
)

st.sidebar.title("SMART HOSPITAL")

st.sidebar.markdown("---")

menu = st.sidebar.radio(
    # ==========================================


    "Navigation",

    [

        "🏠 Dashboard",

        "🤖 Health Prediction",

        "📊 Analytics",

        "📄 Reports",

        "ℹ About"

    ]

)

dark_mode = st.sidebar.toggle("🌙 Dark Mode")
if dark_mode:

    st.markdown("""
    <style>

    .stApp{
        background-color:#0E1117;
        color:white;
    }

    section[data-testid="stSidebar"]{
        background-color:#111827;
    }

    h1,h2,h3,h4,h5,h6,p,label{
        color:white !important;
    }

    div[data-testid="metric-container"]{
        background:#1E293B;
        color:white;
        border-radius:12px;
        border:1px solid #334155;
    }

    .stButton>button{
        background:#2563EB;
        color:white;
        border-radius:8px;
    }

    </style>
    """, unsafe_allow_html=True)





st.sidebar.markdown("---")

st.sidebar.success("🟢 System Ready")

st.sidebar.write("Machine Learning : ✅")

st.sidebar.write("Analytics : ✅")

st.sidebar.write("AI Assistant : ✅")

st.sidebar.write("Reports : ✅")

st.sidebar.markdown("---")

st.sidebar.info(
    "Version 2.0"
)






# ==========================================================
# DASHBOARD FUNCTION
# ==========================================================

def dashboard():

    today = datetime.now().strftime("%d %B %Y")

    current_time = datetime.now().strftime("%I:%M %p")

    st.markdown(
        '<p class="big-title">🏥 Smart Hospital Analytics & AI Healthcare System</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-title">AI Powered Disease Prediction & Healthcare Analytics Platform</p>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"📅 Date : {today}")

    with col2:
        st.info(f"🕒 Time : {current_time}")

    st.markdown("---")

    st.subheader("👨‍⚕️ Welcome Doctor")

    st.write("""
This dashboard helps healthcare professionals analyze patient records,
predict diseases using Machine Learning, visualize hospital statistics,
and generate patient reports.

Use the navigation menu from the sidebar to access different modules.
""")

    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("👨 Total Patients", "1250", "+12")

    c2.metric("😊 Healthy", "600", "+8")

    c3.metric("🩺 Diabetes", "410", "+6")

    c4.metric("❤️ Heart Disease", "240", "+3")

    st.markdown("---")

    st.subheader("🚀 Project Modules")

    a, b = st.columns(2)

    with a:

        st.success("✔ Disease Prediction")

        st.success("✔ AI Health Assistant")

        st.success("✔ Analytics Dashboard")

    with b:

        st.success("✔ Reports")

        st.success("✔ Machine Learning")

        st.success("✔ PDF Download")

    st.markdown("---")

    st.subheader("💻 Technology Stack")

    t1, t2, t3, t4 = st.columns(4)

    t1.info("🐍 Python")

    t2.info("📊 Pandas")

    t3.info("🤖 Scikit-Learn")

    t4.info("🌐 Streamlit")

    st.markdown("---")

    st.markdown(
        '<p class="footer">Developed by Team: Vikesh Pal, Amarjeet Kumar, Shivam Kumar, Chhotan Kumar | AI & Data Science</p>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.success("🟢 Machine Learning Model Connected Successfully")

    st.success("🤖 AI Health Assistant Active")

    st.success("📊 Analytics Module Ready")

    st.success("📄 Report Module Ready")

def disease_prediction():

    st.title("🤖 Health Prediction")

    st.markdown("---")

    left, right = st.columns(2)

    with left:

        patient_name = st.text_input("Patient Name")

        age = st.number_input("Age",1,100)

        gender = st.selectbox(
            "Gender",
            ["Male","Female"]
        )

        bp = st.number_input("Blood Pressure")

        sugar = st.number_input("Sugar Level")

    with right:

        bmi = st.number_input("BMI")

        heart_rate = st.number_input("Heart Rate")

        smoking = st.selectbox(
            "Smoking",
            ["Yes","No"]
        )

        alcohol = st.selectbox(
            "Alcohol",
            ["Yes","No"]
        )

        exercise = st.selectbox(
            "Exercise",
            ["High","Medium","Low"]
        )

    st.markdown("---")

    if st.button("🔍 Predict Disease"):

        gender = 1 if gender == "Male" else 0

        smoking = 1 if smoking == "Yes" else 0

        alcohol = 1 if alcohol == "Yes" else 0

        exercise_map = {
            "High": 0,
            "Low": 1,
            "Medium": 2
        }

        exercise = exercise_map[exercise]

        # -----------------------------
        # Age Group
        # -----------------------------

        if age <= 35:
            age_group = 2
        elif age <= 55:
            age_group = 0
        else:
            age_group = 1

        # -----------------------------
        # BMI Category
        # -----------------------------

        if bmi < 18.5:
            bmi_category = 3
        elif bmi < 25:
            bmi_category = 1
        elif bmi < 30:
            bmi_category = 2
        else:
            bmi_category = 0

        # -----------------------------
        # Create DataFrame
        # -----------------------------

        new_patient = pd.DataFrame({

            "Age": [age],
            "Gender": [gender],
            "Blood_Pressure": [bp],
            "Sugar_Level": [sugar],
            "BMI": [bmi],
            "Heart_Rate": [heart_rate],
            "Smoking": [smoking],
            "Alcohol": [alcohol],
            "Exercise": [exercise],
            "Age_Group": [age_group],
            "BMI_Category": [bmi_category]

        })

        # -----------------------------
        # Prediction
        # -----------------------------

        prediction = model.predict(new_patient)

        confidence = model.predict_proba(new_patient)

        confidence_score = confidence.max() * 100

        disease_map = {
            0: "Diabetes",
            1: "Healthy",
            2: "Heart Disease"
        }

        predicted_disease = disease_map[prediction[0]]

# ==========================================
# SAVE DATA FOR REPORT
# ==========================================

        st.session_state["patient_name"] = patient_name
        st.session_state["disease"] = predicted_disease
        st.session_state["confidence"] = confidence_score

        st.success("Prediction Completed Successfully ✅")

        st.markdown("---")

        st.subheader("🩺 Prediction Result")

        st.write(f"### 👤 Patient : {patient_name}")

        st.write(f"### 🦠 Disease : {predicted_disease}")

        st.write(f"### 🎯 Confidence : {confidence_score:.2f}%")

        if predicted_disease == "Healthy":

            st.success("🟢 Patient appears Healthy")

        elif predicted_disease == "Diabetes":

            st.error("🔴 Diabetes Risk Detected")

        elif predicted_disease == "Heart Disease":

            st.error("❤️ Heart Disease Risk Detected")


 # =====================================================
# AI HEALTH ASSISTANT
# =====================================================

        st.markdown("---")

        st.subheader("🤖 AI Health Assistant")

        if predicted_disease == "Healthy":

            st.success("🎉 Your health condition looks normal.")

            st.info("""
        ### 🥗 Diet Suggestions

        ✅ Eat fresh fruits

        ✅ Green vegetables

        ✅ Protein rich food

        ✅ Drink 2-3 litres of water
        """)

            st.info("""
        ### 🏃 Exercise

        • Walk 30 minutes daily

        • Light Yoga

        • Stretching
        """)

            st.success("""
        ### 💡 Recommendation

        ✔ Continue your healthy lifestyle.

        ✔ Get regular health checkups every year.
        """)

        elif predicted_disease == "Diabetes":

            st.error("⚠ Diabetes Risk Detected")

            st.info("""
        ### 📖 Disease Explanation

        Diabetes occurs when blood sugar remains higher than normal.
        """)

            st.info("""
        ### 🥗 Diet

        ✅ Oats

        ✅ Brown Rice

        ✅ Green Vegetables

        ✅ High Fiber Foods
        """)

            st.warning("""
        ### ❌ Avoid

        • Cold Drinks

        • Sugar

        • Cakes

        • Chocolates
        """)

            st.info("""
        ### 🏃 Exercise

        ✔ Walk 45 Minutes

        ✔ Cycling

        ✔ Yoga
        """)

            st.error("""
        ### ⚠ Warning Signs

        • Frequent Urination

        • Excessive Thirst

        • Blurred Vision
        """)

        elif predicted_disease == "Heart Disease":

            st.error("❤️ Heart Disease Risk Detected")

            st.info("""
        ### 📖 Disease Explanation

        Heart disease affects blood circulation and heart functioning.
       """)

            st.info("""
        ### 🥗 Diet

        ✅ Fruits

        ✅ Salad

        ✅ Low Salt Food

        ✅ Whole Grains
        """)

            st.warning("""
        ### ❌ Avoid

        • Fast Food

        • Oily Food

        • Smoking

        • Alcohol
        """)

            st.info("""
        ### 🏃 Exercise

        ✔ Morning Walk

        ✔ Breathing Exercise

        ✔ Yoga
        """)
  
            st.error("""
        ### 🚨 Emergency Symptoms

        • Chest Pain

        • Shortness of Breath

        • Sweating

        • Dizziness
        """)

        st.markdown("---")

        st.caption("⚠ This AI Assistant provides educational suggestions only and is NOT a replacement for professional medical advice.")
        

        st.balloons()

        st.success("✅ Prediction Generated Successfully")









def analytics():

    st.title("📊 Hospital Analytics Dashboard")

    st.markdown("---")

    patient_data = pd.DataFrame({

        "Disease": ["Healthy", "Diabetes", "Heart Disease"],

        "Patients": [600, 410, 240]

    })

    st.subheader("Disease Statistics")

    st.bar_chart(patient_data.set_index("Disease"))

    st.markdown("---")

    st.subheader("Hospital Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("👨 Total Patients", "1250")

    col2.metric("🩺 Diseases", "650")

    col3.metric("😊 Healthy", "600")





def reports():

    st.title("📄 Patient Report")

    st.markdown("---")

    if "patient_name" not in st.session_state:

        st.warning("⚠ Please predict a disease first.")

        return

    patient_name = st.session_state["patient_name"]
    disease = st.session_state["disease"]
    confidence = st.session_state["confidence"]

    st.success("Patient Report Ready ✅")

    st.write(f"👤 Patient : {patient_name}")
    st.write(f"🩺 Disease : {disease}")
    st.write(f"🎯 Confidence : {confidence:.2f}%")

    if st.button("📄 Generate PDF"):

        pdf_file = create_pdf(
            patient_name,
            disease,
            confidence
        )

        with open(pdf_file, "rb") as pdf:

            st.download_button(

                "📥 Download PDF Report",

                pdf,

                file_name="Patient_Report.pdf",

                mime="application/pdf"

            )

        st.success("✅ PDF Generated Successfully")




def about():

    st.title("ℹ ABOUT")

    st.markdown("---")

    st.subheader("🏥 SMART HOSPITAL ANALYTICS & AI HEALTHCARE SYSTEM")

    st.write("""
The Smart Hospital Analytics & AI Healthcare System is a Machine Learning based healthcare application developed to analyze patient health records and predict diseases using Artificial Intelligence.

This project provides an easy-to-use dashboard where users can enter patient details, receive disease predictions, view hospital analytics, and download patient reports.

The objective of this project is to demonstrate how Data Analytics and Machine Learning can improve healthcare decision-making and support doctors with quick insights.

This project is developed for educational purposes and should not be considered a replacement for professional medical diagnosis.
""")

    st.markdown("---")

    st.subheader("✨ Features")

    st.success("✔ Disease Prediction using Machine Learning")
    st.success("✔ AI Health Assistant")
    st.success("✔ Hospital Analytics Dashboard")
    st.success("✔ Download Patient Report")
    st.success("✔ Professional Dashboard")

    st.markdown("---")

    st.subheader("🛠 Technologies Used")

    st.write("""
• Python

• Pandas

• NumPy

• Scikit-Learn

• Streamlit

• Joblib

• Matplotlib
""")

    st.markdown("---")

    st.subheader("👨‍💻 Team Members")

    st.info("""
1. Vikesh Pal

2. Amarjeet Kumar

3. Shivam Kumar

4. Chhotan Kumar

Course : B.Tech (Artificial Intelligence & Data Science)

College : IES College of Technology, Bhopal
""")



# ==========================================================
# PAGE ROUTER
# ==========================================================

if menu == "🏠 Dashboard":

    dashboard()

elif menu == "🤖 Health Prediction":

    disease_prediction()

elif menu == "📊 Analytics":

    analytics()

elif menu == "📄 Reports":

    reports()

elif menu == "ℹ About":

    about()
