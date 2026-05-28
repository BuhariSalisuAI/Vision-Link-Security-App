import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="VISION-LINK OS", layout="wide")

# 2. Advanced CSS for Monday.com Vibes
st.markdown("""
    <style>
    .stApp { background-color: #f6f7f8; }
    .card { background-color: #ffffff; padding: 20px; border-radius: 8px; border: 1px solid #e0e0e0; box-shadow: 0 1px 2px rgba(0,0,0,0.1); margin-bottom: 20px; }
    .sidebar .stRadio { font-weight: bold; }
    h1 { color: #1a1d21 !important; font-size: 24px !important; }
    h3 { color: #555 !important; font-size: 16px !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar (Left Menu)
with st.sidebar:
    st.markdown("## 🛡️ VISION-LINK OS")
    st.markdown("---")
    menu = st.radio("Navigation", [
        "Operations Overview", "Camera Feeds", "Personal Protection", 
        "Location Risk", "Incident Log", "Live Detection"
    ])
    st.markdown("---")
    st.info("System Ready")

# 4. Main Interface (Grid Layout)
col1, col2 = st.columns([3, 1]) # Raba shafin gida biyu (Grid)

with col1:
    st.title(f"📊 {menu}")
    
    if menu == "Operations Overview":
        # Metrics Row
        m1, m2, m3 = st.columns(3)
        m1.metric("Incidents", "25", "12%")
        m2.metric("Dispatches", "5", "0")
        m3.metric("Camera", "3/6", "50%")
        
        st.markdown('<div class="card"><h3>Severity Distribution</h3></div>', unsafe_allow_html=True)
        df = pd.DataFrame({'S': ['High', 'Critical', 'Medium', 'Low'], 'C': [2, 2, 11, 10]})
        fig = px.bar(df, x='S', y='C', color='S')
        st.plotly_chart(fig, use_container_width=True)

with col2:
    # Right Sidebar (AI Insights Panel)
    st.markdown('<div class="card"><h3>🤖 AI Insights</h3><p>System is stable.</p><hr><p><b>Last Update:</b> 10:32 AM</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>🚀 Deployment</h3><p>Kaduna Conference OS: <b>Active</b></p></div>', unsafe_allow_html=True)
    
