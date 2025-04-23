import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Akshay Kumar Bagde | Data Scientist", layout="centered")

# Sidebar with contact info
st.sidebar.image("https://avatars.githubusercontent.com/u/77186098?v=4", width=150)
st.sidebar.markdown("### Akshay Kumar Bagde")
st.sidebar.markdown("📧 [akshaybagde0805@gmail.com](mailto:akshaybagde0805@gmail.com)")
st.sidebar.markdown("📞 +91 9823459330")
st.sidebar.markdown("🌐 [LinkedIn](http://www.linkedin.com/in/akshaykumarbagde)")
st.sidebar.markdown("💻 [GitHub](https://github.com/Akshayk69)")

# --- Header ---
st.title("Akshay Kumar Bagde")
st.subheader("🚀 Data Scientist | ML & Gen AI | Forecasting | NLP | Optimization")

# --- Summary ---
st.markdown("""
Data Scientist with 2.5+ years of experience in Machine Learning, Demand Forecasting, Optimization, and NLP.
Proven track record in improving KPIs, automating ML pipelines, and leveraging AI to solve real-world problems.
""")

# --- Skills ---
st.markdown("### 💼 Skills & Tools")
st.markdown("""
- **Programming & Analysis**: Python, PySpark, SQL, Pandas, NumPy, Excel
- **ML & AI**: Scikit-learn, XGBoost, Keras, CNN, LSTM, FBProphet
- **Visualization & BI**: Power BI, Seaborn
- **NLP**: NLTK, Sentiment Analysis, Data Scraping
""")

# --- Work Experience ---
st.markdown("### 🧠 Work Experience")

st.markdown("**Data Scientist – Ernst & Young**  \n*Oct 2022 – Present*")
st.markdown("""
- Developed Forecast Engine Utility for 10K+ FMCG SKUs.
- Used regression, XGBoost, FBProphet for demand prediction.
- Collaborated across teams using Azure Databricks to automate pipelines.
- Led optimization initiatives that reduced logistics cost & time.
""")

st.markdown("**Consultant – Design Center**  \n*Sep 2014 – May 2015*")
st.markdown("""
- Delivered strategy consulting for MSMEs.
- Implemented data-driven improvements across operational flows.
""")

# --- Education ---
st.markdown("### 🎓 Education")
st.markdown("**M.Tech – National Institute of Technology, Warangal**  \n*System Engineering Design (2016 – 2018)*")
st.markdown("**PG Certificate in Data Science & ML – Manipal Academy**  \n*Dec 2021 – Jun 2022*  \nCGPA: 9.32/10")

# --- Languages ---
st.markdown("### 🌍 Languages")
st.markdown("English, Hindi, Marathi")

# --- Resume Download ---
with open("latest_Akshay Kumar Bagde.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="📄 Download Resume (PDF)", data=PDFbyte, file_name="Akshay_Bagde_Resume.pdf", mime='application/pdf')
