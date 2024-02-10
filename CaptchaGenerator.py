from tkinter import *
from tkinter import ttk
from captcha.image import ImageCaptcha
from tkcolorpicker import askcolor
import os
from PIL import ImageTk

def generate_captcha():
    text = entry_text.get()
    selected_font = font_combobox.get()  # Get selected font name from Combobox
    font_path = font_mapping[selected_font]
    font_color = entry_font_color.get()
    background_color = entry_background_color.get()

    captcha = ImageCaptcha(fonts=[font_path])
    image = captcha.create_captcha_image(text, background_color, font_color)

    # Convert PIL image to Tkinter PhotoImage and display in label
    image_tk = ImageTk.PhotoImage(image)
    captcha_label.config(image=image_tk)
    captcha_label.image = image_tk

    # Save the captcha image to a local folder
    image.save(f"{text}.png")  # Save with text as filename

def select_font_color():
    font_color = askcolor(title="Select Font Color")
    entry_font_color.delete(0, END)
    entry_font_color.insert(0, font_color[1])  # Set font color hex value

def select_background_color():
    background_color = askcolor(title="Select Background Color")
    entry_background_color.delete(0, END)
    entry_background_color.insert(0, background_color[1])  # Set background color hex value

# Create Tkinter window
window = Tk()
window.title("Captcha Generator")

# Text input
Label(window, text="Text:").grid(row=0, column=0)
entry_text = Entry(window)
entry_text.grid(row=0, column=1)

# Font selection dropdown
Label(window, text="Font:").grid(row=1, column=0)
available_fonts = [font for font in os.listdir("C:/Windows/Fonts") if font.endswith('.ttf')]
font_mapping = {os.path.splitext(font)[0]: os.path.join("C:/Windows/Fonts", font) for font in available_fonts}
font_combobox = ttk.Combobox(window, values=list(font_mapping.keys()))
font_combobox.grid(row=1, column=1)

# Font color input with color picker button
Label(window, text="Font Color:").grid(row=2, column=0)
entry_font_color = Entry(window)
entry_font_color.grid(row=2, column=1)
Button(window, text="Select Color", command=select_font_color).grid(row=2, column=2)

# Background color input with color picker button
Label(window, text="Background Color:").grid(row=3, column=0)
entry_background_color = Entry(window)
entry_background_color.grid(row=3, column=1)
Button(window, text="Select Color", command=select_background_color).grid(row=3, column=2)

# Generate button
Button(window, text="Generate Captcha", command=generate_captcha).grid(row=4, columnspan=3)

# Captcha display label
captcha_label = Label(window)
captcha_label.grid(row=5, columnspan=3)

# Run the Tkinter event loop
window.mainloop()
