import time
import pyautogui
import pytesseract
import tkinter as tk
from tkinter import filedialog

# Set up Tesseract to recognize Chinese characters
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
def tesseract_ocr(image):
    # Try using Simplified Chinese language data
    text = pytesseract.image_to_string(image, lang='chi_sim')
    if text:
        return text
    
    # If that doesn't work, try using Traditional Chinese language data
    return pytesseract.image_to_string(image, lang='chi_tra')

def start_capture(duration):
    # List of names to search for (including Chinese names)
    names_to_search = ["张三", "李四", "王五", "赵六", "陳小明", "林美玲", "王大明", "黃小芳"]

    # Start the screen capture
    start_time = time.time()
    end_time = start_time + duration

    # Set up a dictionary to keep track of which names were found
    names_found = {}
    for name in names_to_search:
        names_found[name] = False

    while time.time() < end_time:
        # Capture the screen
        screenshot = pyautogui.screenshot()

        # Convert the screenshot to grayscale
        grayscale_image = screenshot.convert('L')

        # Use Tesseract to perform OCR on the image
        recognized_text = tesseract_ocr(grayscale_image)

        # Check if any of the names appear in the recognized text
        for name in names_to_search:
            if name in recognized_text:
                names_found[name] = True

    # End of screen capture
    print("Screen capture complete")

    # Print the list of names that were found
    names_found_list = [name for name, found in names_found.items() if found]
    print("Names found:", names_found_list)

    # Print the list of names that were not found
    names_not_found_list = [name for name, found in names_found.items() if not found]
    print("Names not found:", names_not_found_list)

def select_file():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Executable files","*.exe"),("all files","*.*")))
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)

def start_button_click():
    duration = int(duration_entry.get())
    start_capture(duration)

# Create the main window
window = tk.Tk()
window.title("Screen Capture")

# Add a label for the duration
duration_label = tk.Label(window, text="Capture duration (seconds):")
duration_label.pack()

# Add an entry box for the duration
duration_entry = tk.Entry(window)
duration_entry.pack()

# Add a label for the file
file_label = tk.Label(window, text="Executable file:")
file_label.pack()

# Add an entry box for the file
file_entry = tk.Entry(window)
file_entry.pack()

# Add a button to select the executable file
select_file_button = tk.Button(window, text="Select file", command=select_file)
select_file_button.pack()

# Add a button to start the screen capture
start_button = tk.Button(window, text="Start", command=start_button_click)
start_button.pack()

# Start the main loop
window.mainloop()
