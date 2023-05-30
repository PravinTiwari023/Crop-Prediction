import streamlit as st

def sidebardesign():
    st.markdown(
        """
        <style>

        div[data-testid="stSidebarNav"] li div a {
            margin-left: 0.8rem;
            padding: 0.5rem;
            width: 300px;
            border-radius: 0.5rem;
        }
        div[data-testid="stSidebarNav"] li div::focus-visible {
            background-color: rgba(151, 166, 195, 0.15);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
hide_st_style="""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)