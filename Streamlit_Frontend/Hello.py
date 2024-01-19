import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Fruit Recommendation System! 👋")

st.sidebar.success("Select a recommendation app.")

st.markdown(
    """
    A fruit recommendation web application using content-based approach to generate fruit and vegetables based on user preference, detary goals and health restriction.
    """
)
