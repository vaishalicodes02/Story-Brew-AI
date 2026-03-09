import streamlit as st

st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    
    if username == "creator" and password == "1234":
        st.session_state["logged_in"] = True
        st.success("Login successful!")
    else:
        st.error("Invalid username or password")