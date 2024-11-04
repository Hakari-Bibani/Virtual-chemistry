import streamlit as st
import time

# Streamlit App Title
st.title("Litmus Paper Experiment")

# Instructions
st.write("""
### Instructions:
1. Choose a beaker solution type below.
2. Click "Dip Litmus Paper" to see the color change based on the solution type.
3. After a few seconds, the litmus paper will reset.
""")

# Solution type selection
solution_type = st.radio(
    "Select a Beaker Solution:",
    ("Neutral (H2O)", "Acidic (HCl)", "Basic (NaOH)")
)

# Button to "dip" the litmus paper
if st.button("Dip Litmus Paper"):
    # Initialize litmus paper color to black
    litmus_color = "black"

    # Determine the color change based on the selected solution
    if solution_type == "Neutral (H2O)":
        litmus_color = "green"
    elif solution_type == "Acidic (HCl)":
        litmus_color = "red"
    elif solution_type == "Basic (NaOH)":
        litmus_color = "blue"

    # Display the color change
    litmus_placeholder = st.empty()
    litmus_placeholder.markdown(f"### Litmus Paper Color: {litmus_color.capitalize()}")
    time.sleep(5)  # Hold the color change for 5 seconds

    # Reset the litmus paper color back to black
    litmus_placeholder.markdown("### Litmus Paper Color: Black")
else:
    st.markdown("### Litmus Paper Color: Black")  # Initial display

# Display beakers
st.write("""
#### Beaker Visuals:
* Neutral Solution: Grey
* Acidic Solution: Light Red
* Basic Solution: Light Blue
""")
st.image("path_to_your_beaker_images.png")  # Placeholder for visuals
