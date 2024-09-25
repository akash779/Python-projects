This Python script generates QR codes for a given URL. It allows you to create multiple QR codes with different color combinations for customization.

Features

Generates QR codes for any valid URL.
Creates multiple versions with distinct color schemes.
Saves the generated QR codes as PNG images.
Instructions

Prerequisites:

Python 3.x
qrcode library (install using pip install qrcode)
Pillow (PIL) library (install using pip install Pillow)
Usage:

Open a terminal or command prompt and navigate to the directory containing this script (e.g., cd path/to/script).
Run the script using: python qr_code_generator.py (replace qr_code_generator.py with the actual script filename).
Generated Files:

The script creates three PNG image files named temp_QR.png, temp_QR1.png, and temp_QR2.png. These files contain the QR codes with different color combinations.
Color Combinations:
temp_QR.png: Black foreground (fill color) on white background.
temp_QR1.png: Red foreground on white background.
temp_QR2.png: Red foreground on blue background.
Customization

You can modify the script to generate QR codes for different URLs.
Change the color combinations within the script (lines 8-10) to suit your preferences.