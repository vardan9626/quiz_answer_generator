import tkinter as tk
from tkinter import font

def create_custom_popup(text):
    def close_popup():
        popup.destroy()
        rt.quit()

    # Create the popup window
    popup = tk.Toplevel(rt)
    popup.configure(bg='white')
    popup.overrideredirect(True)  # Removes the title bar

    # Add a label
    label = tk.Label(popup, text=text, bg='white', wraplength=290)
    label.pack(padx=15, pady=12)

    # Create a close button (X) with a smaller font size
    small_font = font.Font(size=6)  # Set a smaller font size
    close_button = tk.Button(popup, text="x", bg='red', fg='white', command=close_popup, font=small_font, highlightthickness=0, bd=0)
    close_button.place(relx=1.0, rely=0.0, anchor='ne')

    # Update the popup to adjust to its contents
    popup.update_idletasks()
    width = popup.winfo_reqwidth()
    height = popup.winfo_reqheight()

    # Position the popup in the center of the screen
    screen_width = rt.winfo_screenwidth()
    screen_height = rt.winfo_screenheight()
    x = (screen_width - width)
    y = (screen_height - height) 
    popup.geometry(f'{width}x{height}+{x}+{y}')

    return popup

def popup_answer():
    try:
        answer = ''
        with open("output.txt", 'r') as f:
            answer = f.read()
        answer = answer.strip()[10:-1]
        popup_window = create_custom_popup(answer)
        rt.mainloop()
    except:
        print("Error opening file")

# Main window (usually hidden)
rt = tk.Tk()
rt.withdraw()

if __name__ == "__main__":
    # Create and show the popup
    popup_answer()
