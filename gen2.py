import qrcode
from PIL import Image

url = input("Enter URL: ")
if not url.startswith("http"):
    url = "https://" + url

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # allows up to 30% error correction
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Generate colored QR code
img = qr.make_image(fill_color="yellow", back_color="black")
img.save("custom_qr.png")
