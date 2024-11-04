import streamlit as st
import importlib  # For dynamic loading of reaction files
from pathlib import Path

# Configure page settings
st.set_page_config(
    page_title="Virtual Chemistry Lab",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Define sidebar navigation options
reaction_tabs = {
    "Acid Base": "acid_base",
    "Elephant Toothpaste": "elephant_toothpaste",
    "Indicator": "indicator",
    "Explosion": "explosion",
    "Baking Soda & Vinegar": "baking"
}

# Sidebar with navigation options
selected_tab = st.sidebar.selectbox("Choose an Experiment", list(reaction_tabs.keys()))

# Load CSS for styling
def load_css():
    # Your existing CSS here
    pass

# Function to render the main page cards
def render_card(title, content):
    # Your existing render_card code here
    pass

def main():
    load_css()
    
    # Main title and animated icons
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

    # Experiment cards
    experiments = {
        "Baking Soda and Vinegar Reaction": {
            "description": "A classic acid-base reaction that produces carbon dioxide gas.",
            "visualization": "Fizzing and bubbling as CO2 is released.",
            "fun_fact": "This reaction is commonly used in science fair volcanoes!"
        },
        "Sodium and Water Reaction": {
            "description": "Sodium metal reacts with water, producing hydrogen gas and heat.",
            "visualization": "Bubbles and flames as hydrogen gas ignites.",
            "fun_fact": "This reaction showcases the reactivity of alkali metals, especially with water."
        },
        "pH Indicator": {
            "description": "A reaction where an indicator changes color based on the pH.",
            "visualization": "Litmus turning red in acid, blue in base, green in neutral.",
            "fun_fact": "pH indicators are used in labs and gardening!"
        },
        "Acid-Base Titration": {
            "description": "A process where an acid is neutralized by a base.",
            "visualization": "A pH curve that changes as titrant is added.",
            "fun_fact": "Titrations help determine unknown concentrations."
        },
        "Elephant Toothpaste Reaction": {
            "description": "Decomposition of hydrogen peroxide produces oxygen gas and foam.",
            "visualization": "Expanding foam like giant toothpaste.",
            "fun_fact": "Famous for its foamy explosion in demonstrations!"
        }
    }

    # Display the experiment cards in rows
    top_row = st.columns(3)
    bottom_row = st.columns(2)

    # Render cards in two rows
    for i, (title, content) in enumerate(list(experiments.items())[:3]):
        with top_row[i]:
            render_card(title, content)
    for i, (title, content) in enumerate(list(experiments.items())[3:]):
        with bottom_row[i]:
            render_card(title, content)

    # Load the selected reaction file
    if selected_tab in reaction_tabs:
        # Import the corresponding module
        reaction_module = importlib.import_module(reaction_tabs[selected_tab])
        reaction_module.main()  # Assuming each reaction file has a main() function to execute the code

    # Footer
    st.markdown("""
        <div style='text-align: center; padding: 20px;'>
            Created by <a href="https://github.com/Hakari-Bibani" target="_blank">Hakari Bibani</a> | 
            <a href="https://hawkardemo.streamlit.app/" target="_blank">Visit Demo Site</a>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
