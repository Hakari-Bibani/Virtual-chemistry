import streamlit as st
from acid_base import run_acid_base
from elephant_toothpaste import run_elephant_toothpaste
from indicator import run_indicator
from explosion import run_explosion
from baking import run_baking

# Configure page settings
st.set_page_config(
    page_title="Virtual Chemistry Lab",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for the title and flip card styling
def load_css():
    css = """
    /* Existing CSS styling here */
    """
    st.markdown(css, unsafe_allow_html=True)

# Main application
def main():
    load_css()
    
    # Title container with animations and icons
    st.markdown("""
        <div class='title-container'>
            <h1 class='glowing-title'>Virtual Chemistry Lab</h1>
            <div class='icons-container'>
                <span class='chemistry-icon'>⚗️</span>
                <span class='chemistry-icon'>🧪</span>
                <span class='chemistry-icon'>🔬</span>
                <span class='chemistry-icon'>🧫</span>
                <span class='chemistry-icon'>⚛️</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Tabs for each experiment
    tabs = st.tabs(["Acid-Base Titration", "Elephant Toothpaste", "pH Indicator", "Sodium and Water", "Baking Soda & Vinegar"])
    
    with tabs[0]:
        run_acid_base()  # Calls function from acid_base.py

    with tabs[1]:
        run_elephant_toothpaste()  # Calls function from elephant_toothpaste.py

    with tabs[2]:
        run_indicator()  # Calls function from indicator.py

    with tabs[3]:
        run_explosion()  # Calls function from explosion.py

    with tabs[4]:
        run_baking()  # Calls function from baking.py

    # Footer
    st.markdown("""
        <div style='text-align: center; padding: 20px;'>
            Created by <a href="https://github.com/Hakari-Bibani" target="_blank">Hakari Bibani</a> | 
            <a href="https://hawkardemo.streamlit.app/" target="_blank">Visit Demo Site</a>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
