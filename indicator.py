import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Define solution colors (BGR format)
neutral_color = (112, 112, 112)  # Light grey
acidic_color = (0, 0, 255)  # Red
basic_color = (255, 0, 0)  # Blue

# Define image paths
beaker_path = "beaker.png"
litmus_path = "litmus_black.png"

# Load images
beaker_img = cv2.imread(beaker_path, cv2.IMREAD_UNCHANGED)
litmus_img = cv2.imread(litmus_path, cv2.IMREAD_UNCHANGED)

# Define solution regions in the beaker image
acidic_region = [(100, 100), (200, 200)]  # Replace with actual coordinates in your image
basic_region = [(300, 100), (400, 200)]  # Replace with actual coordinates in your image
neutral_region = [(0, 0), (beaker_img.shape[1], beaker_img.shape[0])]  # Full beaker

# Function to check which solution region the litmus is dropped on
def get_solution(x, y):
  if acidic_region[0][0] < x < acidic_region[1][0] and acidic_region[0][1] < y < acidic_region[1][1]:
    return "acidic"
  elif basic_region[0][0] < x < basic_region[1][0] and basic_region[0][1] < y < basic_region[1][1]:
    return "basic"
  else:
    return "neutral"

# Function to animate litmus dipping
def dip_litmus(beaker, litmus, duration=0.5):
  frames = []
  for i in range(int(duration * 30)):
    dy = (litmus.shape[0] - 50) * i / (duration * 30)
    mask = cv2.bitwise_not(litmus[:, :, 3:])  # Extract alpha channel
    result = cv2.seamlessClone(litmus[:, :, :3], beaker, mask, (beaker.shape[1] // 2, beaker.shape[0] - 50 + dy), cv2.NORMAL_CLONE)
    frames.append(result)
  return frames

# Function to change litmus color
def change_color(litmus, color, duration=5):
  frames = []
  for i in range(duration * 30):
    alpha = i / (duration * 30)
    new_color = cv2.addWeighted(litmus[:, :, :3], 1 - alpha, np.full((litmus.shape[0], litmus.shape[1], 3), color, dtype=np.uint8), alpha, 0)
    result = cv2.cvtColor(new_color, cv2.COLOR_BGR2BGRA)
    result[:, :, 3] = litmus[:, :, 3]  # Preserve alpha channel
    frames.append(result)
  return frames

# Function to display the simulation
def display_simulation():
  state = st.empty()
  litmus_pos = (state.width // 2, 50)
  solution = None
  color_change_frames = None

  def on_drag(key, delta):
    nonlocal litmus_pos
    litmus_pos = (max(0, min(state.width - litmus_img.shape[1], litmus_pos[0] + delta[0])), litmus_pos[1])
    solution = get_solution(litmus_pos[0], litmus_pos[1])
    state.empty()

  litmus_img_with_alpha = cv2.cvtColor(litmus_img, cv2.COLOR_BGR
