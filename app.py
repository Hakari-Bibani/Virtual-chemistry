import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

# Import the experiment pages
import acid_base
import elephant_toothpaste
import indicator
import explosion
import baking

# Configure page settings
st.set_page_config(
    page_title="Virtual Chemistry Lab",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Chemistry experiments data for the main page cards
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

# Custom CSS for the flip card styling and title animations
def load_css():
    css = """
    <style>
    /* Your CSS styling code here */
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
    # Load CSS for styling
    load_css()
    
    # Sidebar for experiment navigation
    st.sidebar.title("Experiments")
    experiment_choice = st.sidebar.radio(
        "Choose an experiment:",
        ("Main Page", "Acid Base", "Elephant Toothpaste", "Indicator", "Explosion", "Baking Soda & Vinegar")
    )

    # Display main page or selected experiment page
    if experiment_choice == "Main Page":
        # Title container with animations and icons
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

        # Footer
        st.markdown("""
            <div style='text-align: center; padding: 20px;'>
                Created by <a href="https://github.com/Hakari-Bibani" target="_blank">Hakari Bibani</a> | 
                <a href="https://hawkardemo.streamlit.app/" target="_blank">Visit Demo Site</a>
            </div>
        """, unsafe_allow_html=True)

    elif experiment_choice == "Acid Base":
        acid_base.run()

    elif experiment_choice == "Elephant Toothpaste":
        elephant_toothpaste.run()

    elif experiment_choice == "Indicator":
        indicator.run()

    elif experiment_choice == "Explosion":
        explosion.run()

    elif experiment_choice == "Baking Soda & Vinegar":
        baking.run()

if __name__ == "__main__":
    main()
