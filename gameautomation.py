import time
import pyautogui

# Delay before starting the automation
time.sleep(5)

# Loop to automate the task
for i in range(10):
    # Move the mouse to the desired location and click
    pyautogui.moveTo(100, 200, duration=0.5)
    pyautogui.click()

    # Type a message
    pyautogui.typewrite("Hello World!")

    # Press the Enter key
    pyautogui.press('enter')

    # Wait for a few seconds before repeating
    time.sleep(2)