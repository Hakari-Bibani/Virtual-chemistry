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

# Custom CSS for the flip card styling and title animations
def load_css():
    css = """
    <style>
    /* Previous CSS remains unchanged */
    [Previous CSS code remains the same until the sidebar styling]

    /* New Navigation Button Styling */
    .stButton > button {
        width: 100%;
        background-color: black;
        color: white;
        border: none;
        padding: 10px 15px;
        border-radius: 5px;
        margin: 5px 0;
        font-family: 'Roboto', sans-serif;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #333;
        transform: translateY(-2px);
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    .stButton > button:active {
        transform: translateY(0);
    }

    /* Active button style */
    .stButton > button.active {
        background-color: #444;
        border-left: 4px solid #00f;
    }

    /* Sidebar header styling */
    .sidebar-header {
        padding: 20px 0;
        text-align: center;
        border-bottom: 2px solid #eee;
        margin-bottom: 20px;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# [Previous functions remain unchanged: render_card, load_module]

def create_nav_buttons():
    """Create navigation buttons in the sidebar"""
    with st.sidebar:
        st.markdown('<div class="sidebar-header"><h2>🧪 Experiments</h2></div>', unsafe_allow_html=True)
        
        # Create a button for Overview
        if st.button("Overview", key="overview"):
            st.session_state.selected_tab = "Overview"
            
        # Create buttons for each experiment
        for exp_name in experiments.keys():
            if st.button(exp_name, key=exp_name):
                st.session_state.selected_tab = exp_name

def main():
    load_css()
    
    # Initialize session state for selected tab if not exists
    if 'selected_tab' not in st.session_state:
        st.session_state.selected_tab = "Overview"
    
    # Create navigation buttons
    create_nav_buttons()
    
    # Only show title container on Overview page
    if st.session_state.selected_tab == "Overview":
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
        experiment_data = experiments[st.session_state.selected_tab]
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
