# Captcha Generator
This is a simple graphical user interface (GUI) application built in Python using the Tkinter library to generate captcha images with random text, fonts, colors, and distortions.

## Features
- **Random Text Generation:** Generates random text of varying lengths (between 4 to 7 characters) for the captcha.
- **Font Selection:** Allows users to choose from available fonts installed on their system.
- **Custom Filename:** Enables users to input a custom filename for the generated captcha image.
- **Distortion Effects:** Applies distortion effects to the captcha images for added security.
- **Save Functionality:** Saves the generated captcha images in a local "Outputs" folder.

## Dependencies
- Python 3.x
- PIL (Python Imaging Library)
- Tkinter
- tkcolorpicker

## Installation
1. Clone the repository:
```git clone https://github.com/your_username/CaptchaGenerator.git```
2. Install the dependencies:
   ```pip install -r requirements.txt```
3. Run the application:
   ```python CaptchaGenerator2.py```

## Usage
1. Select a font from the dropdown menu.
2. Enter a filename for the captcha image.
3. Click the "Generate Captcha" button to create a captcha image.
4. The generated captcha will be displayed in the GUI window.
5. The image will be saved in the "Outputs" folder in the same directory.

## Contributions

**Georgia Croci** - Worked on ***generate_random_text*** method which generates a random text string with a length between 4 and 7 characters <br>
**Ishaan Chaudhari** - Worked on ***generate_random_color*** function which generates a random hexadecimal color code. <br>
**Lloyd Dsouza** - Applied distortion by rotating it with a random rotation angle.<br>
**Prashant Gupta** - Created ***generate_captcha*** method to generate base captcha file. <br>

## License
This project is licensed under the MIT License.
