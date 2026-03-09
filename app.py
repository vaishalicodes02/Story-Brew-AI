import streamlit as st
import time
import random

st.session_state["logged_in"] = True

# Configure page
st.set_page_config(
    page_title="Story Brew AI - Create Amazing Web Series Stories",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern dark theme
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

    /* Global styles */
    * {
        font-family: 'Poppins', sans-serif !important;
    }

    /* Main background with animated gradient */
    .main {
        background:
            linear-gradient(135deg, #0c0b1a 0%, #1a1a2e 20%, #2d1b69 40%, #11998e 60%, #38ef7d 80%, #667eea 100%),
            radial-gradient(circle at 25% 25%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 75% 75%, rgba(255, 119, 198, 0.2) 0%, transparent 50%),
            radial-gradient(circle at 50% 50%, rgba(120, 219, 226, 0.1) 0%, transparent 50%) !important;
        background-attachment: fixed !important;
    }

    /* Animated background particles */
    .main::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background:
            radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(120, 219, 226, 0.05) 0%, transparent 50%),
            url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.02'%3E%3Ccircle cx='30' cy='30' r='1.5'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E") repeat;
        background-size: 60px 60px;
        animation: colorShift 15s ease-in-out infinite alternate;
        pointer-events: none;
        z-index: -1;
    }

    .main::after {
        content: '';
        position: fixed;
        width: 100%;
        height: 100%;
        background:
            radial-gradient(ellipse 200px 100px at 20% 30%, rgba(108, 99, 255, 0.08), transparent),
            radial-gradient(ellipse 150px 200px at 80% 70%, rgba(255, 101, 132, 0.06), transparent),
            radial-gradient(ellipse 100px 150px at 60% 20%, rgba(152, 224, 202, 0.05), transparent),
            radial-gradient(ellipse 180px 120px at 30% 80%, rgba(255, 193, 7, 0.04), transparent),
            radial-gradient(circle at 10% 20%, rgba(108, 99, 255, 0.2) 0%, transparent 40%),
            radial-gradient(circle at 90% 80%, rgba(255, 101, 132, 0.2) 0%, transparent 40%),
            radial-gradient(circle at 50% 10%, rgba(152, 224, 202, 0.15) 0%, transparent 40%),
            radial-gradient(circle at 30% 70%, rgba(255, 193, 7, 0.1) 0%, transparent 40%),
            radial-gradient(circle at 70% 30%, rgba(156, 39, 176, 0.15) 0%, transparent 40%);
        animation: combinedFloat 35s ease-in-out infinite;
        pointer-events: none;
        z-index: -1;
    }

    @keyframes combinedFloat {
        0%, 100% {
            transform: translate(0, 0) rotate(0deg) scale(1);
            filter: blur(0px);
            opacity: 0.6;
        }
        20% {
            transform: translate(20px, -30px) rotate(5deg) scale(1.02);
            filter: blur(1px);
            opacity: 0.8;
        }
        40% {
            transform: translate(-15px, 25px) rotate(-3deg) scale(0.98);
            filter: blur(0.5px);
            opacity: 0.4;
        }
        60% {
            transform: translate(10px, -20px) rotate(2deg) scale(1.01);
            filter: blur(0.8px);
            opacity: 0.7;
        }
        80% {
            transform: translate(-25px, 15px) rotate(-4deg) scale(0.99);
            filter: blur(0.3px);
            opacity: 0.5;
        }
    }

    @keyframes colorShift {
        0% {
            filter: hue-rotate(0deg) brightness(1);
        }
        50% {
            filter: hue-rotate(15deg) brightness(1.1);
        }
        100% {
            filter: hue-rotate(30deg) brightness(0.9);
        }
    }

    @keyframes backgroundFloat {
        0%, 100% {
            transform: translateY(0px) rotate(0deg) scale(1);
            filter: blur(0px);
        }
        25% {
            transform: translateY(-15px) rotate(2deg) scale(1.02);
            filter: blur(1px);
        }
        50% {
            transform: translateY(-30px) rotate(-1deg) scale(0.98);
            filter: blur(0.5px);
        }
        75% {
            transform: translateY(-15px) rotate(1deg) scale(1.01);
            filter: blur(0.8px);
        }
    }

    /* Title styling */
    .title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 30%, #f093fb 60%, #f5576c 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        text-align: center !important;
        margin-bottom: 1rem !important;
        text-shadow: 0 0 30px rgba(102, 126, 234, 0.3) !important;
        letter-spacing: -2px !important;
        line-height: 1.1 !important;
    }

    .subtitle {
        font-size: 1.2rem !important;
        text-align: center !important;
        margin-bottom: 2rem !important;
        color: #e0e7ff !important;
        font-weight: 400 !important;
        letter-spacing: 0.5px !important;
        opacity: 0.9 !important;
    }

    /* Card styling */
    .card {
        background: rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(20px) !important;
        border-radius: 25px !important;
        padding: 2rem !important;
        margin: 1rem 0 !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), 0 0 60px rgba(102, 126, 234, 0.1) !important;
        transition: all 0.3s ease !important;
    }

    .card:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 15px 45px rgba(0, 0, 0, 0.4), 0 0 80px rgba(102, 126, 234, 0.15) !important;
    }

    /* Form styling */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > div,
    .stTextArea > div > div > textarea {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 2px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: white !important;
        padding: 15px 18px !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(10px) !important;
    }

    .stTextInput > div > div > input:focus,
    .stSelectbox > div > div > div:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea !important;
        background: rgba(255, 255, 255, 0.08) !important;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.3) !important;
    }

    .stTextInput > div > div > input::placeholder,
    .stTextArea > div > div > textarea::placeholder {
        color: rgba(255, 255, 255, 0.6) !important;
    }

    /* Label styling */
    .stTextInput label,
    .stSelectbox label,
    .stTextArea label,
    .stSlider label {
        color: #e0e7ff !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        margin-bottom: 8px !important;
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%) !important;
        background-size: 200% 200% !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 18px 30px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4) !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        position: relative !important;
        overflow: hidden !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.6) !important;
        background-position: 200% 0 !important;
    }

    .stButton > button:active {
        transform: translateY(0) !important;
    }

    /* Success message */
    .success {
        background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 50%, #56c596 100%) !important;
        color: white !important;
        padding: 20px 30px !important;
        border-radius: 15px !important;
        text-align: center !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        margin: 2rem 0 !important;
        box-shadow: 0 8px 25px rgba(86, 171, 47, 0.3) !important;
        letter-spacing: 0.5px !important;
    }

    /* Character cards */
    .character-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(102, 126, 234, 0.1) 100%) !important;
        padding: 25px !important;
        border-radius: 15px !important;
        text-align: center !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        margin: 10px 0 !important;
        transition: all 0.3s ease !important;
        position: relative !important;
        overflow: hidden !important;
    }

    .character-card::before {
        content: '' !important;
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 4px !important;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb) !important;
        transform: scaleX(0) !important;
        transition: transform 0.3s ease !important;
    }

    .character-card:hover::before {
        transform: scaleX(1) !important;
    }

    .character-card:hover {
        transform: translateY(-8px) !important;
        box-shadow: 0 12px 30px rgba(102, 126, 234, 0.3) !important;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.15) 0%, rgba(102, 126, 234, 0.2) 100%) !important;
    }

    /* Episode styling */
    .episode-item {
        background: rgba(255, 255, 255, 0.05) !important;
        padding: 20px !important;
        border-radius: 12px !important;
        border-left: 4px solid #667eea !important;
        margin: 10px 0 !important;
        transition: all 0.3s ease !important;
    }

    .episode-item:hover {
        background: rgba(255, 255, 255, 0.08) !important;
        transform: translateX(10px) !important;
        border-left-color: #f093fb !important;
    }

    /* Insights grid */
    .insight-item {
        background: rgba(255, 255, 255, 0.05) !important;
        padding: 20px !important;
        border-radius: 12px !important;
        text-align: center !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        margin: 8px 0 !important;
        transition: all 0.3s ease !important;
    }

    .insight-item:hover {
        transform: translateY(-5px) !important;
        background: rgba(255, 255, 255, 0.08) !important;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.2) !important;
    }

    /* Section headers */
    .section-header {
        font-size: 1.6rem !important;
        font-weight: 700 !important;
        margin-bottom: 25px !important;
        color: #fff !important;
        border-bottom: 2px solid rgba(102, 126, 234, 0.3) !important;
        padding-bottom: 10px !important;
    }

    /* Slider styling */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 50%, #f093fb 100%) !important;
    }

    .stSlider > div > div > div > div > div {
        background: white !important;
        box-shadow: 0 2px 8px rgba(102, 126, 234, 0.4) !important;
    }

    /* Spinner */
    .stSpinner > div > div {
        border-color: rgba(255, 255, 255, 0.1) !important;
        border-top-color: #667eea !important;
        border-right-color: #764ba2 !important;
    }

    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}

    /* Responsive design */
    @media (max-width: 768px) {
        .title {
            font-size: 2.5rem !important;
        }
        .subtitle {
            font-size: 1rem !important;
        }
        .card {
            padding: 1.5rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Custom title
st.markdown('<h1 class="title">🎬 Story Brew AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">✨ Generate captivating YouTube Web Series Stories with AI magic ✨</p>', unsafe_allow_html=True)

# Create columns for better layout
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📝 Story Details")
    title = st.text_input("🎯 Series Title", placeholder="Enter your series title...", key="title")

    genre_options = ["🎭 Comedy", "🎭 Drama", "🚀 Sci-Fi", "🔪 Thriller", "🧙 Fantasy", "💕 Romance", "🔍 Mystery"]
    genre = st.selectbox("🎭 Select Genre", genre_options, key="genre")

    premise = st.text_area("💡 Story Premise", placeholder="Describe your story idea, main conflict, and key themes...", height=120, key="premise")

with col2:
    st.markdown("### ⚙️ Configuration")
    episodes = st.slider("📺 Number of Episodes", 1, 20, 5, key="episodes")

    tone_options = ["Light-hearted", "Dark", "Inspirational", "Humorous", "Suspenseful", "Dramatic"]
    tone = st.selectbox("🎨 Story Tone", tone_options, key="tone")

    audience_options = ["👦 Teens (13-19)", "👨‍💼 Young Adults (20-35)", "🧑 Adults (35+)", "👨‍👩‍👧‍👦 Family Friendly", "🧒 Kids (8-12)"]
    target_audience = st.selectbox("👥 Target Audience", audience_options, key="audience")

    platform_options = ["📺 YouTube Series", "🎬 Netflix Style", "📱 TikTok Series", "📸 Instagram Reels"]
    platform = st.selectbox("📱 Platform Style", platform_options, key="platform")

# Generate button
if st.button("🚀 Generate Story", key="generate"):

    # Save inputs for Script Generator page
    st.session_state["video_title"] = title
    st.session_state["genre"] = genre
    st.session_state["story"] = premise
    st.session_state["duration"] = episodes
    st.session_state["audience"] = target_audience
    # Character data
    characters = [
        {"icon": "🦸", "name": "The Protagonist", "desc": "A passionate creator with big dreams and endless determination."},
        {"icon": "👫", "name": "The Best Friend", "desc": "Loyal companion who provides comic relief and moral support."},
        {"icon": "😈", "name": "The Antagonist", "desc": "Formidable rival who challenges the protagonist's journey."},
        {"icon": "🧙", "name": "The Mentor", "desc": "Wise guide who offers crucial advice and perspective."}
    ]

    char_cols = st.columns(len(characters))
    for i, char in enumerate(characters):
        with char_cols[i]:
            st.markdown(f"""
            <div class="character-card">
                <div style="font-size: 3rem; margin-bottom: 15px;">{char['icon']}</div>
                <h3>{char['name']}</h3>
                <p>{char['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Episode outline
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📋 Episode Outline")

    episode_templates = [
        "🌟 The journey begins with unexpected challenges and new alliances.",
        "🎬 Characters face their first major conflict and grow stronger.",
        "⚡ Plot twists reveal hidden secrets and change everything.",
        "💫 Romantic subplots develop while main conflicts intensify.",
        "🔥 The stakes rise as antagonists make their move.",
        "🌈 Moments of triumph are followed by devastating setbacks.",
        "🎭 Character backstories are revealed through flashbacks.",
        "🚀 The story reaches its climax with epic confrontations.",
        "✨ Resolutions bring closure while setting up future adventures.",
        "🏆 The series concludes with emotional depth and hope.",
        "🎪 New characters join as the world expands.",
        "🕵️ Mysteries deepen with surprising revelations.",
        "❤️ Relationships evolve through trials and tribulations.",
        "⚔️ Battles test the limits of courage and friendship.",
        "🎨 Creative solutions overcome impossible obstacles.",
        "🌟 Dreams become reality through perseverance.",
        "🔮 Prophecies and visions guide the characters' path.",
        "🎭 Disguises and deception create thrilling moments.",
        "💎 Precious discoveries change everything.",
        "🎊 Celebrations mask underlying tensions."
    ]

    for i in range(1, episodes + 1):
        template = episode_templates[(i - 1) % len(episode_templates)]
        st.markdown(f"""
        <div class="episode-item">
            <div style="font-weight: 700; color: #667eea; font-size: 1.1rem; margin-bottom: 8px;">Episode {i}</div>
            <div style="color: rgba(255, 255, 255, 0.9); line-height: 1.6;">{template}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Pilot episode
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🎬 Pilot Episode Summary")
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(240, 147, 251, 0.1) 100%); padding: 25px; border-radius: 15px; border: 1px solid rgba(102, 126, 234, 0.2);">
        <p style="color: rgba(255, 255, 255, 0.9); line-height: 1.7; margin-bottom: 15px;">🌅 The story begins in a bustling creative hub where our protagonist discovers their passion for storytelling. With limited resources but unlimited ambition, they embark on an extraordinary journey filled with unexpected alliances, thrilling challenges, and life-changing discoveries.</p>
        <p style="color: rgba(255, 255, 255, 0.9); line-height: 1.7; margin-bottom: 0;">🎯 The first episode establishes the core conflict, introduces key characters, and sets up the overarching narrative that will captivate audiences throughout the series.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Story insights
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🎨 Story Insights")

    insights = [
        {"icon": "📊", "label": "Genre Fit", "value": "Excellent"},
        {"icon": "🎯", "label": "Audience Appeal", "value": "High"},
        {"icon": "⏱️", "label": "Episode Length", "value": "8-12 min"},
        {"icon": "📈", "label": "Viral Potential", "value": "Very High"},
        {"icon": "💰", "label": "Monetization", "value": "Strong"},
        {"icon": "🔥", "label": "Engagement", "value": "Excellent"}
    ]

    insight_cols = st.columns(3)
    for i, insight in enumerate(insights):
        with insight_cols[i % 3]:
            st.markdown(f"""
            <div class="insight-item">
                <div style="font-size: 2rem; margin-bottom: 10px;">{insight['icon']}</div>
                <h4>{insight['label']}</h4>
                <span style="font-size: 1.2rem; font-weight: 700; color: #667eea;">{insight['value']}</span>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Analytics section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📊 Story Analytics")

    analytics = [
        {"label": "Estimated Views", "value": "2.5M+", "color": "#ff6b6b"},
        {"label": "Series Rating", "value": "4.8/5", "color": "#ffd93d"},
        {"label": "Completion Rate", "value": "87%", "color": "#6bcf7f"}
    ]

    analytic_cols = st.columns(3)
    for i, analytic in enumerate(analytics):
        with analytic_cols[i]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, rgba(255, 107, 107, 0.1) 0%, rgba(152, 224, 202, 0.1) 100%); padding: 20px; border-radius: 12px; text-align: center; border: 1px solid rgba(255, 107, 107, 0.2);">
                <span style="display: block; font-size: 0.9rem; color: rgba(255, 255, 255, 0.8); margin-bottom: 8px;">{analytic['label']}</span>
                <span style="font-size: 1.5rem; font-weight: 700; color: {analytic['color']};">{analytic['value']}</span>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)