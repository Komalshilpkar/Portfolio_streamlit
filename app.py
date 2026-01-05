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

/* Reduce top Streamlit header height */
header[data-testid="stHeader"] {
    height: 3rem !important;
    padding: 0.2rem 1rem !important;
}

/* Reduce default Streamlit side margins */
.block-container {
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    padding-top: 0.6rem !important;
    max-width: 100% !important;
}

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

    I focus on building **real-world machine learning and Generative AI applications**,
    deploying them as interactive tools, and explaining complex AI concepts
    in a clear and practical way.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= ABOUT =================
elif section == "👩‍💼 About":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("""
    Motivated **AI/ML and Data Science professional** seeking an opportunity to apply
    strong programming, data analysis, and machine learning skills in building
    intelligent, data-driven solutions.

    I have hands-on experience in developing **analytical dashboards** and a
    **Retrieval-Augmented Generation (RAG) based AI application** for
    document-driven question answering, and I am eager to contribute to real-world
    AI projects while growing as an **AI/ML Engineer or Data Scientist**.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= SKILLS =================
elif section == "🛠 Skills":
    st.markdown("## 🛠 Skills & Technical Expertise")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🐍 Programming")
    st.write("""
    Python, Java, C/C++, JavaScript, and .NET with strong fundamentals,
    object-oriented programming concepts, and logical problem-solving skills.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📊 Data & Analytics")
    st.write("""
    Pandas, NumPy, and Excel with experience in data cleaning,
    preprocessing, feature engineering, exploratory data analysis,
    and basic statistical techniques.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🤖 Machine Learning")
    st.write("""
    Supervised learning techniques including classification and regression,
    along with model evaluation, validation, and performance assessment.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🧠 Generative AI & RAG")
    st.write("""
    Retrieval-Augmented Generation (RAG) using LangChain, including
    document ingestion, text chunking, vector embeddings, FAISS similarity search,
    prompt engineering, and context-aware response generation for
    document-based question answering systems.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🧠 Deep Learning (Conceptual)")
    st.write("""
    Understanding of CNN architecture including convolution, pooling,
    and feature maps, demonstrated through an interactive simulator.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📊 Visualization & BI")
    st.write("""
    Power BI, Matplotlib, Seaborn, and Streamlit for building dashboards
    and analytical visualizations.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= PROJECTS =================
elif section == "📂 Projects":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📈 Stock Market Analysis Dashboard | Python, Streamlit | Live")
    st.write("""
    • Data cleaning, preprocessing, and exploratory data analysis  
    • RSI, MACD, Moving Averages, and Bollinger Bands implementation  
    """)
    st.markdown("🔗 Live App: https://nandinistock-x6hbjqmh5qdzrn5v2vmappn.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🧠 CNN Simulator (Web-based Visualization Tool) | Live")
    st.write("""
    • Step-by-step simulation of convolution and pooling layers  
    • Interactive educational tool for understanding CNN concepts  
    """)
    st.markdown("🔗 Live App: https://komalshilpkar.github.io/cnn-convolution-visualizer-clean/")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📄 RAG-based AI Chatbot (Document Question Answering) | Live")
    st.write("""
    • Retrieval-Augmented Generation for document-based question answering  
    • FAISS vector similarity search with embeddings and LLM-based response generation  
    """)
    st.markdown("🔗 Live App: https://ragprojec.streamlit.app/")
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

