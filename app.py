import streamlit as st
import random

st.set_page_config(page_title="Virtual Chemistry Lab", page_icon="🧪", layout="wide")

# Inject CSS styles
st.markdown("""
<style>
/* Neon glowing text with wave effect */
@keyframes neon {
  0% {
    text-shadow: 0 0 5px #fff;
  }
  50% {
    text-shadow: 0 0 20px #0ff;
  }
  100% {
    text-shadow: 0 0 5px #fff;
  }
}

.glowing-title {
  font-size: 4em;
  color: #fff;
  animation: neon 2s infinite;
  text-align: center;
  margin: 0;
  padding: 20px;
  background-color: rgba(211, 211, 211, 0.1);
  border-radius: 10px;
  display: inline-block;
}

.title-container {
  text-align: center;
  margin-top: 50px;
  position: relative;
  overflow: hidden;
}

.floating-element {
  position: absolute;
  font-size: 2em;
  animation: float 5s infinite;
}

@keyframes float {
  0% { opacity: 0; transform: translateY(100%); }
  50% { opacity: 1; transform: translateY(-100%); }
  100% { opacity: 0; transform: translateY(-200%); }
}

/* Flip card styles */
.flip-card {
  background-color: transparent;
  width: 300px;
  height: 200px;
  perspective: 1000px;
  margin: 20px;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-front, .flip-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
}

.flip-front {
  background-color: lightgreen;
  color: black;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
}

.flip-back {
  background-color: lightpink;
  color: black;
  transform: rotateY(180deg);
  padding: 10px;
  box-sizing: border-box;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.flip-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

</style>
""", unsafe_allow_html=True)

# Title with glowing effect
st.markdown("""
<div class="title-container">
  <h1 class="glowing-title">Virtual Chemistry Lab</h1>
</div>
""", unsafe_allow_html=True)

# Floating elements (emojis and chemical formulas)
floating_elements = ["H₂O 💧", "CO₂ 💨", "🔥", "NaCl", "CH₄ 🔥", "🧪", "🔬", "🧫", "⚛️", "🌡️", "💡"]

# Display floating elements
for elem in floating_elements:
    st.markdown(f"""
    <div class="floating-element" style="top:{random.randint(10, 90)}%; left:{random.randint(10, 90)}%;">
        {elem}
    </div>
    """, unsafe_allow_html=True)

# Flip cards
flip_cards = [
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

# Display flip cards
st.markdown('<div class="flip-container">', unsafe_allow_html=True)
for card in flip_cards:
    st.markdown(f"""
    <div class="flip-card">
      <div class="flip-card-inner">
        <div class="flip-front">
          <h3>{card['name']}</h3>
        </div>
        <div class="flip-back">
          <div>
            <p><strong>Description:</strong> {card['description']}</p>
            <p><strong>Fun Fact:</strong> {card['fun_fact']}</p>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Tabs for experiments
tabs = st.tabs(["Baking Soda and Vinegar Reaction", "Sodium and Water Reaction", "pH Indicator", "Acid-Base Titration", "Elephant Toothpaste Reaction"])

# For each tab, import the corresponding module
with tabs[0]:
    st.header("Baking Soda and Vinegar Reaction")
    # Assuming you have an app() function in reactions/baking.py
    import reactions.baking as baking
    baking.app()
with tabs[1]:
    st.header("Sodium and Water Reaction")
    import reactions.explosion as explosion
    explosion.app()
with tabs[2]:
    st.header("pH Indicator")
    import reactions.indicator as indicator
    indicator.app()
with tabs[3]:
    st.header("Acid-Base Titration")
    import reactions.acid_base as acid_base
    acid_base.app()
with tabs[4]:
    st.header("Elephant Toothpaste Reaction")
    import reactions.elephant_toothpaste as elephant_toothpaste
    elephant_toothpaste.app()

# Hide the Streamlit sidebar
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
---
<p style='text-align: center;'>Created by Hakari Bibani | <a href='https://hawkardemo.streamlit.app/' target='_blank'>https://hawkardemo.streamlit.app/</a></p>
""", unsafe_allow_html=True)
