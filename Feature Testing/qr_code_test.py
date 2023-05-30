import qrcode

data = "https://www.google.com"

qr = qrcode.QRCode(version=1, box_size=1, border=0)

qr.add_data(data)
qr.make()

img = qr.make_image(fill_color="white", back_color="black")
img.save("test_qr_code.png")

"""
Code for the RPi
"""
# def showQRCode(image_path):
#     image = iio.read(image_path).get_data(0)

#     y = 0
#     while y < len(image):
#         x = 0
#         while x < len(image[y]):
#             setPixelsColour(image[y][x], getLED(x, y))
#             x += 1
#         y += 1

# Test QR code functionality
# showQRCode("test_qr_code.png")
# time.sleep(10)
