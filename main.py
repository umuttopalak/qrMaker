import qrcode

url = input("URL for qr:")

try:
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4)
    
    qr.add_data(url)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save("qrcode.png")
    print("Successfully created!")
except Exception as ex:
    print(f'exception message : {ex}')