import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import importlib
import sys

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
        "description": "A classic acid-base reaction that produces carbon dioxide gas.",
        "visualization": "Fizzing and bubbling as CO2 is released.",
        "fun_fact": "This reaction is commonly used in science fair volcanoes!",
        "module": "baking"
    },
    "Sodium and Water Reaction": {
        "description": "Sodium metal reacts with water, producing hydrogen gas and heat.",
        "visualization": "Bubbles and flames as hydrogen gas ignites.",
        "fun_fact": "This reaction showcases the reactivity of alkali metals, especially with water.",
        "module": "explosion"
    },
    "pH Indicator": {
        "description": "A reaction where an indicator changes color based on the pH.",
        "visualization": "Litmus turning red in acid, blue in base, green in neutral.",
        "fun_fact": "pH indicators are used in labs and gardening!",
        "module": "indicator"
    },
    "Acid-Base Titration": {
        "description": "A process where an acid is neutralized by a base.",
        "visualization": "A pH curve that changes as titrant is added.",
        "fun_fact": "Titrations help determine unknown concentrations.",
        "module": "acid_base"
    },
    "Elephant Toothpaste Reaction": {
        "description": "Decomposition of hydrogen peroxide produces oxygen gas and foam.",
        "visualization": "Expanding foam like giant toothpaste.",
        "fun_fact": "Famous for its foamy explosion in demonstrations!",
        "module": "elephant_toothpaste"
    }
}

# Custom CSS for styling
def load_css():
    css = """
    <style>
    /* CSS code for styling flip cards, animations, and sidebar */
    /* Additional styling for selected button-like tabs */
    .stRadio > div[role="radiogroup"] > label {
        background: black;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        transition: all 0.3s ease;
    }
    .stRadio > div[role="radiogroup"] > label:hover {
        background: #333;
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

def load_module(module_name):
    """Dynamically import and return the specified module"""
    try:
        return importlib.import_module(module_name)
    except ImportError as e:
        st.error(f"Error loading module {module_name}: {str(e)}")
        return None

def main():
    load_css()
    
    # Sidebar navigation with button-styled tabs
    with st.sidebar:
        st.title("🧪 Experiments")
        tabs = ["Overview"] + list(experiments.keys())
        selected_tab = st.radio(
            "Select Experiment",
            tabs,
            format_func=lambda x: f"⬤ {x}" if x == selected_tab else x
        )
    
    # Title container with animations and icons for the main overview page only
    if selected_tab == "Overview":
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
    else:
        # Load and display the selected experiment's content
        experiment_data = experiments[selected_tab]
        module_name = experiment_data["module"]
        module = load_module(module_name)
        
        if module and hasattr(module, 'run_experiment'):
            module.run_experiment()
        else:
            st.warning(f"The experiment module '{module_name}' is not properly configured.")

    # Footer
    st.markdown("""
        <div style='text-align: center; padding: 20px;'>
            Created by <a href="https://github.com/Hakari-Bibani" target="_blank">Hakari Bibani</a> | 
            <a href="https://hawkardemo.streamlit.app/" target="_blank">Visit Demo Site</a>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
