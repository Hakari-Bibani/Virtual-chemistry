import streamlit as st
import importlib
from pathlib import Path

# Configure page settings
st.set_page_config(
    page_title="Virtual Chemistry Lab",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Chemistry experiments data
experiments = {
    "Baking Soda and Vinegar Reaction": {
        "module": "baking"
    },
    "Sodium and Water Reaction": {
        "module": "explosion"
    },
    "pH Indicator": {
        "module": "indicator"
    },
    "Acid-Base Titration": {
        "module": "acid_base"
    },
    "Elephant Toothpaste Reaction": {
        "module": "elephant_toothpaste"
    }
}

# Custom CSS for the flip card styling and title animations
def load_css():
    css = """
    # [Previous CSS code remains unchanged]
    """
    st.markdown(css, unsafe_allow_html=True)

def render_card(title, content):
    # [Previous render_card function remains unchanged]
    pass

def load_module(module_name):
    """Dynamically import and return the specified module"""
    try:
        return importlib.import_module(module_name)
    except ImportError as e:
        st.error(f"Error loading module {module_name}: {str(e)}")
        return None

def main():
    load_css()
    
    # Sidebar navigation
    with st.sidebar:
        st.title("🧪 Experiments")
        for experiment in experiments:
            if st.button(experiment):
                render_experiment(experiments[experiment]["module"])
                break

    # Title container with animations and icons
    st.markdown("""
        <div class='title-container'>
            # [Previous title container code remains unchanged]
        </div>
    """, unsafe_allow_html=True)

def render_experiment(module_name):
    module = load_module(module_name)
    
    if module and hasattr(module, 'run_experiment'):
        module.run_experiment()
    else:
        st.warning(f"The experiment module '{module_name}' is not properly configured.")

if __name__ == "__main__":
    main()
