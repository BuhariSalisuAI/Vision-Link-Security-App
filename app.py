import streamlit as st
import pandas as pd

# Page Setup
st.set_page_config(page_title="VISION-LINK OS", layout="wide", page_icon="🛡️")

# CSS - An tabbatar da rubutu ya zama baƙi koyaushe don kaucewa farin allo
st.markdown("""
    <style>
    .stApp { background-color: #f6f7f8; }
    
    /* Card Styles */
    .card { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 12px; 
        border: 1px solid #dcdcdc; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
        margin-bottom: 20px;
        color: #000000 !important;
    }
    
    /* Forced Text Color for all elements */
    h1, h2, h3, p, div, span, label {
        color: #000000 !important;
    }
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

# Main Interface
st.markdown(f"<h1>{menu_items.get(selected_menu, '🛡️')} {selected_menu}</h1>", unsafe_allow_html=True)

# Dashboard Logic
if selected_menu == "Operations Overview":
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="card"><h3>Total Incidents</h3><h1>25</h1><p>21 active detections</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="card"><h3>Active Dispatches</h3><h1>5</h1><p>1 pending response</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="card"><h3>Camera Status</h3><h1>3/6</h1><p>50% operational</p></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card"><h3>Incidents by Severity</h3>', unsafe_allow_html=True)
    chart_data = pd.DataFrame([2, 2, 11, 10], index=["High", "Critical", "Medium", "Low"])
    st.bar_chart(chart_data)
    st.markdown('</div>', unsafe_allow_html=True)

elif selected_menu == "Live Detection":
    st.markdown('<div class="card"><h3>Live AI Model</h3><p>Model: YOLOv8n (87.5% mAP50)</p></div>', unsafe_allow_html=True)
    st.warning("System Initializing...")

else:
    st.markdown(f'<div class="card"><h3>{selected_menu}</h3><p>Module under construction.</p></div>', unsafe_allow_html=True)
    
