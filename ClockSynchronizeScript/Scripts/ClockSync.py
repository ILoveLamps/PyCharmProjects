"""
    Moves and clicks mouse pointer to open the date/time menu and sync the clock
    -   Hirdayesh Shrestha
"""

from pynput.mouse import Button, Controller
import time

mouse = Controller()

mouse.position = (1835, 1059)   # # Moving to date/time at bottom right
mouse.click(Button.right, 1)    # # Right click once

mouse.position = (1829, 589)    # # Moving to "Adjust date/time"
mouse.click(Button.left, 1)     # # Left click once
time.sleep(1)                   # # Wait 1 second

mouse.position = (390, 502)     # # Moving to "Sync now" button
mouse.click(Button.left, 1)     # # Left click once
time.sleep(1)                   # # Wait 1 second

mouse.position = (1895, 13)     # # Moving to "x" button at top-right
mouse.click(Button.left, 1)     # # Left click once
