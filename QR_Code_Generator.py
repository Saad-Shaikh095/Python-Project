import qrcode as qr

# My LinkedIn Profile QR Code Generator
img = qr.make("https://www.linkedin.com/in/saad-shaikh-7a1a53331/")
img.save("Saad_shaikh_LinkedIn_QR_Code.png")
