"""
    Moves and clicks mouse pointer to open the date/time menu and sync the clock
    -   Hirdayesh Shrestha
"""

from pynput.mouse import Button, Controller
import time

mouse = Controller()

mouse.position = (1835, 1059)   # # Moving to date/time at bottom right
time.sleep(0.1)                 # # Wait
mouse.click(Button.right, 1)    # # Right click once

mouse.position = (1655, 590)    # # Moving to "Adjust date/time"
time.sleep(0.1)                 # # Wait
mouse.click(Button.left, 1)     # # Left click once

mouse.position = (390, 502)     # # Moving to "Sync now" button
time.sleep(1)                   # # Wait
mouse.click(Button.left, 1)     # # Left click once
time.sleep(1)                   # # Wait

mouse.position = (1895, 13)     # # Moving to "x" button at top-right
time.sleep(0.1)                 # # Wait
mouse.click(Button.left, 1)     # # Left click once
