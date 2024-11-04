import streamlit as st
import numpy as np
from scipy.spatial.transform import Rotation as R
import time

# Set up the page config
st.set_page_config(page_title="pH Indicator Experiment", layout="centered")

# Define the dimensions of the beakers and litmus paper
BEAKER_WIDTH = 150
BEAKER_HEIGHT = 200
LITMUS_WIDTH = 50
LITMUS_HEIGHT = 150

# Define the positions of the beakers
BEAKER_POSITIONS = [
    (100, 400),
    (300, 400),
    (500, 400)
]

# Define the solution colors
ACID_COLOR = (255, 0, 0)
BASE_COLOR = (0, 0, 255)
NEUTRAL_COLOR = (0, 255, 0)

# Define the litmus paper color changes
LITMUS_COLORS = {
    "acid": (255, 0, 0),
    "base": (0, 0, 255),
    "neutral": (0, 255, 0)
}

# Define the duration of the color change
COLOR_CHANGE_DURATION = 5  # in seconds

class LitmusPaper:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.color = (0, 0, 0)  # Black
        self.solution_type = None
        self.is_dropped = False
        self.drop_start_time = None
        self.drop_duration = 1  # in seconds
        self.color_change_start_time = None

    def draw(self):
        if self.is_dropped:
            if time.time() - self.drop_start_time < self.drop_duration:
                # Animate the litmus paper dropping into the beaker
                t = (time.time() - self.drop_start_time) / self.drop_duration
                self.y = BEAKER_POSITIONS[self.solution_type][1] + BEAKER_HEIGHT // 2 - LITMUS_HEIGHT * (1 - t)
            else:
                # Litmus paper is fully dropped, start color change
                self.color = LITMUS_COLORS[self.solution_type]
                self.color_change_start_time = time.time()

            if self.color_change_start_time and time.time() - self.color_change_start_time > COLOR_CHANGE_DURATION:
                # Reset the litmus paper color
                self.color = (0, 0, 0)
                self.solution_type = None
                self.is_dropped = False

        st.image(
            self.get_litmus_paper_image(),
            width=LITMUS_WIDTH,
            height=LITMUS_HEIGHT,
            rot=self.angle,
            output_format="PNG"
        )

    def get_litmus_paper_image(self):
        # Generate a litmus paper image with the current color
        image = np.zeros((LITMUS_HEIGHT, LITMUS_WIDTH, 3), dtype=np.uint8)
        image[:, :] = self.color
        return image

    def handle_drop(self, solution_type):
        self.is_dropped = True
        self.solution_type = solution_type
        self.drop_start_time = time.time()

def render_beakers():
    for i, position in enumerate(BEAKER_POSITIONS):
        x, y = position
        # Draw the beaker
        st.image(
            get_beaker_image(i),
            width=BEAKER_WIDTH,
            height=BEAKER_HEIGHT,
            output_format="PNG"
        )
        # Draw the solution
        st.image(
            get_solution_image(i),
            width=BEAKER_WIDTH,
            height=BEAKER_HEIGHT // 2,
            output_format="PNG"
        )

def get_beaker_image(index):
    # Generate a beaker image
    image = np.zeros((BEAKER_HEIGHT, BEAKER_WIDTH, 3), dtype=np.uint8)
    image[:, :] = (192, 192, 192)  # Light grey
    return image

def get_solution_image(index):
    # Generate a solution image
    image = np.zeros((BEAKER_HEIGHT // 2, BEAKER_WIDTH, 3), dtype=np.uint8)
    if index == 0:
        image[:, :] = ACID_COLOR  # Acid (HCl)
    elif index == 1:
        image[:, :] = BASE_COLOR  # Base (NaOH)
    else:
        image[:, :] = NEUTRAL_COLOR  # Neutral (H2O)
    return image

def main():
    # Create the litmus paper
    litmus_paper = LitmusPaper(x=100, y=100)

    # Render the beakers
    render_beakers()

    # Allow the user to drag and drop the litmus paper
    if st.drag_data:
        litmus_paper.x = st.drag_data["x"]
        litmus_paper.y = st.drag_data["y"]

        # Check if the litmus paper is dropped into a beaker
        for i, position in enumerate(BEAKER_POSITIONS):
            x, y = position
            if (
                x - BEAKER_WIDTH // 2 <= litmus_paper.x <= x + BEAKER_WIDTH // 2
                and y - BEAKER_HEIGHT // 2 <= litmus_paper.y <= y + BEAKER_HEIGHT // 2
            ):
                litmus_paper.handle_drop(i)
                break

    # Render the litmus paper
    litmus_paper.draw()

if __name__ == "__main__":
    main()
