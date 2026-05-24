import streamlit as st

st.set_page_config(page_title="Sana Pinjari Portfolio", layout="wide")

# CSS Styling
st.markdown("""
    <style>
    .stApp { background-color: #1a1f2e; color: white; }
    h1, h2, h3 { color: #d4af37 !important; }
    .skill-card { background-color: #252d3d; padding: 20px; border-radius: 10px; border: 1px solid #d4af37; height: 260px; }
    .project-card { border: 1px solid #d4af37; padding: 20px; border-radius: 10px; margin-bottom: 20px; background-color: #252d3d; }
    </style>
""", unsafe_allow_html=True)

# 1. Header
st.title("SANA PINJARI")
st.subheader("Data Analyst & Business Intelligence Specialist")
st.write("---")

# 2. About
col1, col2 = st.columns([1, 2])
with col1:
    st.image("my_photo.png", use_container_width=True)
with col2:
    st.header("About Me")
    st.write("Passionate data professional dedicated to uncovering insights and driving growth. My journey has equipped me with strong technical skills in SQL, Python, Excel, Power BI, and Tableau. I excel at identifying patterns and solving complex business problems.")

# 3. Technical Skills
st.write("---")
st.header("Technical Skills")
skills = [
    ("📊 Data Analysis", "Expert in exploratory data analysis, statistical testing, pattern recognition, and data profiling."),
    ("🗄️ SQL", "Advanced query writing, database design, optimization, Window Functions, and CTEs."),
    ("🐍 Python", "Data manipulation with Pandas, NumPy, Matplotlib, Scikit-learn, and automation."),
    ("📈 Power BI", "Dashboard design, DAX formulas, data modeling, interactive reports, and KPI tracking."),
    ("📉 Tableau", "Data visualization, dashboards, calculated fields, and data storytelling."),
    ("📋 Excel", "Advanced formulas, Pivot Tables, VBA, data cleaning, and automation."),
    ("📊 Statistics", "Hypothesis testing, regression analysis, probability, and distributions."),
    ("🤖 Machine Learning", "Classification, regression, clustering, model evaluation, and fundamentals.")
]
cols = st.columns(4)
for i, (name, desc) in enumerate(skills):
    with cols[i % 4]:
        st.markdown(f"<div class='skill-card'><b>{name}</b><br><br>{desc}</div>", unsafe_allow_html=True)

# 4. Featured Projects
st.write("---")
st.header("Featured Projects")
projects = [
    ("Swiggy Instamart Analytics", "Swiggy Instamart Analytics.png", "Analysis of operations. 1M+ Orders, 7K+ Stores. Tools: Power BI, SQL, Excel"),
    ("Retail Sales Dashboard", "retail_sales.png", "Multi-year analysis. 4.72B Sales, 316K Units. Tools: Tableau, Python, SQL"),
    ("Zomato Restaurant Insights", "zomato.jpg", "Market analysis, ratings, and performance. 7K Restaurants. Tools: Power BI, Excel, SQL"),
    ("Superstore Sales Dashboard", "superstore_dashboard.jpg", "Data cleaning via Power Query, Pivot Tables, and KPI tracking. Tools: Excel"),
    ("HR Analytics Dashboard", "hr_analytics.jpg", "Employee attrition analysis. 1,470 Employees. Tools: Power BI, SQL, Python")
]
for title, img, desc in projects:
    st.markdown(f"<div class='project-card'><h3>{title}</h3><p>{desc}</p></div>", unsafe_allow_html=True)
    st.image(img, use_container_width=True)

# 5. Certifications & Contact
st.write("---")
st.header("Certifications & Contact")
st.write("✅ Google Data Analytics | ✅ SQL | ✅ Power BI Specialist | ✅ Python | ✅ Tableau | ✅ Statistics")
c1, c2, c3 = st.columns(3)
with c1: st.link_button("📧 Email Me", "mailto:binzer.pinjari007@gmail.com")
with c2: st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/sana-pinjari-analytics/")
with c3: st.link_button("💻 GitHub", "https://github.com/binzerpinjari007-cell")
