import streamlit as st
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="Akshay Kumar Bagde | Data Scientist", layout="centered", initial_sidebar_state="expanded")

# --- Dark Mode Toggle ---
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #1e1e1e;
            color: white;
        }
        .stApp {
            animation: fadein 1s;
        }
        @keyframes fadein {
            from { opacity: 0; }
            to   { opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar: Contact & Photo ---
photo_url = "https://raw.githubusercontent.com/Akshayk69/<your-repo>/main/akshay_photo.jpg"  # Update this path
st.sidebar.image(photo_url, width=200, caption="Akshay Kumar Bagde")
st.sidebar.markdown("📧 [akshaybagde0805@gmail.com](mailto:akshaybagde0805@gmail.com)")
st.sidebar.markdown("📞 +91 9823459330")
st.sidebar.markdown("🌐 [LinkedIn](http://www.linkedin.com/in/akshaykumarbagde)")
st.sidebar.markdown("💻 [GitHub](https://github.com/Akshayk69)")

# --- Main Section ---
st.title("Akshay Kumar Bagde")
st.subheader("🚀 Data Scientist | ML & Gen AI | Forecasting | NLP | Optimization")

st.markdown("""
Experienced Data Scientist with over 2.5 years in designing machine learning models, demand forecasting engines,
optimization pipelines, and NLP applications. Adept at translating business goals into intelligent data products
across large-scale operations.
""")

# --- Skills ---
st.markdown("### 💼 Skills & Tools")
st.markdown("""
- **Languages & Frameworks**: Python, PySpark, SQL, Pandas, NumPy  
- **Machine Learning**: Scikit-learn, XGBoost, LSTM, CNN, Keras, FBProphet  
- **Data Visualization**: Power BI, Seaborn, Excel  
- **NLP**: NLTK, Sentiment Analysis, Web Scraping  
""")

# --- Projects ---
st.markdown("### 📊 Projects")

st.markdown("**🧠 Demand Forecast Engine Utility (FEU)** – *EY*")
st.markdown("""
Built from scratch using ML + FBProphet for 10K+ FMCG SKUs.  
Boosted business accuracy by 20% and enabled auto-scaling with Azure Databricks.
""")

st.markdown("**📦 Delivery Optimization Engine** – *EY*")
st.markdown("""
Minimized cost & time in distribution logistics using probabilistic models and decision trees.  
Delivered measurable operational gains across client verticals.
""")

st.markdown("**🤖 Resume Ranker GenAI** *(Personal Project)*")
st.markdown("""
Developed an LLM-driven Streamlit tool that parses resumes and ranks them based on job descriptions  
using OpenAI's GPT-4, LangChain, and vector embeddings for semantic similarity.  
👉 [GitHub Repo](https://github.com/Akshayk69/resume-ranker)
""")

# --- Work Experience ---
st.markdown("### 🧠 Work Experience")

st.markdown("**Data Scientist – Ernst & Young**  \n*Oct 2022 – Present*")
st.markdown("""
- Developed scalable AI solutions for supply chain demand forecasting and KPI optimization.  
- Collaborated across business, engineering & analytics teams for ML pipeline deployment.
""")

st.markdown("**Consultant – Design Center**  \n*Sep 2014 – May 2015*")
st.markdown("""
- Led transformation projects for MSMEs through tailored analytics interventions.
""")

# --- Education ---
st.markdown("### 🎓 Education")
st.markdown("**M.Tech – NIT Warangal**  \nSystem Engineering Design (2016 – 2018)")
st.markdown("**PG Certificate in Data Science – Manipal Academy**  \nDec 2021 – Jun 2022 | CGPA: 9.32/10")

# --- Languages ---
st.markdown("### 🌍 Languages")
st.markdown("English, Hindi, Marathi")

# --- Download Resume ---
with open("latest_Akshay Kumar Bagde.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="📄 Download Resume (PDF)", data=PDFbyte, file_name="Akshay_Bagde_Resume.pdf", mime='application/pdf')
