import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

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
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    .title-container {
        text-align: center;
        margin-bottom: 40px;
        padding: 30px;
        background: #f0f0f0;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        position: relative;
        overflow: hidden;
    }

    @keyframes titlePulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }

    @keyframes titleWave {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
        100% { transform: translateY(0px); }
    }

    @keyframes glowShift {
        0% { text-shadow: 0 0 10px rgba(0,0,139,0.7), 0 0 20px rgba(0,0,139,0.5); }
        50% { text-shadow: 0 0 15px rgba(255,0,0,0.7), 0 0 25px rgba(255,0,0,0.5); }
        100% { text-shadow: 0 0 10px rgba(0,0,139,0.7), 0 0 20px rgba(0,0,139,0.5); }
    }

    .glowing-title {
        font-family: 'Roboto', sans-serif;
        font-size: 3.5em;
        color: #00008B;
        animation: titlePulse 3s infinite ease-in-out, titleWave 4s infinite ease-in-out, glowShift 6s infinite ease-in-out;
        margin: 20px 0;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .icons-container {
        margin: 20px 0;
        position: relative;
        height: 60px;
    }

    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-15px) rotate(180deg); }
        100% { transform: translateY(0px) rotate(360deg); }
    }

    .chemistry-icon {
        font-size: 2.5em;
        display: inline-block;
        margin: 0 15px;
        animation: float 3s ease-in-out infinite;
    }

    @keyframes fadeInOut {
        0% { opacity: 0; transform: translateY(20px); }
        50% { opacity: 1; transform: translateY(0); }
        100% { opacity: 0; transform: translateY(-20px); }
    }

    .floating-formula {
        position: absolute;
        font-size: 1.2em;
        opacity: 0;
        animation: fadeInOut 4s infinite;
    }

    .formula1 { left: 10%; top: 20%; animation-delay: 0s; }
    .formula2 { left: 20%; top: 60%; animation-delay: 1s; }
    .formula3 { left: 80%; top: 30%; animation-delay: 2s; }
    .formula4 { left: 70%; top: 70%; animation-delay: 3s; }
    .formula5 { left: 40%; top: 40%; animation-delay: 1.5s; }

    .flip-card {
        background-color: transparent;
        width: 100%;
        height: 400px;
        perspective: 1000px;
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.8s;
        transform-style: preserve-3d;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }

    .flip-card:hover .flip-card-inner {
        transform: rotateY(180deg);
    }

    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        border-radius: 20px;
        padding: 20px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .flip-card-front {
        background: linear-gradient(145deg, #a8e6cf 0%, #98FB98 100%);
        color: #1a1a1a;
    }

    .flip-card-back {
        background: linear-gradient(145deg, #FFB6C6 0%, #ffd1dc 100%);
        color: #1a1a1a;
        transform: rotateY(180deg);
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

if __name__ == "__main__":
    main()
