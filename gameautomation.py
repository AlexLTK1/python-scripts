import time
import pyautogui
import tkinter as tk
import os

class App:
    def __init__(self, master):
        self.master = master
        self.delay = 5.0
        master.title("Game Automation")
        tk.Label(master, text="Delay (in seconds):").grid(row=0, column=0)
        self.delay_entry = tk.Entry(master)
        self.delay_entry.grid(row=0, column=1)
        self.delay_entry.insert(0, str(self.delay))
        tk.Button(master, text="Save", command=self.save_delay).grid(row=1, column=1)
        tk.Button(master, text="Start", command=self.start_automation).grid(row=2, column=0)
        tk.Button(master, text="Stop", command=self.stop_automation).grid(row=2, column=1)
        tk.Button(master, text="Quit", command=self.quit).grid(row=2, column=2)

    def start_automation(self):
        self.is_running = True
        while self.is_running:
            pyautogui.click(pyautogui.position())
            time.sleep(self.delay)

    def stop_automation(self):
        self.is_running = False

    def save_delay(self):
        self.delay = float(self.delay_entry.get())
        with open("delay.txt", "w") as f:
            f.write(str(self.delay))

    def quit(self):
        # Save the delay to a file
        with open("delay.txt", "w") as f:
            f.write(str(self.delay))
        self.master.destroy()

if __name__ == '__main__':
    # Load the delay from a file
    if os.path.exists("delay.txt"):
        with open("delay.txt", "r") as f:
            delay = float(f.read())
    else:
        delay = 5.0
        with open("delay.txt", "w") as f:
            f.write(str(delay))

    # Create the GUI
    root = tk.Tk()
    app = App(root)
    root.mainloop()