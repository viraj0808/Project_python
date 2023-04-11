import image
import qrcode

qr=qrcode.QRCode(
    version= 15, # version of qr code
    box_size= 10,
    border= 5
)
data = " enter qr code"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("test.png")