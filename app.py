import streamlit as st

# Page Setup
st.set_page_config(page_title="VISION-LINK OS", layout="wide")

# CSS don tsarin Monday.com
st.markdown("""
    <style>
    .main { background-color: #f6f7f8; }
    .card { background-color: #ffffff; padding: 20px; border-radius: 8px; border: 1px solid #dcdcdc; margin-bottom: 20px; }
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] { background-color: #ffffff; border-radius: 5px; padding: 10px 20px; }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.title("🛡️ VISION-LINK OS")
st.subheader("Welcome to your Command Center")

# Tabs kamar yadda yake a Monday.com (Workspaces)
tab1, tab2, tab3 = st.tabs(["📊 Overview", "📷 Camera Feeds", "⚠️ Incidents"])

with tab1:
    st.markdown('<div class="card"><h3>Active Operations</h3><p>System is running at 98% efficiency.</p></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Threats", "0", delta="0")
    col2.metric("Camera Status", "Online", delta="Stable")
    col3.metric("AI Model", "Active", delta="v2.4")

with tab2:
    st.markdown('<div class="card"><h3>Live Camera Feeds</h3><p>Feed 1: Parking Lot - Active</p></div>', unsafe_allow_html=True)
    st.info("Waiting for video stream...")

with tab3:
    st.markdown('<div class="card"><h3>Incident Log</h3><p>No recent incidents reported.</p></div>', unsafe_allow_html=True)
