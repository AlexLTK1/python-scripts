import time
import pyautogui
import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("Auto Clicker")

        # Create the widgets
        self.delay_label = tk.Label(master, text="Delay (in seconds): ")
        self.delay_entry = tk.Entry(master, width=5)
        self.delay_entry.insert(tk.END, "0.5")

        self.record_button = tk.Button(master, text="Record Click Position", command=self.record_click_position)
        self.start_button = tk.Button(master, text="Start", command=self.start_clicking)
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_clicking)
        self.quit_button = tk.Button(master, text="Quit", command=self.quit_script)

        # Layout the widgets
        self.delay_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.delay_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.record_button.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.start_button.grid(row=2, column=0, padx=5, pady=5)
        self.stop_button.grid(row=2, column=1, padx=5, pady=5)
        self.quit_button.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

        # Initialize the click position to None
        self.click_position = None

    def record_click_position(self):
        self.master.withdraw()  # Hide the GUI while recording the click position
        self.click_position = pyautogui.position()
        self.master.deiconify()  # Show the GUI again

    def start_clicking(self):
        # Load the delay from a file or use the default value
        try:
            with open("delay.txt", "r") as f:
                delay = float(f.read())
        except FileNotFoundError:
            delay = 0.5

        # Save the delay to a file
        with open("delay.txt", "w") as f:
            f.write(str(delay))

        if self.click_position is not None:
            # Start clicking at the recorded click position
            while True:
                pyautogui.click(self.click_position)
                time.sleep(delay)
        else:
            # If no click position has been recorded, show an error message
            tk.messagebox.showerror("Error", "No click position has been recorded!")

    def stop_clicking(self):
        # Stop clicking by breaking out of the while loop in the start_clicking method
        pass

    def quit_script(self):
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()