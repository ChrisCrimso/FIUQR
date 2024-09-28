import qrcode
from PIL import Image
# Create a QRCode object


pantherGold = '#B6862C'
pantherBlue = '#081E3F'
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add the data
qr.add_data("fiu.edu")
qr.make(fit=True)

# Generate the QR code with custom colors
img = qr.make_image(fill_color=pantherGold, back_color=pantherBlue)

# Save the image
img.save("Panther.png")
