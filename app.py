import streamlit as st

st.set_page_config(page_title="Story Brew AI")

st.title("🎬 Story Brew AI")
st.subheader("Generate YouTube Web Series Stories")

title = st.text_input("Series Title")

genre = st.selectbox(
    "Select Genre",
    ["Comedy", "Drama", "Sci-Fi", "Thriller", "Fantasy"]
)

premise = st.text_area("Enter your story idea")

episodes = st.slider("Number of Episodes", 1, 10)

if st.button("Generate Story"):

    st.success("Story Generated!")

    st.header("Characters")

    st.write("Hero: A passionate creator trying to build a web series.")
    st.write("Friend: Supports the hero with crazy ideas.")
    st.write("Rival Creator: Competes for views.")

    st.header("Episode Outline")

    for i in range(1, episodes + 1):
        st.write(f"Episode {i}: The journey continues with unexpected challenges.")

    st.header("Pilot Episode")

    st.write(
        "The story begins in a small studio where the creator decides to build a YouTube series..."
    )