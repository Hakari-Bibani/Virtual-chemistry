import streamlit as st
from streamlit_canvas import st_canvas
import time

# Initialize app
st.title("pH Indicator Test with Litmus Paper")

# Define initial colors and states
litmus_color = "black"
beaker_colors = {
    "neutral": "lightgrey",
    "acid": "lightgrey",
    "base": "lightgrey"
}
litmus_positions = {
    "acid": (150, 150),
    "neutral": (350, 150),
    "base": (550, 150)
}
beaker_labels = ["neutral", "acid", "base"]

# Layout
st.sidebar.write("Drag the black litmus paper to any beaker!")

# Display litmus paper above the beakers
col1, col2, col3 = st.columns(3)
with col2:
    st.write("Litmus Paper")
    st_canvas(
        fill_color=litmus_color,
        width=50,
        height=10,
        background_color="black",
        drawing_mode="rect",
        key="litmus_paper"
    )

# Beaker display function
def display_beaker(label, color):
    st.write(f"{label.capitalize()} Beaker")
    st_canvas(
        fill_color=color,
        width=100,
        height=150,
        background_color=color,
        drawing_mode="rect",
        key=f"{label}_beaker"
    )

# Display beakers
col1, col2, col3 = st.columns(3)
display_beaker("acid", beaker_colors["acid"])
display_beaker("neutral", beaker_colors["neutral"])
display_beaker("base", beaker_colors["base"])

# Drag-and-drop detection (simulated for demo purposes)
def simulate_drag_and_drop(target_beaker):
    global litmus_color
    st.write(f"Litmus Paper dropped in {target_beaker}!")
    
    # Color-changing logic based on solution type
    if target_beaker == "acid":
        litmus_color = "red"
    elif target_beaker == "base":
        litmus_color = "blue"
    else:
        litmus_color = "green"
        
    # Display new color, then revert after a set duration
    time.sleep(5)
    litmus_color = "black"
    st.experimental_rerun()

# User interaction
st.write("Drag the litmus paper to a beaker and see the color change!")
if st.button("Test Acid Solution"):
    simulate_drag_and_drop("acid")
if st.button("Test Base Solution"):
    simulate_drag_and_drop("base")
if st.button("Test Neutral Solution"):
    simulate_drag_and_drop("neutral")

