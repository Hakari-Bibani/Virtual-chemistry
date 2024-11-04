import streamlit as st
import time

# Page configuration
st.set_page_config(page_title="pH Indicator Test", layout="centered")

# CSS for styling the beakers, litmus paper, and animations
st.markdown(
    """
    <style>
        .beaker {
            display: inline-block;
            width: 100px;
            height: 150px;
            margin: 20px;
            background-color: lightgrey;
            border-radius: 10px;
            border: 2px solid #555;
            text-align: center;
            position: relative;
        }

        .litmus-paper {
            width: 40px;
            height: 80px;
            background-color: black;
            margin: 0 auto;
            position: relative;
            top: -50px;
            cursor: pointer;
        }

        .litmus-immersed {
            transition: top 1s ease, background-color 1s ease;
        }

        .solution-label {
            font-weight: bold;
            position: absolute;
            bottom: 5px;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

# Display the litmus paper and beakers
st.write("### Drag the litmus paper into a beaker to test its pH")

col1, col2, col3 = st.columns(3)

# Initial litmus paper
if "litmus_color" not in st.session_state:
    st.session_state.litmus_color = "black"

# Define the beakers and their contents
beakers = {
    "acidic": {"name": "HCl (Acid)", "color": "red"},
    "neutral": {"name": "H2O (Neutral)", "color": "green"},
    "basic": {"name": "NaOH (Base)", "color": "blue"},
}

# Render the beakers
with col1:
    st.write('<div class="beaker"><div class="solution-label">Acid (HCl)</div></div>', unsafe_allow_html=True)

with col2:
    st.write('<div class="beaker"><div class="solution-label">Neutral (H₂O)</div></div>', unsafe_allow_html=True)

with col3:
    st.write('<div class="beaker"><div class="solution-label">Base (NaOH)</div></div>', unsafe_allow_html=True)

# Drag-and-drop logic
st.write("#### Drag the litmus paper below into one of the beakers to test")
st.markdown('<div class="litmus-paper" id="litmus-paper"></div>', unsafe_allow_html=True)

# JavaScript for drag-and-drop functionality
st.markdown(
    """
    <script>
    const litmus = document.getElementById("litmus-paper");
    const beakers = document.querySelectorAll(".beaker");

    beakers.forEach(beaker => {
        beaker.ondrop = (event) => {
            event.preventDefault();
            testLitmus(beaker);
        };
        beaker.ondragover = (event) => {
            event.preventDefault();
        };
    });

    function testLitmus(beaker) {
        let color = beaker.querySelector('.solution-label').textContent.includes("Acid") ? "red" :
                    beaker.querySelector('.solution-label').textContent.includes("Neutral") ? "green" : "blue";
        
        litmus.style.backgroundColor = color;
        litmus.classList.add("litmus-immersed");
        
        setTimeout(() => {
            litmus.style.backgroundColor = "black";
            litmus.classList.remove("litmus-immersed");
        }, 5000);
    }
    </script>
    """,
    unsafe_allow_html=True
)

st.write("### Test Instructions")
st.markdown("""
1. Drag the litmus paper into a beaker.
2. Observe the color change.
3. After 5 seconds, the litmus paper will revert to black.
4. Repeat with another beaker to test different solutions.
""")
