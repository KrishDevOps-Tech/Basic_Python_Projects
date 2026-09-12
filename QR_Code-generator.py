# QR Code Generator

import os 
import qrcode
from PIL import Image

# 1. Text ya Link Input
def generate_qrcode():
    # for pasting the URL or Link.
    data = input("Enter the URL or Link to generate QR Code: ").strip()
    while not data:
        print("Error! Please enter a valid URL or Link.")
        data = input("Enter the URL or Link to generate QR Code: ").strip()

    # 2. File Name Input
    filename =( input("Enter the file name to save the QR Code (without extension): ").strip() or "my_qrcode"
               )
    output_path = f"{filename}.png"

    # 3. QR Code Configuration
    # version=1: Smallest matrix size (fits small text, auto-expands with fit=True)
    # ERROR_CORRECT_H: ~30% damage/scratch resistance
    # box_size=10: Pixel width/height of each box
    # border=4: Standard 4-box white padding around the QR code

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border = 4,
    )
 
    # 4. Data add karke matrix generate karo
    qr.add_data(data)
    qr.make(fit=True)
    
    #5. image create karna hai ab
    img = qr.make_image(fill_color="black", back_color="white")

    #6. save img to disk
    img.save(output_path)

    print(f"Success! QR Code generated: {os.path.abspath(output_path)}")

def main():
    generate_qrcode()


if __name__ == "__main__":
    main()
