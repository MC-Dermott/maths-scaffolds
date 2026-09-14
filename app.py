import pathlib

import streamlit as st
import streamlit.components.v1 as components

HTML_PATH = pathlib.Path(__file__).parent / "maths_scaffolds.html"

st.set_page_config(page_title="Maths Scaffolds", layout="wide")

st.markdown(
    """
    <style>
        .block-container {padding: 0 !important; max-width: 100% !important;}
        header[data-testid="stHeader"] {background: transparent;}
        iframe {border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = HTML_PATH.read_text(encoding="utf-8")
components.html(html, height=1600, scrolling=True)
