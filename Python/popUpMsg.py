from tkinter import *
from PIL import Image, ImageTk

def message(title, message, image_path):
    dialog = Toplevel()
    dialog.title(title)
    
    my_img = ImageTk.PhotoImage(Image.open(image_path))
    Label(dialog, image=my_img).pack()
    
    Label(dialog, text=message, wraplength=300, justify="center").pack()

    Button(dialog, text="OK", command=dialog.destroy).pack(pady=10)

    dialog.grab_set()
    dialog.focus_set()
    dialog.wait_window()

if __name__ == '__main__':
    root = Tk()
    root.withdraw()

    message("STRAIN ALERT", "Try this stretch to relax your muscles", "image.png")

    root.destroy()