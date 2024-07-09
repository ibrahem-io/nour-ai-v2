import streamlit as st
from utils.studio_style import apply_studio_style


if __name__ == '__main__':
    st.set_page_config(
        page_title="Nour AI"
    )
    apply_studio_style()
    st.title("Nour AI: Social Media Manager")
    st.markdown("Nour for social media management offers range of tools to assist you with your brand content craetion on social media" )