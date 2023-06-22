import qrcode

data = "https://whenlifehandsyoulemons.github.io/LED-Light-Wall/"

qr = qrcode.QRCode(version=1, box_size=1, border=0)

qr.add_data(data)
qr.make()

img = qr.make_image(fill_color="black", back_color="white")
img.save("Feature Testing/qr_code_test.png")
