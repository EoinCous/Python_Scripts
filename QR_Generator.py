#This script generates a QR code from a URL. Run the script and enter the URL into the GUI
import os
import sys
import tkinter as tk
import tkinter.messagebox as messagebox
import qrcode

def generate_qr_code(url):
    # Create the QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code instance
    qr.add_data(url)
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image to the downloads folder
    downloads_folder = os.path.expanduser("~/Downloads")
    file_path = os.path.join(downloads_folder, "qr_code.png")
    with open(file_path, "wb") as f:
        img.save(f)
    return True

def on_generate_button_click():
    url = entry.get()
    if generate_qr_code(url):
        messagebox.showinfo("Success", "QR code generated successfully! Check downloads folder.")
        sys.exit()

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("300x200")
    root.title("QR Code Generator")

    label = tk.Label(root, text="Enter the URL:")
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=10)

    button = tk.Button(root, text="Generate QR Code", command=on_generate_button_click)
    button.pack(pady=10)

    root.mainloop()
