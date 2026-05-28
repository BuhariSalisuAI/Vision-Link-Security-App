import streamlit as st
import pandas as pd
import plotly.express as px

# Page Setup
st.set_page_config(page_title="VISION-LINK OS", layout="wide")

# CSS 
st.markdown("""
    <style>
    .stApp { background-color: #f6f7f8; }
    .card { background-color: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #dcdcdc; margin-bottom: 20px; color: #000000; }
    h1, h2, h3, p { color: #000000 !important; }
    </style>
""", unsafe_allow_html=True)

# Sidebar - Menu mai Personal Protection
with st.sidebar:
    st.markdown("## 🛡️ SECURITY OPS")
    st.caption("AI Threat Detection System")
    st.markdown("---")
    
    menu_options = [
        "Operations Overview", "Camera Feeds", "Personal Protection", 
        "Location Risk", "Incident Log", "Dispatch Center", 
        "Evidence Archive", "Ultralytics HUB", "Live Detection", "Presentation"
    ]
    
    menu = st.radio("Navigation", menu_options)
    st.markdown("---")
    st.success("System Status: Active")

# Main Interface
st.title(f"📊 {menu}")

# Dashboard Logic - Kowanne menu yana da abin da zai nuna
if menu == "Operations Overview":
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="card"><h3>Total Incidents</h3><h1>25</h1></div>', unsafe_allow_html=True)
    c2.markdown('<div class="card"><h3>Active Dispatches</h3><h1>5</h1></div>', unsafe_allow_html=True)
    c3.markdown('<div class="card"><h3>Camera Status</h3><h1>3/6</h1></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card"><h3>Incidents by Severity</h3>', unsafe_allow_html=True)
    df = pd.DataFrame({'Severity': ['High', 'Critical', 'Medium', 'Low'], 'Count': [2, 2, 11, 10]})
    fig = px.bar(df, x='Severity', y='Count', color='Severity', text_auto=True)
    fig.update_layout(showlegend=False, plot_bgcolor='white', paper_bgcolor='white')
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "Personal Protection":
    st.markdown('<div class="card"><h3>Personal Protection Module</h3><p>Monitoring biometric safety and individual threat levels.</p></div>', unsafe_allow_html=True)

elif menu == "Camera Feeds":
    st.markdown('<div class="card"><h3>Camera Feeds</h3><p>Live stream integration active for all sectors.</p></div>', unsafe_allow_html=True)

else:
    st.markdown(f'<div class="card"><h3>{menu}</h3><p>Module active and monitoring.</p></div>', unsafe_allow_html=True)
    
