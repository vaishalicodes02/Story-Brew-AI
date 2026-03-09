import streamlit as st

st.set_page_config(page_title="Story Brew AI")

# Custom title
st.markdown('<h1 class="title">🎬 Story Brew AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">✨ Generate captivating YouTube Web Series Stories with AI magic ✨</p>', unsafe_allow_html=True)

# Create two columns for better layout
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📝 Story Details")
    title = st.text_input("Series Title", placeholder="Enter your series title...")
    
    genre = st.selectbox(
        "🎭 Select Genre",
        ["🎭 Comedy", "🎭 Drama", "🚀 Sci-Fi", "🔪 Thriller", "🧙 Fantasy"]
    )
    
    premise = st.text_area("💡 Enter your story idea", placeholder="Describe your story premise...", height=100)

with col2:
    st.markdown("### ⚙️ Configuration")
    episodes = st.slider("📺 Number of Episodes", 1, 10, 5)
    
    st.markdown("### 🎯 Story Elements")
    tone = st.selectbox("🎨 Tone", ["Light-hearted", "Dark", "Inspirational", "Humorous", "Suspenseful"])
    target_audience = st.selectbox("👥 Target Audience", ["Teens", "Young Adults", "Adults", "Family"])

# Generate button
if st.button("🚀 Generate Story"):
    with st.spinner("Brewing your story... ☕"):
        import time
        time.sleep(2)  # Simulate processing
    
    st.success("🎉 Story Generated Successfully!")
    
    # Characters section
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("👥 Characters")
    char_col1, char_col2, char_col3 = st.columns(3)
    
    with char_col1:
        st.markdown("**🦸 Hero**")
        st.write("A passionate creator trying to build a web series.")
    
    with char_col2:
        st.markdown("**👫 Friend**")
        st.write("Supports the hero with crazy ideas.")
    
    with char_col3:
        st.markdown("**😈 Rival Creator**")
        st.write("Competes for views and attention.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Episode outline
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📋 Episode Outline")
    
    for i in range(1, episodes + 1):
        if i % 2 == 0:
            st.markdown(f"**Episode {i}:** 🌟 The journey continues with unexpected challenges and plot twists.")
        else:
            st.markdown(f"**Episode {i}:** 🎬 New adventures unfold as characters face their destinies.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Pilot episode
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🎬 Pilot Episode")
    st.write(
        "🌅 The story begins in a small studio where the creator decides to build a YouTube series. "
        "With determination and creativity, they embark on an exciting journey filled with challenges, "
        "friendships, and unexpected discoveries. The first episode sets the stage for an epic adventure "
        "that will captivate audiences worldwide! ✨"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Additional features
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("🎨 Story Insights")
    insight_col1, insight_col2 = st.columns(2)
    
    with insight_col1:
        st.markdown("**📊 Genre Fit:** High")
        st.markdown("**🎯 Audience Appeal:** Excellent")
    
    with insight_col2:
        st.markdown("**⏱️ Episode Length:** 8-12 minutes")
        st.markdown("**📈 Viral Potential:** High")
    st.markdown('</div>', unsafe_allow_html=True)