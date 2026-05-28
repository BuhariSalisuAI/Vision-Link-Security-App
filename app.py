import streamlit as st
import pandas as pd

# Page Setup
st.set_page_config(page_title="VISION-LINK OS", layout="wide")

# CSS - Mun gyara shi don rubutu ya zama baƙi koyaushe
st.markdown("""
    <style>
    /* Canza launin rubutu zuwa baki domin ya fito a kan kowane background */
    .stApp { 
        background-color: #f5f6f8; 
        color: #000000; 
    }
    div[data-testid="stSidebar"] { 
        background-color: #ffffff; 
        border-right: 1px solid #e0e0e0; 
    }
    /* Tabbatar da header ma baki ne */
    h1, h2, h3, p, div {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("<h1 style='color: black;'>🛡️ SECURITY OPS</h1>", unsafe_allow_html=True)
    menu = st.radio("Navigation", [
        "Operations Overview", "Camera Feeds", "Location Risk", 
        "Incident Log", "Dispatch Center", "Live Detection"
    ])
    st.markdown("---")
    st.write("Status: System Active 🟢")

# Main Interface
st.header(f"Dashboard: {menu}")

if menu == "Operations Overview":
    st.write("Welcome to the Command Center.")
    col1, col2 = st.columns(2)
    col1.metric("Active Threats", "0")
    col2.metric("Camera Status", "Online")
elif menu == "Live Detection":
    st.warning("Live AI Model: System Initializing...")
else:
    st.write("Module under construction.")
