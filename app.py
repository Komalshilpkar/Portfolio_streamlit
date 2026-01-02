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
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}
.fade-in { animation: fadeIn 0.8s ease-in-out; }

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
    ["🏠 Home", "👩‍💼 About", "🛠 Skills", "📂 Projects", "🖼 Screenshots", "📜 Certifications", "📞 Contact"]
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
    st.markdown('<div class="card fade-in">', unsafe_allow_html=True)
    st.write("""
    👋 Welcome to my **interactive AI/ML portfolio**.

    I build **real-world machine learning systems**, deploy them with **Streamlit**,
    and focus on **data-driven decision-making** using AI models.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= ABOUT =================
elif section == "👩‍💼 About":
    st.markdown('<div class="card fade-in">', unsafe_allow_html=True)
    st.write("""
    🎯 **Career Objective**

    Motivated AI/ML and Data Science professional seeking opportunities to
    build intelligent, scalable, and impactful data-driven applications.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= SKILLS =================
elif section == "🛠 Skills":
    st.markdown("### 💡 Technical Skills")
    st.markdown("""
    <span class="badge">Python</span>
    <span class="badge">Machine Learning</span>
    <span class="badge">Deep Learning</span>
    <span class="badge">LSTM</span>
    <span class="badge">CNN</span>
    <span class="badge">Streamlit</span>
    <span class="badge">Power BI</span>
    <span class="badge">Git & GitHub</span>
    """, unsafe_allow_html=True)

# ================= PROJECTS =================
elif section == "📂 Projects":
    st.markdown("## 📈 AI-Driven Stock Market Prediction System")

    st.write("""
    ✔ LSTM-based 10-day price forecasting  
    ✔ RSI, MACD & Bollinger Bands  
    ✔ Buy / Sell / Hold AI decision engine  
    ✔ Backtesting & equity curve  
    ✔ Investment summary & reports  
    """)

    st.markdown("🔗 **Live App:** https://nandinistock-x6hbjqmh5qdzrn5v2vmappn.streamlit.app/")
    st.markdown("🔗 **GitHub:** https://github.com/Komalshilpkar")

    st.markdown("---")

    st.markdown("## 🧠 CNN Convolution & Pooling Visualizer")

    st.write("""
    ✔ Step-by-step convolution & pooling animation  
    ✔ Editable kernels, stride & padding  
    ✔ Educational deep learning visualizer  
    """)

    st.markdown("🔗 **Live App:** https://komalshilpkar.github.io/cnn-convolution-visualizer-clean/")
    st.markdown("🔗 **GitHub:** https://github.com/Komalshilpkar")

# ================= SCREENSHOTS =================
elif section == "🖼 Screenshots":
    st.markdown("## 📸 Project Screenshots")

    image_files = [
        "1767370611681.jpg","1767370611694.jpg","1767370611705.jpg",
        "1767370611720.jpg","1767370611731.jpg","1767370611744.jpg",
        "1767370611759.jpg","1767370611772.jpg","1767370611783.jpg",
        "1767370611797.jpg","1767370611811.jpg","1767370611825.jpg",
        "1767370611837.jpg","1767370611848.jpg","1767370611862.jpg",
        "1767370611873.jpg","1767370611883.jpg","1767370611898.jpg"
    ]

    cols = st.columns(3)
    idx = 0
    for img in image_files:
        path = f"assets/{img}"
        if os.path.exists(path):
            cols[idx % 3].image(path, use_container_width=True)
            idx += 1

# ================= CERTIFICATIONS =================
elif section == "📜 Certifications":
    st.write("""
    🏅 **AI & Machine Learning – IIT Delhi**  
    🏅 **Programming – Protec Consultancy**  
    🏅 **Data & Analytics – Satish Dhawale**
    """)

# ================= CONTACT =================
elif section == "📞 Contact":
    st.write("📧 Email: nandinishilpkar00@gmail.com")
    st.write("📞 Phone: 7071337033")
    st.write("🔗 GitHub: https://github.com/Komalshilpkar")
    st.write("🔗 LinkedIn: https://www.linkedin.com/in/nandini-s-836ba55b")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🚀 Built with Streamlit | Nandini Shilpkar")
