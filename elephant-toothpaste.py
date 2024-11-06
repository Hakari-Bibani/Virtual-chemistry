import streamlit as st
import time

def run_experiment():
    # Custom CSS for enhanced styling and animations
    st.markdown("""
    <style>
        /* (CSS code remains the same here) */
    </style>
    """, unsafe_allow_html=True)

    # Display the title
    st.markdown("<h1 class='title'>Chemical Reaction Animation</h1>", unsafe_allow_html=True)
    
    # Container for the experiment
    container = st.empty()
    
    def render_initial_state():
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="label">H₂O₂</div>
                    <div class="solution"></div>
                </div>
                <div class="cylinder">
                    <div class="solution"></div>
                    <div class="foam"></div>
                    <div class="label">30% KI</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    def animate_reaction():
        # Step 1: Pour the solution
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker pouring">
                    <div class="label">H₂O₂</div>
                    <div class="solution"></div>
                </div>
                <div class="cylinder">
                    <div class="solution"></div>
                    <div class="foam"></div>
                    <div class="label">30% KI</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        time.sleep(1)
        
        # Step 2: Return beaker and start reaction
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="label">H₂O₂</div>
                    <div class="solution"></div>
                </div>
                <div class="cylinder reacting">
                    <div class="solution"></div>
                    <div class="foam"></div
