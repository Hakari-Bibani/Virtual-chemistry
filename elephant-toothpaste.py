import streamlit as st
import time

def run_experiment():
    # Custom CSS for enhanced styling and animations
    st.markdown("""
    <style>
        /* Your CSS here */
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
                    <div class="foam"></div>
                    <div class="label">30% KI</div>
                    <div class="particle" style="--tx: 30px; --ty: -60px;"></div>
                    <div class="particle" style="--tx: -25px; --ty: -55px;"></div>
                    <div class="particle" style="--tx: 15px; --ty: -65px;"></div>
                    <div class="particle" style="--tx: -35px; --ty: -50px;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    render_initial_state()
    
    if st.button("Start Reaction"):
        animate_reaction()
        st.markdown("""
            **Chemical Reaction:**
            2 H₂O₂ (aq) + 30% KI (aq) → 2 H₂O (l) + O₂ (g) + KI (aq)
            
            **Note:** The rapid decomposition of hydrogen peroxide is catalyzed by potassium iodide, 
            producing water and oxygen gas. The dramatic foam effect is created by the rapid release of oxygen gas.
        """)
        
        st.button("Reset Experiment", on_click=run_experiment)

if __name__ == "__main__":
    run_experiment()
