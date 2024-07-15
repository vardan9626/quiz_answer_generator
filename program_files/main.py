import tkinter as tk
from PIL import Image, ImageTk
import os

interrupted = False

def on_icon_click(event=None):
    os.system("bash script")

def check_interrupt():
    global interrupted
    if interrupted:
        root.destroy()  # Close the Tkinter window
    else:
        root.after(100, check_interrupt)  # Check again after 100ms

# Setup the root window
root = tk.Tk()
root.attributes('-topmost', True)  # Keep the window on top
root.overrideredirect(True)  # Remove border and title bar

# Position of the icon (you can adjust the coordinates)
root.geometry("+960+1000")

# Load your icon image
img = Image.open("../icon/icon.png")  # Replace with your icon path

# Resize the image (e.g., 50x50 pixels)
resized_img = img.resize((50, 50))
photo = ImageTk.PhotoImage(resized_img)

# Create a label with your resized image
label = tk.Label(root, image=photo, cursor="hand2")
label.pack()

# Bind click event
label.bind("<Button-1>", on_icon_click)

# Set transparency
root.attributes("-alpha", 0.5)

root.lift()

try:
    root.after(100, check_interrupt)
    root.mainloop()
except KeyboardInterrupt:
    interrupted = True
