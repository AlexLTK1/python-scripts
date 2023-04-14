import time
import pyautogui
import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("Game Automation")

        # Load the delay from a file or use default value
        try:
            with open("delay.txt", "r") as f:
                delay = float(f.read())
        except FileNotFoundError:
            delay = 2.5

        # Load the click position from a file or use default value
        try:
            with open("position.txt", "r") as f:
                position = tuple(map(int, f.read().split(',')))
        except FileNotFoundError:
            position = (500, 500)

        self.delay_label = tk.Label(master, text="Delay:")
        self.delay_label.grid(row=0, column=0)

        self.delay_entry = tk.Entry(master, width=10)
        self.delay_entry.insert(0, delay)
        self.delay_entry.grid(row=0, column=1)

        self.position_label = tk.Label(master, text="Position (x,y):")
        self.position_label.grid(row=0, column=2)

        self.position_entry = tk.Entry(master, width=20)
        self.position_entry.insert(0, position)
        self.position_entry.grid(row=0, column=3)

        self.save_button = tk.Button(master, text="Save", command=self.save)
        self.save_button.grid(row=0, column=4)

        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.grid(row=0, column=5)

        self.quit_button = tk.Button(master, text="Quit", command=self.quit_script)
        self.quit_button.grid(row=0, column=6)

    def save(self):
        delay = float(self.delay_entry.get())
        position = tuple(map(int, self.position_entry.get().split(',')))

        with open("delay.txt", "w") as f:
            f.write(str(delay))

        with open("position.txt", "w") as f:
            f.write("{},{}".format(position[0], position[1]))

    def start(self):
        # Load the delay from a file or use default value
        try:
            with open("delay.txt", "r") as f:
                delay = float(f.read())
        except FileNotFoundError:
            delay = 2.5

        # Load the click position from a file or use default value
        try:
            with open("position.txt", "r") as f:
                position = tuple(map(int, f.read().split(',')))
        except FileNotFoundError:
            position = (500, 500)

        # Click at the specified position
        pyautogui.click(position)

        # Wait for the specified delay
        time.sleep(delay)

        # Click again at the same position
        pyautogui.click(position)

    def quit_script(self):
        self.save()
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()