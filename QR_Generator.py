#This script generates a QR code from a URL. Run the script and enter the URL into the GUI
import sys
import tkinter as tk
import tkinter.messagebox as messagebox
import qrcode
import os

def generate_qr_code(url):
    # Validate the input URL
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return False
    if not url.startswith("http://") and not url.startswith("https://"):
        messagebox.showerror("Error", "The URL must start with 'http://' or 'https://'.")
        return False

    # Create the QR code instance
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create QR code instance: {str(e)}")
        return False

    # Add data to the QR code instance
    try:
        qr.add_data(url)
        qr.make(fit=True)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add data to QR code instance: {str(e)}")
        return False

    # Generate the QR code image
    try:
        img = qr.make_image(fill_color="black", back_color="white")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR code image: {str(e)}")
        return False

    # Save the QR code image to the downloads folder
    downloads_folder = os.path.expanduser("~/Downloads")
    file_path = os.path.join(downloads_folder, "qr_code.png")
    try:
        with open(file_path, "wb") as f:
            img.save(f)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save QR code image: {str(e)}")
        return False

    return True

def on_generate_button_click():
    url = entry.get()
    if generate_qr_code(url):
        messagebox.showinfo("Success", "QR code generated successfully!")
        sys.exit()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("QR Code Generator")
    root.geometry("300x200")

    label = tk.Label(root, text="Enter the URL:")
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack(pady=10)

    button = tk.Button(root, text="Generate QR Code", command=on_generate_button_click)
    button.pack(pady=10)

    root.mainloop()
