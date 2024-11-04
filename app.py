import streamlit as st
import importlib
from typing import Callable

# Configure page settings
st.set_page_config(
    page_title="Virtual Chemistry Lab",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Chemistry experiments data
experiments = {
    "Baking Soda and Vinegar Reaction": {
        "module": "baking",
        "run_experiment": lambda: importlib.import_module("baking").run_experiment()
    },
    "Sodium and Water Reaction": {
        "module": "explosion",
        "run_experiment": lambda: importlib.import_module("explosion").run_experiment()
    },
    "pH Indicator": {
        "module": "indicator",
        "run_experiment": lambda: importlib.import_module("indicator").run_experiment()
    },
    "Acid-Base Titration": {
        "module": "acid_base",
        "run_experiment": lambda: importlib.import_module("acid_base").run_experiment()
    },
    "Elephant Toothpaste Reaction": {
        "module": "elephant_toothpaste",
        "run_experiment": lambda: importlib.import_module("elephant_toothpaste").run_experiment()
    }
}

# Custom CSS for the flip card styling and title animations
def load_css():
    css = """
    /* All the previous CSS code remains unchanged */
    
    /* Custom sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f0f0f0 0%, #e0e0e0 100%);
    }

    .sidebar .element-container {
        background: transparent;
    }

    .sidebar .stButton > button {
        font-family: 'Roboto', sans-serif;
        font-weight: 500;
        color: #1a1a1a;
        background: white;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        transition: all 0.3s ease;
    }

    .sidebar .stButton > button:hover {
        background: #f8f8f8;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def render_card(title, content):
    st.markdown(f"""
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <h2>{title}</h2>
                    <div style='font-size: 3em; margin: 20px 0'>🧪</div>
                </div>
                <div class="flip-card-back">
                    <h3>Description</h3>
                    <p>{content['description']}</p>
                    <h3>Visualization</h3>
                    <p>{content['visualization']}</p>
                    <h3>Fun Fact</h3>
                    <p>{content['fun_fact']}</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def main():
    load_css()
    
    # Sidebar navigation
    with st.sidebar:
        st.title("🧪 Experiments")
        selected_tab = st.selectbox("Select Experiment", list(experiments.keys()), index=0)

    # Title container with animations and icons
    st.markdown("""
        <div class='title-container'>
            <div class='floating-formula formula1'>H₂O 💧</div>
            <div class='floating-formula formula2'>CO₂ ⚡</div>
            <div class='floating-formula formula3'>O₂ 🔥</div>
            <div class='floating-formula formula4'>NaCl ✨</div>
            <div class='floating-formula formula5'>CH₄ 💨</div>
            <h1 class='glowing-title'>{selected_tab}</h1>
            <div class='icons-container'>
                <span class='chemistry-icon'>⚗️</span>
                <span class='chemistry-icon'>🧪</span>
                <span class='chemistry-icon'>🔬</span>
                <span class='chemistry-icon'>🧫</span>
                <span class='chemistry-icon'>⚛️</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Load and display the selected experiment's content
    experiment_data = experiments[selected_tab]
    experiment_data["run_experiment"]()

    # Footer
    st.markdown("""
        <div style='text-align: center; padding: 20px;'>
            Created by <a href="https://github.com/Hakari-Bibani" target="_blank">Hakari Bibani</a> | 
            <a href="https://hawkardemo.streamlit.app/" target="_blank">Visit Demo Site</a>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
