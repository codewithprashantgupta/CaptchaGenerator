from tkinter import *
from tkinter import ttk
from captcha.image import ImageCaptcha
from tkcolorpicker import askcolor
import os
import random
from PIL import Image, ImageTk

def generate_random_text():
    text_length = random.randint(4, 7)
    text = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=text_length))
    return text

def generate_random_color():
    return '#{:06x}'.format(random.randint(0, 0xFFFFFF))  # Generate random hex color code

def generate_captcha():
    text = generate_random_text()
    selected_font = font_combobox.get()  # Get selected font name from Combobox
    font_path = font_mapping[selected_font]
    font_color = generate_random_color()
    background_color = generate_random_color()
    filename = entry_filename.get()

    captcha = ImageCaptcha(fonts=[font_path])
    image = captcha.create_captcha_image(text, background_color, font_color)

    # Apply distortion effect with reduced rotation angle range
    image = apply_distortion(image)

    # Convert PIL image to Tkinter PhotoImage and display in label
    image_tk = ImageTk.PhotoImage(image)
    captcha_label.config(image=image_tk)
    captcha_label.image = image_tk

    # Save the captcha image to a local folder
    output_folder = "Outputs"
    os.makedirs(output_folder, exist_ok=True)
    image_path = os.path.join(output_folder, f"{filename}.png")
    image.save(image_path)

def apply_distortion(image):
    rotation_angle = random.uniform(-5, 5)  # Reduced rotation angle range
    distorted_image = image.rotate(rotation_angle, resample=Image.BILINEAR, expand=True)
    return distorted_image

# Create Tkinter window
window = Tk()
window.title("Captcha Generator")

# Frame for input fields
input_frame = Frame(window)
input_frame.pack(pady=10, padx=10)

# Font selection dropdown
Label(input_frame, text="Font:").grid(row=0, column=0, padx=10, pady=5)
available_fonts = [font for font in os.listdir("C:/Windows/Fonts") if font.endswith('.ttf')]
font_mapping = {os.path.splitext(font)[0]: os.path.join("C:/Windows/Fonts", font) for font in available_fonts}
font_combobox = ttk.Combobox(input_frame, values=list(font_mapping.keys()), width=30)
font_combobox.grid(row=0, column=1, padx=10, pady=5)

# Filename input
Label(input_frame, text="Filename:").grid(row=1, column=0, padx=10, pady=5)
entry_filename = Entry(input_frame, width=30)
entry_filename.grid(row=1, column=1, padx=10, pady=5)

# Generate button
generate_button = Button(input_frame, text="Generate Captcha", command=generate_captcha, width=30)
generate_button.grid(row=2, columnspan=2, pady=10)

# Frame for captcha display
captcha_frame = Frame(window)
captcha_frame.pack(pady=10, padx=10)

# Captcha display label
captcha_label = Label(captcha_frame)
captcha_label.pack()

# Run the Tkinter event loop
window.mainloop()
