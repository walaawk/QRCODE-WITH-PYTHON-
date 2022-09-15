from dataclasses import dataclass
import qrcode
import image


qr= qrcode.QRCode(

    version=20,
    box_size=15,
    border=10
)

data="https://www.youtube.com/channel/UCHpZ56OgVuVYgHQyPCrFGVA"


qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("img.png")