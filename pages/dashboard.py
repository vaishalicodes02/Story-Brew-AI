import streamlit as st

st.title("🎬 Creator Dashboard")

# Check if user logged in
if "logged_in" not in st.session_state:
    st.warning("⚠ Please login first.")
    st.stop()

st.success("Welcome to Story Brew AI 🚀")

st.write("Create cinematic YouTube scripts using AI.")

st.markdown("---")

# Dashboard cards
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📝 Create New Script")
    st.write("Start writing your YouTube story idea.")

with col2:
    st.info("🎥 Video Scripts")
    st.write("Manage generated screenplay scripts.")

with col3:
    st.info("⬇ Download Scripts")
    st.write("Download scripts as PDF or TXT.")