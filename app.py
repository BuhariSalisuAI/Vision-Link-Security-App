import streamlit as st

st.set_page_config(page_title="VISION-LINK OS", layout="wide")

# CSS don layout irin na Monday.com (Cards & Shadows)
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; }
    .css-card { 
        background-color: white; 
        padding: 20px; 
        border-radius: 10px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
        margin-bottom: 20px;
    }
    .metric-value { font-size: 24px; font-weight: bold; color: #007bff; }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🛡️ VISION-LINK")
    menu = st.radio("Navigation", [
        "Operations Overview", "Camera Feeds", "Live Detection"
    ])

# Main Interface
st.header(f"Dashboard: {menu}")

if menu == "Operations Overview":
    # Nan ne muke kirkirar "Cards" irin na Monday.com
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="css-card"><h3>Active Threats</h3><p class="metric-value">0</p></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="css-card"><h3>Camera Status</h3><p class="metric-value" style="color: green;">Online</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="css-card"><h3>Welcome</h3><p>Command Center yana aiki lafiya.</p></div>', unsafe_allow_html=True)
