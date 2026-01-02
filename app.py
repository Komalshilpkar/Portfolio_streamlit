import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Nandini Shilpkar | Data Science Portfolio",
    page_icon="👩‍💻",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "About Me",
        "Skills",
        "Projects",
        "ML Demo",
        "Certifications",
        "Contact"
    ]
)

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style='color:#0A66C2;'>Nandini Shilpkar</h1>
    <h4>AI/ML & Data Science Professional</h4>
    """,
    unsafe_allow_html=True
)

st.write(
    "📍 Lucknow, Uttar Pradesh | 📧 nandinishilpkar00@gmail.com | 📞 7071337033"
)

st.markdown("---")

# ---------------- ABOUT ----------------
if page == "About Me":
    st.header("👋 About Me")

    st.write("""
    Motivated **AI/ML and Data Science professional** with a B.Tech in Computer Science & Engineering.
    Strong foundation in **Python, data analysis, machine learning, and visualization**, with hands-on
    experience building **interactive dashboards and ML simulators**.

    Certified in **Applied AI & Machine Learning from IIT Delhi**, actively seeking roles as a
    **Data Scientist, Data Analyst, or AI/ML Engineer**.
    """)

# ---------------- SKILLS ----------------
elif page == "Skills":
    st.header("🛠 Technical Skills")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Programming")
        st.write("- Python\n- Java\n- C/C++\n- JavaScript\n- .NET")

    with col2:
        st.subheader("Data & Analytics")
        st.write("- Pandas\n- NumPy\n- Excel\n- Data Cleaning\n- Feature Engineering")

    with col3:
        st.subheader("ML, DL & Tools")
        st.write("- Machine Learning\n- CNN (Conceptual)\n- Power BI\n- Streamlit\n- Git & GitHub")

# ---------------- PROJECTS ----------------
elif page == "Projects":
    st.header("📂 Projects")

    # ---- Stock Dashboard ----
    st.subheader("📈 Stock Market Analysis Dashboard")
    st.image("assets/stock_dashboard.png", caption="Stock Market Dashboard", use_container_width=True)

    st.write("""
    **Objective:** Analyze and visualize stock market trends.

    **Key Features:**
    - Data cleaning & exploratory analysis
    - RSI, MACD, Moving Averages, Bollinger Bands
    - Interactive real-time Streamlit dashboard
    """)

    st.markdown("🔗 GitHub: https://github.com/Komalshilpkar")
    st.markdown("🌐 Live App: (add your Streamlit link)")

    st.markdown("---")

    # ---- CNN Simulator ----
    st.subheader("🧠 CNN Convolution & Pooling Simulator")
    st.image("assets/cnn_simulator.png", caption="CNN Simulator", use_container_width=True)

    st.write("""
    **Objective:** Explain CNN working visually.

    **Key Features:**
    - Convolution & pooling step-by-step simulation
    - Interactive kernel & layer controls
    - Educational visualization tool
    """)

    st.markdown("🔗 GitHub: https://github.com/Komalshilpkar")
    st.markdown("🌐 Live App: (add simulator link if deployed)")

# ---------------- ML DEMO ----------------
elif page == "ML Demo":
    st.header("🧠 Machine Learning Prediction Demo")

    st.write("Simulated **Regression Model Deployment**")

    experience = st.slider("Years of Experience", 0, 10, 2)
    projects = st.slider("Number of Projects", 0, 20, 5)

    # Simulated trained model logic
    prediction = (experience * 8) + (projects * 2) + 30

    st.success(f"📊 Predicted Performance Score: **{prediction:.2f}**")

    st.info("This demo showcases ML logic + Streamlit deployment skills.")

# ---------------- CERTIFICATIONS ----------------
elif page == "Certifications":
    st.header("📜 Certifications")

    st.markdown("""
    ✅ **AI & Machine Learning – IIT Delhi**  
    - Supervised & unsupervised learning  
    - Model evaluation & AI use cases  

    ✅ **Programming – Protec Consultancy**  
    - Python, Java, .NET fundamentals  

    ✅ **Data & Analytics – Satish Dhawale**  
    - Advanced Excel & Power BI dashboards  
    """)

# ---------------- CONTACT ----------------
elif page == "Contact":
    st.header("📞 Contact & Links")

    st.write("📧 Email: nandinishilpkar00@gmail.com")
    st.write("📞 Phone: 7071337033")
    st.write("🔗 GitHub: https://github.com/Komalshilpkar")
    st.write("🔗 LinkedIn: https://www.linkedin.com/in/nandini-s-836ba55b")
