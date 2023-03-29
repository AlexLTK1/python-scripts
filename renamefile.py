import os

folder_path = "/path/to/folder" # Change this to the path of your folder

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"): # Change this to the extension of the files you want to rename
        new_filename = filename.replace("old_text", "new_text") # Change "old_text" and "new_text" to the text you want to replace and the new text
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
