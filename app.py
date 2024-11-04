import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(
    page_title="Virtual Chemistry Lab",
    page_icon="⚗️",
    layout="wide"
)

# Custom CSS for animations and styling
custom_css = """
<style>
    /* Title container */
    .title-container {
        background-color: rgba(211, 211, 211, 0.1);
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        position: relative;
        overflow: hidden;
    }

    /* Neon title effect */
    .neon-title {
        font-size: 3em;
        font-weight: bold;
        text-align: center;
        color: #fff;
        text-shadow: 0 0 5px #fff,
                     0 0 10px #fff,
                     0 0 20px #ff00de,
                     0 0 30px #ff00de,
                     0 0 40px #ff00de;
        animation: text-glow 2s ease-in-out infinite alternate;
    }

    @keyframes text-glow {
        from {
            text-shadow: 0 0 5px #fff,
                         0 0 10px #fff,
                         0 0 20px #ff00de,
                         0 0 30px #ff00de;
        }
        to {
            text-shadow: 0 0 10px #fff,
                         0 0 20px #fff,
                         0 0 30px #ff00de,
                         0 0 40px #ff00de,
                         0 0 50px #ff00de;
        }
    }

    /* Floating symbols */
    .floating-symbol {
        position: absolute;
        opacity: 0;
        animation: float 4s infinite;
    }

    @keyframes float {
        0% { opacity: 0; transform: translateY(0); }
        50% { opacity: 1; }
        100% { opacity: 0; transform: translateY(-20px); }
    }

    /* Flip cards container */
    .cards-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        margin: 20px 0;
    }

    /* Flip card */
    .flip-card {
        width: 300px;
        height: 200px;
        perspective: 1000px;
        margin: 10px;
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.8s;
        transform-style: preserve-3d;
        cursor: pointer;
    }

    .flip-card:hover .flip-card-inner {
        transform: rotateY(180deg);
    }

    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
        border-radius: 10px;
    }

    .flip-card-front {
        background-color: rgba(144, 238, 144, 0.3);
        color: black;
    }

    .flip-card-back {
        background-color: rgba(255, 192, 203, 0.3);
        color: black;
        transform: rotateY(180deg);
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 20px;
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: rgba(255, 255, 255, 0.1);
    }
</style>
"""

# HTML for the title section with floating symbols
title_html = """
<div class="title-container">
    <h1 class="neon-title">Virtual Chemistry Lab</h1>
    <div class="floating-symbols">
        <span class="floating-symbol" style="left: 10%; animation-delay: 0s;">H₂O 💧</span>
        <span class="floating-symbol" style="left: 20%; animation-delay: 1s;">CO₂ 💨</span>
        <span class="floating-symbol" style="left: 30%; animation-delay: 2s;">🔥</span>
        <span class="floating-symbol" style="left: 40%; animation-delay: 3s;">NaCl</span>
        <span class="floating-symbol" style="left: 50%; animation-delay: 4s;">CH₄ 🔥</span>
        <span class="floating-symbol" style="right: 40%; animation-delay: 5s;">🧪</span>
        <span class="floating-symbol" style="right: 30%; animation-delay: 6s;">🔬</span>
        <span class="floating-symbol" style="right: 20%; animation-delay: 7s;">🧫</span>
        <span class="floating-symbol" style="right: 10%; animation-delay: 8s;">⚛️</span>
    </div>
</div>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(title_html, unsafe_allow_html=True)

# Create tabs
tabs = st.tabs([
    "Baking Soda and Vinegar",
    "Sodium and Water",
    "pH Indicator",
    "Acid-Base Titration",
    "Elephant Toothpaste"
])

# Flip cards data
cards_data = [
    {
        "name": "Sodium and Water Reaction",
        "description": "Sodium metal reacts with water, producing hydrogen gas and heat, often resulting in a small flame or explosion.",
        "fun_fact": "This reaction showcases the reactivity of alkali metals, especially with water."
    },
    {
        "name": "pH Indicator",
        "description": "A reaction where an indicator changes color based on the pH of the solutions.",
        "fun_fact": "pH indicators are widely used in labs and even in gardening to test soil acidity!"
    },
    {
        "name": "Acid-Base Titration",
        "description": "A process where an acid is neutralized by a base, or vice versa, typically resulting in a pH change.",
        "fun_fact": "Titrations are commonly used in labs to determine the concentration of an unknown solution."
    },
    {
        "name": "Elephant Toothpaste Reaction",
        "description": "The decomposition of hydrogen peroxide, catalyzed by potassium iodide, produces a large volume of oxygen gas and foam.",
        "fun_fact": "This reaction is famous for its foamy explosion and is popular in science demonstrations."
    },
    {
        "name": "Baking Soda and Vinegar Reaction",
        "description": "A simple acid-base reaction between vinegar and baking soda, producing carbon dioxide gas.",
        "fun_fact": "This reaction is commonly used in DIY volcanoes and as a cleaning agent."
    }
]

# Generate flip cards HTML
cards_html = """
<div class="cards-container">
"""

for i, card in enumerate(cards_data):
    cards_html += f"""
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front">
                <h3>{card['name']}</h3>
            </div>
            <div class="flip-card-back">
                <div>
                    <p><strong>Description:</strong> {card['description']}</p>
                    <p><strong>Fun Fact:</strong> {card['fun_fact']}</p>
                </div>
            </div>
        </div>
    </div>
    """

cards_html += "</div>"

# Display flip cards
st.markdown(cards_html, unsafe_allow_html=True)

# Footer
footer_html = """
<div class="footer">
    Created by Hakari Bibani | 
    <a href="https://hawkardemo.streamlit.app/" target="_blank">Visit Demo</a>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)

# Import and use reaction modules based on selected tab
with tabs[0]:
    from reactions.baking import show_reaction
    show_reaction()

with tabs[1]:
    from reactions.explosion import show_reaction
    show_reaction()

with tabs[2]:
    from reactions.indicator import show_reaction
    show_reaction()

with tabs[3]:
    from reactions.acid_base import show_reaction
    show_reaction()

with tabs[4]:
    from reactions.elephant_toothpaste import show_reaction
    show_reaction()
