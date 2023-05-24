import qrcode

data = "https://www.google.com"

qr = qrcode.QRCode(version=1, box_size=1, border=0)

qr.add_data(data)
qr.make()

img = qr.make_image(fill_color="white", back_color="black")
img.save("test_qr_code.png")
