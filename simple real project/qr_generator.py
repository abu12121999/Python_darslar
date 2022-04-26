import qrcode
def QR():
    qr = qrcode.QRCode(
        version=1,
        box_size=15,
        border=5
    )

    data = input("Enter any data to convert into a QR code: ")
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='green')
    img.save('link.png')
    return img
QR()