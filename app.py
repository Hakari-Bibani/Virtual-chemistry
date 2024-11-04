import streamlit as st
import importlib
from pathlib import Path

# Configure page settings
st.set_page_config(
    page_title="Virtual Chemistry Lab",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Chemistry experiments data
experiments = {
    "Baking Soda and Vinegar Reaction": {
        "module": "baking"
    },
    "Sodium and Water Reaction": {
        "module": "explosion"
    },
    "pH Indicator": {
        "module": "indicator"
    },
    "Acid-Base Titration": {
        "module": "acid_base"
    },
    "Elephant Toothpaste Reaction": {
        "module": "elephant_toothpaste"
    }
}

# Custom CSS for the sidebar and other elements
def load_css():
    css = """
    /* ... (previous CSS code remains unchanged) ... */

    /* Custom sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f0f0f0 0%, #e0e0e0 100%);
    }

    .sidebar .element-container {
        background: transparent;
    }

    .sidebar .stButton > button {
        background: white;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        transition: all 0.3s ease;
        font-family: 'Roboto', sans-serif;
        font-weight: 500;
        color: #1a1a1a;
        width: 100%;
        text-align: left;
    }

    .sidebar .stButton > button:hover {
        background: #f8f8f8;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def load_module(module_name):
    """Dynamically import and return the specified module"""
    try:
        return importlib.import_module(module_name)
    except ImportError as e:
        st.error(f"Error loading module {module_name}: {str(e)}")
        return None

def main():
    load_css()
    
    # Sidebar navigation
    with st.sidebar:
        st.title("🧪 Experiments")
        selected_tab = st.selectbox("Select Experiment", ["Overview"] + list(experiments.keys()))

    # Main content area
    if selected_tab == "Overview":
        render_overview()
    else:
        render_experiment(selected_tab)

def render_overview():
    # Title container with animations and icons
    render_title()

    # Create the layout with two rows: top row with three cards, bottom row with two
    top_row = st.columns(3)
    bottom_row = st.columns(2)

    # First row of cards (3 cards)
    for i, (title, content) in enumerate(list(experiments.items())[:3]):
        with top_row[i]:
            render_card(title, content)

    # Second row of cards (2 cards)
    for i, (title, content) in enumerate(list(experiments.items())[3:]):
        with bottom_row[i]:
            render_card(title, content)

    # Footer
    render_footer()

def render_experiment(experiment_name):
    experiment_data = experiments[experiment_name]
    module_name = experiment_data["module"]
    module = load_module(module_name)
    
    if module and hasattr(module, 'run_experiment'):
        # Set the page title to the experiment name
        st.set_page_config(page_title=experiment_name)
        module.run_experiment()
    else:
        st.warning(f"The experiment module '{module_name}' is not properly configured.")

def render_title():
    st.markdown("""
        <div class='title-container'>
            <div class='floating-formula formula1'>H₂O 💧</div>
            <div class='floating-formula formula2'>CO₂ ⚡</div>
            <div class='floating-formula formula3'>O₂ 🔥</div>
            <div class='floating-formula formula4'>NaCl ✨</div>
            <div class='floating-formula formula5'>CH₄ 💨</div>
            <h1 class='glowing-title'>Virtual Chemistry Lab</h1>
            <div class='icons-container'>
                <span class='chemistry-icon'>⚗️</span>
                <span class='chemistry-icon'>🧪</span>
                <span class='chemistry-icon'>🔬</span>
                <span class='chemistry-icon'>🧫</span>
                <span class='chemistry-icon'>⚛️</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

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

def render_footer():
    st.markdown("""
        <div style='text-align: center; padding: 20px;'>
            Created by <a href="https://github.com/Hakari-Bibani" target="_blank">Hakari Bibani</a> | 
            <a href="https://hawkardemo.streamlit.app/" target="_blank">Visit Demo Site</a>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
