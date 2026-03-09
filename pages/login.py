import streamlit as st

# Custom CSS for beautiful and responsive login page
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    * {
        box-sizing: border-box;
    }

    body {
        margin: 0;
        padding: 0;
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        background-attachment: fixed;
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        min-height: 100vh;
        padding: 20px;
    }

    .login-card {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(20px);
        padding: 50px 40px;
        border-radius: 25px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        width: 100%;
        max-width: 450px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.3);
        animation: slideIn 0.8s ease-out;
        position: relative;
        overflow: hidden;
    }

    .login-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
    }

    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .login-title {
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 35px;
        color: #333;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        position: relative;
    }

    .login-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        border-radius: 2px;
    }

    .input-group {
        position: relative;
        margin-bottom: 25px;
    }

    .input-icon {
        position: absolute;
        left: 15px;
        top: 50%;
        transform: translateY(-50%);
        color: #666;
        font-size: 18px;
        z-index: 1;
    }

    .stTextInput > div > div > input {
        border-radius: 12px;
        border: 2px solid #e1e5e9;
        padding: 18px 18px 18px 50px;
        font-size: 16px;
        width: 100%;
        transition: all 0.3s ease;
        background: rgba(255, 255, 255, 0.9);
        font-family: 'Poppins', sans-serif;
    }

    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        transform: translateY(-2px);
    }

    .stTextInput > div > div > input::placeholder {
        color: #999;
        font-weight: 400;
    }

    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 18px 30px;
        font-size: 18px;
        font-weight: 600;
        cursor: pointer;
        width: 100%;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
        font-family: 'Poppins', sans-serif;
    }

    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s ease;
    }

    .stButton > button:hover::before {
        left: 100%;
    }

    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 30px rgba(102, 126, 234, 0.4);
    }

    .stSuccess, .stError {
        border-radius: 12px;
        padding: 15px;
        margin-top: 25px;
        font-weight: 500;
        animation: fadeIn 0.5s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    .stSuccess {
        background: linear-gradient(135deg, #56ab2f, #a8e6cf);
        color: white;
        border: 1px solid #56ab2f;
    }

    .stError {
        background: linear-gradient(135deg, #ff6b6b, #ffa726);
        color: white;
        border: 1px solid #ff6b6b;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .login-card {
            padding: 40px 30px;
            margin: 20px;
            max-width: 100%;
        }
        .login-title {
            font-size: 2.4rem;
        }
    }

    @media (max-width: 480px) {
        .login-card {
            padding: 30px 20px;
        }
        .login-title {
            font-size: 2rem;
        }
        .stTextInput > div > div > input {
            padding: 15px 15px 15px 45px;
            font-size: 14px;
        }
        .input-icon {
            font-size: 16px;
            left: 12px;
        }
        .stButton > button {
            padding: 15px 20px;
            font-size: 16px;
        }
    }

    /* Hide Streamlit elements */
    .css-1rs6os, .css-1lsmgbg, .css-18e3th9, .css-1d391kg {
        display: none !important;
    }

    .main .block-container {
        padding: 0;
        max-width: none;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="login-container">', unsafe_allow_html=True)
st.markdown('<div class="login-card">', unsafe_allow_html=True)

st.markdown('<h1 class="login-title">🔐 Login</h1>', unsafe_allow_html=True)

# Username input with icon
st.markdown('<div class="input-group">', unsafe_allow_html=True)
st.markdown('<span class="input-icon">👤</span>', unsafe_allow_html=True)
username = st.text_input("", placeholder="Enter your username", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# Password input with icon
st.markdown('<div class="input-group">', unsafe_allow_html=True)
st.markdown('<span class="input-icon">🔒</span>', unsafe_allow_html=True)
password = st.text_input("", type="password", placeholder="Enter your password", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

if st.button("Login"):
    if username == "creator" and password == "1234":
        st.session_state["logged_in"] = True
        st.success("🎉 Login successful! Welcome back!")
        st.rerun()
    else:
        st.error("❌ Invalid username or password. Please try again.")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)