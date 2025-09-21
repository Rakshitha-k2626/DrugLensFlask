import qrcode

img = qrcode.make("san")
img.save("san_qr.png")
print("QR code image 'san_qr.png' created.")
