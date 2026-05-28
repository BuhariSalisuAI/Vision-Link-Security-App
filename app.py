import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# CSS don layout na Monday.com
st.markdown("""
    <style>
    .card { background: white; padding: 20px; border-radius: 12px; border: 1px solid #e0e0e0; margin-bottom: 15px; }
    .metric-box { font-size: 20px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Security Operations")

# Raba shafin gida biyu (kamar hoto)
col_left, col_right = st.columns([1, 2])

with col_left:
    st.markdown('<div class="card"><h3>Developer</h3><p>Buhari Salisu - AI Systems Engineer</p><p>Status: Production Ready 🟢</p></div>', unsafe_allow_html=True)
    st.info("Deployment Steps for Hugging Face are active.")

with col_right:
    # Metrics
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="card">Total Incidents<br><b>25</b></div>', unsafe_allow_html=True)
    c2.markdown('<div class="card">Active Dispatches<br><b>5</b></div>', unsafe_allow_html=True)
    c3.markdown('<div class="card">Camera Status<br><b>3/6</b></div>', unsafe_allow_html=True)
    
    # Charts (Misali)
    st.markdown('<div class="card"><h3>Incidents by Severity</h3>', unsafe_allow_html=True)
    chart_data = pd.DataFrame([2, 2, 11, 10], index=["High", "Critical", "Medium", "Low"])
    st.bar_chart(chart_data)
    st.markdown('</div>', unsafe_allow_html=True)

    # Recent Activity
    st.markdown('<div class="card"><h3>Recent Activity</h3><p>⚠️ person detected at North Gate</p><p>⚠️ bottle detected at North Gate</p></div>', unsafe_allow_html=True)
    
