import streamlit as st
import time

def run_experiment():
    # Custom CSS for styling and animations
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@600&display=swap');
        .title {
            font-family: 'Rajdhani', sans-serif;
            font-size: 3em;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            background: linear-gradient(45deg, #ff4757, #2ed573, #1e90ff, #ffa502);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradient 3s ease infinite;
        }
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .experiment-container {
            position: relative;
            display: flex;
            justify-content: center;
            height: 400px;
        }
        .beaker {
            width: 120px;
            height: 180px;
            border: 3px solid #555;
            border-radius: 5px 5px 10px 10px;
            background: transparent;
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            overflow: hidden;
        }
        .water {
            width: 100%;
            height: 90px;
            background: rgba(173, 216, 230, 0.6);
            position: absolute;
            bottom: 0;
            animation: wave 2s ease-in-out infinite;
        }
        @keyframes wave {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-5px); }
        }
        .label {
            font-size: 14px;
            font-weight: bold;
            color: #555;
            text-align: center;
            margin-top: 5px;
        }
        .spoon {
            width: 80px;
            height: 20px;
            background: #d3d3d3;
            border-radius: 10px;
            position: absolute;
            left: 50%;
            top: 80px;
            transform-origin: center right;
            transform: translateX(-50%);
            transition: transform 1s;
        }
        .spoon-content {
            font-size: 14px;
            color: #fff;
            position: absolute;
            right: -30px;
            top: -10px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .pouring {
            transform: translateX(-50%) rotate(-45deg);
        }
        .sodium-piece {
            width: 5px;
            height: 5px;
            background-color: #333;
            border-radius: 50%;
            position: absolute;
            opacity: 0;
            left: 50%;
        }
        @keyframes fall {
            0% {
                transform: translate(-50%, 0);
                opacity: 1;
            }
            100% {
                transform: translate(var(--final-x), 150px);
                opacity: 0;
            }
        }
        .reaction {
            width: 100%;
            height: 0;
            background: linear-gradient(to top, #ff4757, #ff8c42);
            position: absolute;
            bottom: 0;
            animation: explosion 2s ease forwards;
        }
        @keyframes explosion {
            0% { height: 0; opacity: 0; }
            50% { height: 180px; opacity: 1; }
            100% { height: 180px; opacity: 0; }
        }
        .boom-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(0);
            font-size: 48px;
            font-weight: bold;
            color: #ff4757;
            animation: boom 1s ease-out forwards;
            animation-delay: 1s;
        }
        @keyframes boom {
            0% { transform: translate(-50%, -50%) scale(0); }
            50% { transform: translate(-50%, -50%) scale(1.5); }
            100% { transform: translate(-50%, -50%) scale(1); }
        }
        .spark {
            position: absolute;
            width: 4px;
            height: 4px;
            background: #ff4757;
            border-radius: 50%;
        }
        @keyframes spark {
            0% { transform: translate(0, 0); opacity: 1; }
            100% { transform: translate(var(--tx), var(--ty)); opacity: 0; }
        }
        .ripple {
            position: absolute;
            width: 20px;
            height: 20px;
            border: 2px solid #fff;
            border-radius: 50%;
            bottom: 90px;
            left: 50%;
            transform: translate(-50%, 0) scale(0);
            opacity: 0.7;
            animation: ripple 0.6s ease-out forwards;
        }
        @keyframes ripple {
            0% { transform: translate(-50%, 0) scale(0); opacity: 0.7; }
            100% { transform: translate(-50%, 0) scale(2); opacity: 0; }
        }
    </style>
    """, unsafe_allow_html=True)

    # Display the title
    st.markdown("<h1 class='title'>Sodium And Water Reaction</h1>", unsafe_allow_html=True)

    # Container for the experiment setup
    container = st.empty()

    def render_initial_state():
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="water"></div>
                    <div class="label">H₂O</div>
                </div>
                <div class="spoon">
                    <div class="spoon-content">Na</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    def animate_experiment():
        # Step 1: Animate the spoon bending and show falling sodium pieces
        sodium_pieces = "".join([
            f'<div class="sodium-piece" style="--final-x: {-10 + i * 5}px; top: {110 + i * 2}px; animation: fall 1s ease-in-out {i * 0.1}s forwards;"></div>'
            for i in range(20)
        ])
        
        sparks = "".join([
            f'<div class="spark" style="--tx: {-20 + i * 10}px; --ty: {-30 + i * 5}px; animation: spark 0.5s ease-out {i * 0.1}s forwards;"></div>'
            for i in range(15)
        ])
        
        ripples = "".join([
            f'<div class="ripple" style="animation-delay: {i * 0.1}s;"></div>'
            for i in range(10)
        ])

        container.markdown(f"""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="water"></div>
                    <div class="label">H₂O</div>
                    {ripples}
                </div>
                <div class="spoon pouring">
                    <div class="spoon-content">Na</div>
                </div>
                {sodium_pieces}
                {sparks}
            </div>
        """, unsafe_allow_html=True)
        time.sleep(1.5)

        # Step 2: Show the dramatic reaction with fire effect and boom text
        container.markdown("""
            <div class="experiment-container">
                <div class="beaker">
                    <div class="water"></div>
                    <div class="reaction"></div>
                    <div class="boom-text">BOOM!</div>
                    <div class="label">H₂O</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Initial render
    render_initial_state()

    # Button to start the experiment
    if st.button("Start Experiment"):
        animate_experiment()
        # Display the chemical equation
        st.markdown("""
            **Chemical Equation:**
            2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)
        """)

if __name__ == "__main__":
    run_experiment()
