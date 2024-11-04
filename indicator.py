import streamlit as st
import time
import streamlit.components.v1 as components

# Custom CSS for visuals
st.markdown(
    """
    <style>
    .beaker {
        display: inline-block;
        width: 100px;
        height: 150px;
        background-color: #d3d3d3; /* Light grey solution */
        border-radius: 10px 10px 0 0;
        border: 2px solid #999;
        position: relative;
        margin: 20px;
        text-align: center;
        vertical-align: top;
    }
    .litmus-paper {
        width: 80px;
        height: 10px;
        background-color: black;
        margin-top: 20px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Litmus Paper Experiment")

# Beakers with different solutions
solutions = {
    "Beaker 1": "Neutral (H₂O)",
    "Beaker 2": "Acidic (HCl)",
    "Beaker 3": "Basic (NaOH)"
}
solution_colors = {
    "Neutral (H₂O)": "green",
    "Acidic (HCl)": "red",
    "Basic (NaOH)": "blue"
}

# Display beakers
st.write("### Solutions:")
for beaker, solution in solutions.items():
    st.markdown(
        f"""
        <div class='beaker'>
            <div style='position: absolute; bottom: 10px; width: 100%; text-align: center;'>
                {beaker} <br> <small>{solution}</small>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Litmus Paper
st.write("### Drag the Litmus Paper into a Beaker:")
litmus_paper = st.button("🧪 Litmus Paper")

if litmus_paper:
    # Select a solution (drag and drop simulation)
    selected_solution = st.selectbox("Choose a beaker to dip the litmus paper:", list(solutions.values()))

    if selected_solution:
        # Animate dipping (simulated with loading text)
        with st.spinner(f"Dipping into {selected_solution}..."):
            time.sleep(2)  # Dipping animation duration

        # Change color based on solution
        new_color = solution_colors[selected_solution]
        st.markdown(
            f"""
            <div class='litmus-paper' style='background-color: {new_color}; margin-top: 50px;'>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Hold color for a set duration
        time.sleep(5)

        # Reset litmus paper color
        st.markdown(
            """
            <div class='litmus-paper' style='background-color: black; margin-top: 50px;'>
            </div>
            """,
            unsafe_allow_html=True
        )
