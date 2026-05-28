import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="VISION-LINK OS", layout="wide", page_icon="🛡️")

# CSS for Monday.com Vibes
st.markdown("""
    <style>
    /* Global Styles */
    .stApp { background-color: #f6f7f8; }
    
    /* Card Component */
    .card { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 10px; 
        border: 1px solid #e0e0e0; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] { background-color: #fcfcfc; }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #ffffff; border-radius: 8px; border: 1px solid #e0e0e0; }
    </style>
""", unsafe_allow_html=True)

# Sidebar - Professional Menu
with st.sidebar:
    st.markdown("## 🛡️ SECURITY OPS")
    st.caption("AI Threat Detection System")
    st.markdown("---")
    
    menu_items = {
        "Operations Overview": "📊",
        "Camera Feeds": "📷",
        "Location Risk": "📍",
        "Incident Log": "⚠️",
        "Dispatch Center": "📻",
        "Evidence Archive": "📂",
        "Ultralytics HUB": "⚡",
        "Live Detection": "🎯",
        "Presentation": "📈"
    }
    
    selected_menu = st.radio("Navigation", list(menu_items.keys()), 
                             format_func=lambda x: f"{menu_items[x]} {x}")
    
    st.markdown("---")
    st.success("System Status: Active")
    st.write("Live Connection")

# Main Interface
st.title(f"{menu_items.get(selected_menu, '🛡️')} {selected_menu}")

# Dashboard Logic
if selected_menu == "Operations Overview":
    # Metrics
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="card"><h3>Total Incidents</h3><h1>25</h1><p>21 active detections</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="card"><h3>Active Dispatches</h3><h1>5</h1><p>1 pending response</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="card"><h3>Camera Status</h3><h1>3/6</h1><p>50% operational</p></div>', unsafe_allow_html=True)
    
    # Graphs
    st.markdown('<div class="card"><h3>Incidents by Severity</h3>', unsafe_allow_html=True)
    st.bar_chart(pd.DataFrame([2, 2, 11, 10], index=["High", "Critical", "Medium", "Low"]))
    st.markdown('</div>', unsafe_allow_html=True)

elif selected_menu == "Live Detection":
    st.warning("Live AI Model: System Initializing...")
    st.markdown('<div class="card"><h3>Model Performance</h3><p>Model: YOLOv8n (87.5% mAP50)</p></div>', unsafe_allow_html=True)

else:
    st.info(f"The {selected_menu} module is under active development.")
    st.markdown('<div class="card"><h3>Work in Progress</h3><p>Stay tuned for updates.</p></div>', unsafe_allow_html=True)
    
