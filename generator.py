import qrcode
import webbrowser

# Ask user for the URL
url = input("Enter the URL you want to generate a QR code for: ")

# Ensure URL has a valid scheme
if not url.startswith("http://") and not url.startswith("https://"):
    url = "https://" + url  # Add https by default

# Generate and save the QR code
qr = qrcode.make(url)
filename = "qr_code.png"
qr.save(filename)

print(f"QR code saved as '{filename}'.")
print(f"Try scanning the code or open the URL directly: {url}")
