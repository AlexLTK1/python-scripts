import time
import pyautogui
import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("Automation Tool")

        self.delay_label = tk.Label(master, text="Delay (seconds):")
        self.delay_label.grid(row=0, column=0)

        self.delay_entry = tk.Entry(master)
        self.delay_entry.insert(0, "2.5")
        self.delay_entry.grid(row=0, column=1)

        self.save_button = tk.Button(master, text="Save", command=self.save_delay)
        self.save_button.grid(row=1, column=0)

    def save_delay(self):
        delay = float(self.delay_entry.get())

        # Save the delay to a file
        with open("delay.txt", "w") as f:
            f.write(str(delay))

        self.master.destroy()

if __name__ == '__main__':
    # Load the delay from a file
    with open("delay.txt", "r") as f:
        delay = float(f.read())

    # Create the GUI
    root = tk.Tk()
    app = App(root)
    root.mainloop()

    # Delay before starting the automation
    time.sleep(delay)

    # Loop to automate the task
    for i in range(10):
        # Move the mouse to the desired location and click
        pyautogui.moveTo(100, 200, duration=0.5)
        pyautogui.click()

        # Type a message
        pyautogui.typewrite("Hello World!")

        # Press the Enter key
        pyautogui.press('enter')

        # Wait for the specified delay before repeating
        time.sleep(delay)