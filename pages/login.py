import streamlit as st

# Configure page
st.set_page_config(
    page_title="Story Brew AI - Login",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful and responsive login page
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500;600;700&display=swap');

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0c0b1a 0%, #1a1a2e 25%, #2d1b69 50%, #11998e 75%, #667eea 100%);
        background-attachment: fixed;
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stAppViewContainer"]::before {
        content: '';
        position: fixed;
        inset: 0;
        background:
            radial-gradient(ellipse 60% 50% at 10% 10%, rgba(0, 212, 170, 0.1) 0%, transparent 60%),
            radial-gradient(ellipse 50% 60% at 90% 90%, rgba(102, 126, 234, 0.1) 0%, transparent 60%),
            radial-gradient(ellipse 40% 40% at 50% 50%, rgba(168, 85, 247, 0.08) 0%, transparent 70%);
        pointer-events: none;
        z-index: 0;
    }

    .main {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
        background: transparent !important;
    }

    .block-container {
        max-width: 500px;
        width: 100%;
        padding: 0 !important;
        background: transparent;
    }

    .stContainer {
        background: transparent;
        padding: 0;
    }

    /* Login Card */
    .login-wrapper {
        background: rgba(13, 28, 48, 0.7);
        backdrop-filter: blur(30px);
        border: 1px solid rgba(0, 212, 170, 0.2);
        border-radius: 24px;
        padding: 60px 45px;
        box-shadow:
            0 20px 60px rgba(0, 0, 0, 0.3),
            inset 0 1px 1px rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
        animation: slideIn 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    .login-wrapper::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(0, 212, 170, 0.5), transparent);
        z-index: 1;
    }

    .login-wrapper::after {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at 30% 30%, rgba(0, 212, 170, 0.1), transparent 50%);
        animation: gradientShift 8s ease-in-out infinite;
        z-index: 0;
    }

    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes gradientShift {
        0%, 100% { transform: translate(0, 0); }
        50% { transform: translate(20px, 20px); }
    }

    /* Header */
    .login-header {
        position: relative;
        z-index: 2;
        text-align: center;
        margin-bottom: 50px;
    }

    .login-icon {
        font-size: 3.5rem;
        margin-bottom: 15px;
        animation: bounce 2s ease-in-out infinite;
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    .login-title {
        font-family: 'Syne', sans-serif;
        font-size: 2.2rem;
        font-weight: 800;
        color: #f0f4f8;
        margin-bottom: 10px;
        letter-spacing: -0.5px;
    }

    .login-subtitle {
        font-size: 0.95rem;
        color: rgba(255, 255, 255, 0.6);
        font-weight: 400;
        letter-spacing: 0.5px;
    }

    /* Form Styles */
    .form-content {
        position: relative;
        z-index: 2;
    }

    .input-group {
        margin-bottom: 24px;
        position: relative;
    }

    .input-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        color: rgba(0, 212, 170, 0.8);
        font-weight: 600;
        letter-spacing: 0.1em;
        margin-bottom: 8px;
        display: block;
    }

    .stTextInput > div > div > input,
    .stTextInput > div > div > input[type="password"] {
        width: 100% !important;
        background: rgba(19, 27, 40, 0.6) !important;
        border: 1.5px solid rgba(0, 212, 170, 0.2) !important;
        border-radius: 12px !important;
        padding: 14px 18px !important;
        color: #f0f4f8 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
        outline: none !important;
    }

    .stTextInput > div > div > input::placeholder,
    .stTextInput > div > div > input[type="password"]::placeholder {
        color: rgba(255, 255, 255, 0.4) !important;
    }

    .stTextInput > div > div > input:focus,
    .stTextInput > div > div > input[type="password"]:focus {
        border-color: rgba(0, 212, 170, 0.6) !important;
        background: rgba(25, 35, 55, 0.8) !important;
        box-shadow: 0 0 0 4px rgba(0, 212, 170, 0.15) !important;
        transform: translateY(-2px) !important;
    }

    /* Button Styles */
    .stButton {
        width: 100%;
        margin-top: 32px !important;
    }

    .stButton > button {
        width: 100% !important;
        background: linear-gradient(135deg, #00d4aa 0%, #4f9cf9 100%) !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 16px 24px !important;
        color: white !important;
        font-family: 'Syne', sans-serif !important;
        font-size: 0.95rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.12em !important;
        text-transform: uppercase !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 24px rgba(0, 212, 170, 0.3) !important;
        position: relative !important;
        overflow: hidden !important;
    }

    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        transition: left 0.6s ease !important;
        z-index: 1;
    }

    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 12px 32px rgba(0, 212, 170, 0.5) !important;
    }

    .stButton > button:hover::before {
        left: 100% !important;
    }

    .stButton > button:active {
        transform: translateY(-1px) !important;
    }

    /* Alert Styling */
    .stAlert {
        border-radius: 12px !important;
        border: 1px solid !important;
        padding: 16px 20px !important;
        animation: slideDown 0.4s ease-out;
        margin-top: 24px !important;
    }

    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .stSuccess {
        background: rgba(34, 197, 94, 0.1) !important;
        border-color: rgba(34, 197, 94, 0.3) !important;
        color: #22c55e !important;
    }

    .stError {
        background: rgba(244, 63, 94, 0.1) !important;
        border-color: rgba(244, 63, 94, 0.3) !important;
        color: #f43f5e !important;
    }

    /* Divider */
    .divider {
        position: relative;
        z-index: 2;
        margin: 32px 0;
        text-align: center;
        color: rgba(255, 255, 255, 0.3);
        font-size: 0.85rem;
    }

    .divider::before,
    .divider::after {
        content: '';
        position: absolute;
        top: 50%;
        width: 45%;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1));
    }

    .divider::before {
        left: 0;
    }

    .divider::after {
        right: 0;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .login-wrapper {
            padding: 50px 30px;
            border-radius: 20px;
        }

        .login-title {
            font-size: 1.8rem;
        }

        .login-icon {
            font-size: 2.8rem;
            margin-bottom: 12px;
        }

        .login-subtitle {
            font-size: 0.9rem;
        }

        .stTextInput > div > div > input,
        .stTextInput > div > div > input[type="password"] {
            padding: 12px 16px !important;
            font-size: 0.9rem !important;
        }

        .stButton > button {
            padding: 14px 20px !important;
            font-size: 0.9rem !important;
        }
    }

    @media (max-width: 480px) {
        .login-wrapper {
            padding: 40px 20px;
            border-radius: 16px;
        }

        .main {
            padding: 15px;
        }

        .login-title {
            font-size: 1.6rem;
            margin-bottom: 8px;
        }

        .login-icon {
            font-size: 2.4rem;
            margin-bottom: 10px;
        }

        .login-subtitle {
            font-size: 0.85rem;
        }

        .input-group {
            margin-bottom: 20px;
        }

        .stTextInput > div > div > input,
        .stTextInput > div > div > input[type="password"] {
            padding: 12px 14px !important;
            font-size: 0.88rem !important;
        }

        .stButton > button {
            padding: 12px 16px !important;
            font-size: 0.85rem !important;
        }

        .input-label {
            font-size: 0.75rem;
            margin-bottom: 6px;
        }
    }

    /* Hide Streamlit elements */
    [data-testid="stToolbar"],
    [data-testid="stSidebarNav"],
    .viewerBadge_container__r5tak,
    footer {
        display: none !important;
    }

    .css-1rs6os, .css-1lsmgbg, .css-18e3th9, .css-1d391kg {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Login Container
st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="login-header">
    <div class="login-icon">🔐</div>
    <h1 class="login-title">Story-Brew-AI</h1>
    <p class="login-subtitle">Sign in to create amazing web series stories</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="form-content">', unsafe_allow_html=True)

# Username input
st.markdown('<label class="input-label">👤 Username</label>', unsafe_allow_html=True)
username = st.text_input("", placeholder="Enter your username", label_visibility="collapsed", key="username")

# Password input
st.markdown('<label class="input-label">🔒 Password</label>', unsafe_allow_html=True)
password = st.text_input("", type="password", placeholder="Enter your password", label_visibility="collapsed", key="password")

# Remember me checkbox
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("")
with col2:
    st.markdown("")

# Login button
if st.button("🚀 Login", use_container_width=True, key="login_btn"):
    if username == "creator" and password == "1234":
        st.session_state["logged_in"] = True
        st.success("✨ Login successful! Welcome back, Creator!")
        st.balloons()
        st.rerun()
    else:
        st.error("❌ Invalid username or password. Please try again.")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer info
st.markdown("""
<div class="divider">Demo Credentials</div>
<style>
    .footer-info {
        position: relative;
        z-index: 2;
        text-align: center;
        margin-top: 30px;
        font-size: 0.8rem;
        color: rgba(255, 255, 255, 0.5);
    }
</style>
<div class="footer-info">
    <strong>Username:</strong> creator | <strong>Password:</strong> 1234
</div>
""", unsafe_allow_html=True)