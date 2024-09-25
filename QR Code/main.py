import qrcode
from PIL import Image 
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=5,border=4 )

qr.add_data("https://www.linkedin.com/in/akash-asati-25b6041a6/")

qr.make(fit=True)

img=qr.make_image(fill_color="black",back_color="white")
img2=qr.make_image(fill_color="red",back_color="white")
img3=qr.make_image(fill_color="red",back_color="blue")

img.save("temp_QR.png")
img2.save("temp_QR1.png")
img3.save("temp_QR2.png")
