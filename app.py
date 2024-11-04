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
    initial_sidebar_state="expanded"
)

# Chemistry experiments data
experiments = {
    "Main": {"module": "main"},  # Added main page
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

# Custom CSS for the flip card styling and title animations
def load_css():
    css = """
    <style>
    /* [Previous CSS remains the same until sidebar styling] */

    /* Custom sidebar button styling */
    .sidebar-button {
        width: 100%;
        padding: 10px 15px;
        margin: 5px 0;
        border: none;
        border-radius: 10px;
        background: white;
        color: #1a1a1a;
        font-family: 'Roboto', sans-serif;
        font-weight: 500;
        text-align: left;
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    .sidebar-button:hover {
        background: #f0f0f0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        transform: translateY(-1px);
    }

    .sidebar-button.active {
        background: #e0e0e0;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
    }

    /* Main content styling */
    .main-content {
        padding: 20px;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def render_card(title, content):
    # [Previous render_card function remains the same]
    pass

def load_module(module_name):
    """Dynamically import and return the specified module"""
    try:
        return importlib.import_module(module_name)
    except ImportError as e:
        st.error(f"Error loading module {module_name}: {str(e)}")
        return None

def main():
    load_css()
    
    # Initialize session state for navigation if not exists
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Main'

    # Sidebar navigation with buttons
    with st.sidebar:
        st.title("🧪 Navigation")
        
        # Create a button for each page
        for page_name in experiments.keys():
            if st.button(
                page_name,
                key=f"btn_{page_name}",
                help=f"Go to {page_name}",
                use_container_width=True
            ):
                st.session_state.current_page = page_name
                # Force a rerun to update the page
                st.rerun()

    # Load and display the selected page content
    if st.session_state.current_page == 'Main':
        # Display main page content
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
        experiment_items = list(experiments.items())[1:]  # Skip 'Main'
        for i, (title, content) in enumerate(experiment_items[:3]):
            with top_row[i]:
                render_card(title, content)

        # Second row of cards (2 cards)
        for i, (title, content) in enumerate(experiment_items[3:]):
            with bottom_row[i]:
                render_card(title, content)
    else:
        # Load and display the selected experiment's content
        experiment_data = experiments[st.session_state.current_page]
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
