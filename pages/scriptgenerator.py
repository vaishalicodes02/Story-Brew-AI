import streamlit as st
import google.generativeai as genai

st.title("🎬 AI Screenplay Generator")

# Check login
if "logged_in" not in st.session_state:
    st.warning("Please login first")
    st.stop()

# Get data from story input page
video_title = st.session_state.get("video_title", "")
genre = st.session_state.get("genre", "")
story = st.session_state.get("story", "")
duration = st.session_state.get("duration", "")
audience = st.session_state.get("audience", "")

st.write("Click below to generate your cinematic narration script.")

if st.button("Generate Script"):
    # Check for API key
    if "GEMINI_API_KEY" not in st.secrets:
        st.error("GEMINI_API_KEY not found in secrets. Please configure it in Streamlit secrets.")
        st.stop()

    # Configure gemini
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-pro")

    # 👇 THIS WAS MISSING
    prompt = f"""
Create a cinematic storytelling script.

Title: {video_title}
Genre: {genre}
Story Idea: {story}
Duration: {duration}
Audience: {audience}

Write an engaging YouTube storytelling narration.
"""

    try:
        response = model.generate_content(prompt)
        script = response.text
        st.session_state["generated_script"] = script
        st.text_area("Generated Script", script, height=400)
    except Exception as e:
        st.error(f"Error generating script: {e}")