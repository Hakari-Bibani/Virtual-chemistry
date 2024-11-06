import streamlit as st
import time

def run_experiment():
    # Custom CSS for enhanced styling and animations
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@600&display=swap');
        
        .title {
            font-family: 'Rajdhani', sans-serif;
            font-size: 2.8em;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: linear-gradient(45deg, #2c3e50, #3498db, #2c3e50);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-size: 200% auto;
            animation: gradient 3s linear infinite;
        }
        
        .experiment-container {
            display: flex;
            justify-content: center;
            align-items: flex-end;
            position: relative;
            height: 500px;
            margin-bottom: 20px;
            overflow: visible;
        }
        
        .beaker {
            width: 80px;
            height: 120px;
            border: 3px solid #ddd;
            border-radius: 5px 5px 10px 10px;
            position: absolute;
            left: 22%;  /* Moved further left from 28% */
            top: 5%;
            transform-origin: bottom right;
            transition: transform 1s ease;
            z-index: 2;
        }
        
        .cylinder {
            width: 160px;
            height: 240px;
            border: 4px solid #ddd;
            border-radius: 10px 10px 20px 20px;
            position: relative;
            overflow: visible;
            margin-top: 120px;
        }
        
        .solution {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 50%;
            transition: all 1s ease;
        }
        
        .beaker .solution {
            background: rgba(176, 224, 230, 0.7);
        }
        
        .cylinder .solution {
            background: rgba(169, 169, 169, 0.7);
        }
        
        .beaker .label {
            position: absolute;
            top: -25px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 14px;
            font-weight: bold;
            color: #2c3e50;
        }
        
        .cylinder .label {
            position: absolute;
            bottom: -30px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 14px;
            font-weight: bold;
            color: #2c3e50;
        }
        
        @keyframes pour {
            0% { height: 50%; }
            50% { height: 0%; }
            100% { height: 0%; }
        }
        
        .foam {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 0;
            background: repeating-linear-gradient(
                0deg,
                rgba(0, 0, 0, 0.3) 0px,
                rgba(0, 0, 0, 0.3) 20px,
                rgba(255, 0, 0, 0.3) 20px,
                rgba(255, 0, 0, 0.3) 40px
            );
            animation: none;
            filter: drop-shadow(0 0 5px rgba(255, 0, 0, 0.2));
        }
        
        @keyframes reaction {
            0% {
                height: 50%;
                transform: translateY(0);
            }
            20% {
                height: 100%;
                transform: translateY(0);
            }
            40% {
                height: 100%;
                transform: translateY(-50%);
            }
            60% {
                height: 100%;
                transform: translateY(-100%);
            }
            80% {
                height: 100%;
                transform: translateY(-120%);
                opacity: 1;
            }
            100% {
                height: 100%;
                transform: translateY(-140%);
                opacity: 0;
            }
        }
        
        .pouring {
            transform: rotate(65deg) translateY(-20px) translateX(60px);
        }
        
        .pouring .solution {
            animation: pour 1s ease forwards;
        }
        
        .reacting .foam {
            animation: reaction 1.5s ease-out forwards;
        }
        
        .reacting .solution {
            animation: empty 1.5s ease-out forwards;
        }
        
        @keyframes empty {
            0% { height: 50%; }
            100% { height: 0%; }
        }
        
        .particle {
            position: absolute;
            width: 12px;
            height: 12px;
            background: repeating-linear-gradient(
                45deg,
                rgba(0, 0, 0, 0.3) 0px,
                rgba(0, 0, 0, 0.3) 6px,
                rgba(255, 0, 0, 0.3) 6px,
                rgba(255, 0, 0, 0.3) 12px
            );
            border-radius: 50%;
            opacity: 0;
        }
        
        @keyframes particle {
            0% {
                transform: translate(0, 0) rotate(0deg);
                opacity: 1;
            }
            100% {
                transform: translate(var(--tx), var(--ty)) rotate(360deg);
                opacity: 0;
            }
        }
        
        .reacting .particle {
            animation: particle 1s ease-out forwards;
        }
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
                    <!-- Add foam particles -->
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
