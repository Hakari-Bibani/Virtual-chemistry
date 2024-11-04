# indicator.py
import streamlit as st
import time
from PIL import Image
import numpy as np
import io
import base64
from streamlit_draggable import st_draggable

def create_beaker_svg(color="#f0f0f0"):
    return f"""
    <svg width="100" height="150" viewBox="0 0 100 150">
        <path d="M20 30 L20 120 Q20 140 40 140 L60 140 Q80 140 80 120 L80 30 Z" 
              fill="{color}" stroke="black" stroke-width="2"/>
        <path d="M15 30 L85 30" stroke="black" stroke-width="2"/>
    </svg>
    """

def create_litmus_paper_svg(color="black"):
    return f"""
    <svg width="20" height="80" viewBox="0 0 20 80">
        <rect x="5" y="0" width="10" height="80" fill="{color}" stroke="none"/>
    </svg>
    """

def main():
    st.title("Interactive Litmus Paper Experiment")
    st.markdown("""
    ### Instructions:
    1. Drag the litmus paper into any beaker to test the solution
    2. Watch the color change based on the pH:
        - Green = Neutral (H₂O)
        - Red = Acidic (HCl)
        - Blue = Basic (NaOH)
    3. The paper will reset after 5 seconds
    """)

    # Initialize session state
    if 'dragging' not in st.session_state:
        st.session_state.dragging = False
    if 'last_drop_time' not in st.session_state:
        st.session_state.last_drop_time = time.time()
    if 'current_color' not in st.session_state:
        st.session_state.current_color = "black"

    # Create container for beakers
    col1, col2, col3 = st.columns(3)
    
    # Display beakers
    with col1:
        st.markdown("### H₂O")
        st.markdown(create_beaker_svg(), unsafe_allow_html=True)
        st.markdown("(Neutral)")
        
    with col2:
        st.markdown("### HCl")
        st.markdown(create_beaker_svg(), unsafe_allow_html=True)
        st.markdown("(Acidic)")
        
    with col3:
        st.markdown("### NaOH")
        st.markdown(create_beaker_svg(), unsafe_allow_html=True)
        st.markdown("(Basic)")

    # Create draggable litmus paper
    paper_position = st_draggable("litmus_paper", 
                                create_litmus_paper_svg(st.session_state.current_color),
                                key="paper")

    # Handle paper position and color changes
    if paper_position:
        x, y = paper_position['x'], paper_position['y']
        
        # Define drop zones for each beaker
        beaker_zones = {
            'h2o': {'x': (50, 150), 'y': (100, 250)},
            'hcl': {'x': (200, 300), 'y': (100, 250)},
            'naoh': {'x': (350, 450), 'y': (100, 250)}
        }
        
        # Check if paper is dropped in any beaker
        current_time = time.time()
        for solution, zone in beaker_zones.items():
            if (zone['x'][0] <= x <= zone['x'][1] and 
                zone['y'][0] <= y <= zone['y'][1] and 
                current_time - st.session_state.last_drop_time > 5):
                
                st.session_state.last_drop_time = current_time
                
                # Change color based on solution
                if solution == 'h2o':
                    st.session_state.current_color = "green"
                elif solution == 'hcl':
                    st.session_state.current_color = "red"
                elif solution == 'naoh':
                    st.session_state.current_color = "blue"
                
                # Reset color after 5 seconds
                time.sleep(0.5)  # Animation delay
                st.experimental_rerun()

    # Reset color if 5 seconds have passed
    if time.time() - st.session_state.last_drop_time > 5:
        st.session_state.current_color = "black"

if __name__ == "__main__":
    main()
