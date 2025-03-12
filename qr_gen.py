import pyqrcode
import os

def generate_qr(data: str, file_name: str = "qr_code.png"):
    """Generates a QR code from the given data and saves it as an image file."""
    if not data.strip():
        raise ValueError("Data for QR code generation cannot be empty.")

    # Create QR code
    qr = pyqrcode.create(data)
    
    # Save QR code as a PNG file
    qr.png(file_name, scale=5)
    
    # Check if the file was created successfully
    if os.path.exists(file_name):
        print(f"QR Code generated and saved successfully as '{file_name}'!")
    else:
        print("Failed to save QR Code. Please try again.")

if __name__ == "__main__":
    try:
        data = input("Enter the data or URL to generate QR Code: ")
        file_name = input("Enter the file name to save (with .png extension, or leave blank for 'qr_code.png'): ")
        
        # Use default name if not specified
        if not file_name.strip():
            file_name = "qr_code.png"
        
        generate_qr(data, file_name)
    except Exception as e:
        print(f"Error: {e}")
