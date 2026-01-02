import streamlit as st
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Nandini Shilpkar | Interactive Portfolio",
    page_icon="👩‍💻",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.card {
    background: #ffffff;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    margin-bottom: 25px;
}
.badge {
    display: inline-block;
    background: #e6f0ff;
    color: #0A66C2;
    padding: 6px 14px;
    border-radius: 20px;
    margin: 4px;
    font-size: 14px;
}
.btn {
    background: linear-gradient(90deg,#0A66C2,#0073e6);
    color: white;
    padding: 10px 20px;
    border-radius: 25px;
    text-decoration: none;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Navigation")
section = st.sidebar.radio(
    "",
    ["🏠 Home", "👩‍💼 About", "🛠 Skills", "📂 Projects", "🖼 Screenshots", "📞 Contact"]
)

# ---------------- HEADER ----------------
st.markdown("<h1 style='color:#0A66C2;'>Nandini Shilpkar</h1>", unsafe_allow_html=True)
st.markdown("**AI / ML | Data Science | Python Developer**")
st.write("📍 Lucknow, Uttar Pradesh | 📧 nandinishilpkar00@gmail.com | 📞 7071337033")

st.markdown("""
<a class="btn" href="https://github.com/Komalshilpkar" target="_blank">GitHub</a>
<a class="btn" href="https://www.linkedin.com/in/nandini-s-836ba55b" target="_blank">LinkedIn</a>
""", unsafe_allow_html=True)

st.markdown("---")

# ================= HOME =================
if section == "🏠 Home":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("""
    👋 Welcome to my **interactive AI/ML portfolio**.

    I focus on building **real-world machine learning applications**, deploying them
    as interactive tools, and explaining complex AI concepts in a clear and practical way.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= ABOUT =================
elif section == "👩‍💼 About":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("""
    I am an aspiring **AI/ML and Data Science professional** with a strong foundation
    in computer science, programming, and data analysis. I enjoy working on real-world
    datasets and building intelligent solutions that combine analytical thinking
    with practical deployment.
    
    I have hands-on experience across the full machine learning lifecycle—from data
    preprocessing and modeling to evaluation and deployment using Streamlit.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= SKILLS =================
elif section == "🛠 Skills":
    st.markdown("## 🛠 Skills & Technical Expertise")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🐍 Python Programming")
    st.write("""
    Python is my primary programming language, and I use it extensively for data analysis,
    machine learning, and application development. I focus on writing clean, modular, and
    reusable code that follows best practices.

    I have used Python for data preprocessing, feature engineering, model implementation,
    and deploying complete end-to-end applications using Streamlit.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📊 Data Analysis & Data Science")
    st.write("""
    I have strong experience in data analysis using Pandas and NumPy, including cleaning
    datasets, handling missing values, and performing exploratory data analysis (EDA)
    to identify patterns and trends.

    My data science approach emphasizes understanding the problem context first, followed
    by statistical analysis and meaningful visualization to support decision-making.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🤖 Machine Learning")
    st.write("""
    I have worked with machine learning techniques such as regression, classification,
    and time-series forecasting. I understand the full ML pipeline including training,
    evaluation, and tuning models.

    My focus is on building models that are both accurate and interpretable, rather than
    treating machine learning as a black-box solution.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🧠 Deep Learning (LSTM & CNN)")
    st.write("""
    I have hands-on exposure to deep learning concepts, particularly LSTM models for
    sequential data and CNN fundamentals for image processing.

    To strengthen conceptual clarity, I built interactive visualizations that explain
    convolution and pooling operations step by step.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📈 Time-Series Forecasting")
    st.write("""
    Time-series forecasting is a key area of interest for me, especially in financial data.
    I have applied LSTM-based models to predict future price movements using historical data.

    I understand concepts such as windowing, scaling, and sequence preparation that are
    essential for reliable time-series modeling.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🌐 Streamlit & Deployment")
    st.write("""
    I use Streamlit to convert machine learning models into interactive web applications.
    This allows non-technical users to explore predictions and insights easily.

    I am comfortable deploying applications on Streamlit Cloud and managing dependencies
    through structured project setups.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= PROJECTS =================
elif section == "📂 Projects":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📈 AI-Driven Stock Market Prediction System")
    st.write("""
    LSTM-based forecasting system integrated with RSI, MACD, and Bollinger Bands.
    Includes buy/sell/hold logic, backtesting, and investment summaries.
    """)
    st.markdown("🔗 Live App: https://nandinistock-x6hbjqmh5qdzrn5v2vmappn.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🧠 CNN Convolution & Pooling Visualizer")
    st.write("""
    Interactive educational tool to visualize convolution and pooling operations
    with editable kernels, stride, and padding.
    """)
    st.markdown("🔗 Live App: https://komalshilpkar.github.io/cnn-convolution-visualizer-clean/")
    st.markdown('</div>', unsafe_allow_html=True)

# ================= SCREENSHOTS =================
elif section == "🖼 Screenshots":
    st.markdown("## 📸 Project Screenshots")
    image_files = os.listdir("assets") if os.path.exists("assets") else []
    cols = st.columns(3)
    for i, img in enumerate(image_files):
        cols[i % 3].image(f"assets/{img}", use_container_width=True)

# ================= CONTACT =================
elif section == "📞 Contact":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("📧 Email: nandinishilpkar00@gmail.com")
    st.write("📞 Phone: 7071337033")
    st.write("🔗 GitHub: https://github.com/Komalshilpkar")
    st.write("🔗 LinkedIn: https://www.linkedin.com/in/nandini-s-836ba55b")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🚀 Built with Streamlit | Nandini Shilpkar")
