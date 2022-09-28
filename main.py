import pyautogui
import random
import time

print("Passive Aggressive Bot is currently running. Press Ctrl+C to cancel.")

while True:
    try:
        pyautogui.press('capslock')
        time.sleep(random.uniform(0.2, 0.3))
    except KeyboardInterrupt:
        print("Passive Aggressive Bot stopped.")
        exit()

