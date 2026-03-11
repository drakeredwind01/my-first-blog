
# sudo ./venv/bin/python "/home/drake/Documents/github/my-first-blog/_USB/game/ahk/v_to_click.py"

import time
import threading
import random
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# --- Settings ---
# Time between clicks (12-20 clicks per second)
min_gap, max_gap = 0.05, 0.08 
# Time the button is physically held down
min_hold, max_hold = 0.02, 0.04 

start_stop_key = KeyCode(char='v')
mouse = Controller()
running = False

def human_clicker():
    while True:
        if running:
            mouse.press(Button.left)
            time.sleep(random.uniform(min_hold, max_hold)) # Random hold
            mouse.release(Button.left)
            time.sleep(random.uniform(min_gap, max_gap))   # Random gap
        else:
            time.sleep(0.1)

def on_press(key):
    global running
    if key == start_stop_key:
        running = not running
        print(f"--- Clicking: {running} ---")

# Start thread
threading.Thread(target=human_clicker, daemon=True).start()

print("RUNNING WITH SUDO. Press 'v' to toggle.")
with Listener(on_press=on_press) as listener:
    listener.join()







v
vvvvvvv
v





v



