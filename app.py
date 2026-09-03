from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


BASE_DIR = Path(__file__).resolve().parent
DASHBOARD_FILE = BASE_DIR / "index.html"
LOGO_FILE = BASE_DIR / "assets" / "ATpp_sticker.png"


st.set_page_config(
    page_title="ATPP — Selector curricular relacional",
    page_icon="📚",
    layout="wide",
)


def load_dashboard() -> str:
    """Carga sin transformar la versión HTML validada del selector."""
    if not DASHBOARD_FILE.is_file():
        st.error("No se encontró index.html junto a app.py.")
        st.stop()
    return DASHBOARD_FILE.read_text(encoding="utf-8")


logo_column, headline_column = st.columns([1, 4], vertical_alignment="center")
with logo_column:
    st.image(LOGO_FILE, width="stretch")
with headline_column:
    st.markdown("# Del currículo a la actividad didáctica")
    st.caption("ATPP · Selector curricular relacional")

components.html(load_dashboard(), height=1800, scrolling=True)
