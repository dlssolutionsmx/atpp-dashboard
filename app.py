import base64
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


def render_header() -> None:
    """Muestra una cabecera compacta sin deformar ni apilar el logotipo."""
    logo_data = base64.b64encode(LOGO_FILE.read_bytes()).decode("ascii")
    st.markdown(
        f"""
        <style>
        .atpp-header {{
            align-items: center;
            display: flex;
            gap: 1rem;
            padding: .35rem 0 1rem;
        }}
        .atpp-header img {{
            flex: 0 0 auto;
            height: auto;
            max-width: 110px;
            width: 18vw;
        }}
        .atpp-header h1 {{
            font-size: clamp(1.65rem, 4vw, 2.65rem);
            line-height: 1.05;
            margin: 0;
        }}
        .atpp-header p {{
            margin: .35rem 0 0;
            opacity: .72;
        }}
        @media (max-width: 640px) {{
            .atpp-header {{ gap: .75rem; }}
            .atpp-header img {{ max-width: 82px; }}
            .atpp-header h1 {{ font-size: 1.55rem; }}
        }}
        </style>
        <header class="atpp-header">
            <img src="data:image/png;base64,{logo_data}" alt="ATpp">
            <div>
                <h1>Microlearning by ATpp</h1>
                <p>Del currículo a la actividad didáctica</p>
            </div>
        </header>
        """,
        unsafe_allow_html=True,
    )


render_header()

components.html(load_dashboard(), height=1800, scrolling=True)
