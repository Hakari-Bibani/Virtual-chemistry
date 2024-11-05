# indicator.py
import streamlit as st
import time

def run_experiment():
    # Custom CSS with enhanced styling and animations
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
            position: relative;
            background: linear-gradient(45deg, #2c3e50, #3498db, #2c3e50);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-size: 200% auto;
            animation: gradient 3s linear infinite, float 3s ease-in-out infinite;
        }
    
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            100% { background-position: 200% 50%; }
        }
    
        @keyframes float {
            0%, 100% { transform: translateY(0) rotate(-2deg); }
            50% { transform: translateY(-10px) rotate(2deg); }
        }
    
        .litmus-container {
            display: flex;
            justify-content: space-around;
            margin: 20px 0;
            padding: 20px;
            height: 120px;
        }
        
        .beaker-container {
            display: flex;
            justify-content: space-around;
            margin: 20px 0;
            padding: 20px;
            position: relative;
        }
        
        .litmus {
            width: 30px;
            height: 100px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            transition: all 1.5s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
        }
        
        .beaker {
            width: 120px;
            height: 150px;
            position: relative;
            background: rgba(255,255,255,0.1);
            border: 3px solid #ddd;
            border-top: 15px solid #ddd;
            border-radius: 10px 10px 20px 20px;
            text-align: center;
            padding-top: 10px;
            margin-bottom: 40px;
            overflow: hidden;
        }
        
        .solution {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 80%;
            border-radius: 0 0 17px 17px;
            animation: liquidWave 4s infinite ease-in-out;
        }
    
        .solution::before {
            content: '';
            position: absolute;
            top: -10px;
            left: -10px;
            right: -10px;
            height: 20px;
            background: inherit;
            filter: blur(5px);
            opacity: 0.7;
            animation: surfaceWave 2s infinite ease-in-out;
        }
    
        @keyframes liquidWave {
            0%, 100% { 
                transform: translateY(2px) scaleY(1.02);
                filter: brightness(100%);
            }
            50% { 
                transform: translateY(-2px) scaleY(0.98);
                filter: brightness(105%);
            }
        }
    
        @keyframes surfaceWave {
            0%, 100% { transform: translateX(-5px); }
            50% { transform: translateX(5px); }
        }
    
        .beaker-label {
            font-family: 'Rajdhani', sans-serif;
            font-size: 14px;
            text-align: center;
            margin-top: 15px;
            color: #2c3e50;
            max-width: 120px;
            word-wrap: break-word;
            font-weight: 600;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Title with animation
    st.markdown("<h1 class='title'>Test the pH of different solutions using litmus paper!</h1>", unsafe_allow_html=True)
    
    # Create placeholders for dynamic content
    litmus_placeholder = st.empty()
    beakers_placeholder = st.empty()
    
    def render_initial_state():
        # Render litmus papers
        litmus_placeholder.markdown("""
            <div class='litmus-container'>
                <div class='litmus' style='background-color: #FFFACD; transform: translate(0, 0) rotate(0deg);'></div>
                <div class='litmus' style='background-color: #FFFACD; transform: translate(0, 0) rotate(0deg);'></div>
                <div class='litmus' style='background-color: #FFFACD; transform: translate(0, 0) rotate(0deg);'></div>
            </div>
        """, unsafe_allow_html=True)
        
        # Render beakers with enhanced solution effects
        beakers_placeholder.markdown("""
            <div class='beaker-container'>
                <div>
                    <div class='beaker'>
                        <div class='solution' style='background: linear-gradient(to bottom, rgba(176,224,230,0.7), rgba(135,206,235,0.9));'></div>
                    </div>
                    <div class='beaker-label'>Hydrochloric acid<br>(HCl)</div>
                </div>
                <div>
                    <div class='beaker'>
                        <div class='solution' style='background: linear-gradient(to bottom, rgba(176,224,230,0.7), rgba(135,206,235,0.9));'></div>
                    </div>
                    <div class='beaker-label'>Neutral water<br>(H₂O)</div>
                </div>
                <div>
                    <div class='beaker'>
                        <div class='solution' style='background: linear-gradient(to bottom, rgba(176,224,230,0.7), rgba(135,206,235,0.9));'></div>
                    </div>
                    <div class='beaker-label'>Sodium hydroxide<br>(NaOH)</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    def animate_experiment():
        # Step 1: Move papers to center of beakers with slight rotation
        litmus_placeholder.markdown("""
            <div class='litmus-container'>
                <div class='litmus' style='background-color: #FFFACD; transform: translate(-10px, 90px) rotate(-3deg);'></div>
                <div class='litmus' style='background-color: #FFFACD; transform: translate(0px, 90px) rotate(0deg);'></div>
                <div class='litmus' style='background-color: #FFFACD; transform: translate(10px, 90px) rotate(3deg);'></div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(1.5)
        
        # Step 2: Color change while in solutions with slight movement
        litmus_placeholder.markdown("""
            <div class='litmus-container'>
                <div class='litmus' style='background: linear-gradient(to bottom, #FF6347 60%, #FFFACD); transform: translate(-10px, 90px) rotate(-3deg);'></div>
                <div class='litmus' style='background: linear-gradient(to bottom, #90EE90 60%, #FFFACD); transform: translate(0px, 90px) rotate(0deg);'></div>
                <div class='litmus' style='background: linear-gradient(to bottom, #4682B4 60%, #FFFACD); transform: translate(10px, 90px) rotate(3deg);'></div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(2)
        
        # Step 3: Return to original positions with new colors and slight rotation
        litmus_placeholder.markdown("""
            <div class='litmus-container'>
                <div class='litmus' style='background: linear-gradient(to bottom, #FF6347 90%, #FFFACD); transform: translate(0, 0) rotate(2deg);'></div>
                <div class='litmus' style='background: linear-gradient(to bottom, #90EE90 90%, #FFFACD); transform: translate(0, 0) rotate(-2deg);'></div>
                <div class='litmus' style='background: linear-gradient(to bottom, #4682B4 90%, #FFFACD); transform: translate(0, 0) rotate(1deg);'></div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(2)
        
        # Reset to initial state
        render_initial_state()
    
    # Initial render
    render_initial_state()
    
    # Add start button with light grey styling
    st.markdown("""
        <style>
            .stButton>button {
                background: #d3d3d3;
                color: white;
                font-family: 'Rajdhani', sans-serif;
                font-weight: 600;
                border: none;
                padding: 12px 30px;
                border-radius: 8px;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(211, 211, 211, 0.3);
            }
            .stButton>button:hover {
                background: #c0c0c0;
                transform: translateY(-3px);
                box-shadow: 0 6px 20px rgba(211, 211, 211, 0.4);
            }
            .stButton>button:active {
                transform: translateY(-1px);
            }
        </style>
    """, unsafe_allow_html=True)
    
    if st.button("Start Experiment"):
        animate_experiment()
