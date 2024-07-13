#!/usr/bin/env python3

import os
import time
import tkinter as tk
from PIL import Image, ImageTk

# Introduce a delay to ensure the desktop environment is fully loaded
time.sleep(1)  # Adjust the delay as needed

# Create the main window
root = tk.Tk()
root.title("Kanga Kickboxer")

# Expand the path to the image
image_path = os.path.expanduser("/usr/local/share/startup_script/images/JHKanga.jpg")

# Load the image file using Pillow
image = Image.open(image_path)

# Convert the image to a PhotoImage object
photo = ImageTk.PhotoImage(image)

# Create a Label widget to display the image
label = tk.Label(root, image=photo)
label.pack()

# Ensure the image reference is maintained
label.image = photo

# Start the Tkinter event loop
root.mainloop()

