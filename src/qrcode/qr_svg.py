"""
QR Code SVG généré avec la bibliothèque `qrcode` (factory SVG)
"""

import qrcode
import qrcode.image.svg

def generate_svg_qrcode():
    url = "https://github.com"
    file_name = "../../outputs/qrcode/qrcode-blue.svg"

    # Utilisation du moteur SVG
    factory = qrcode.image.svg.SvgImage

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2
    )

    qr.add_data(url)
    qr.make(fit=True)

    # Générer SVG avec couleur personnalisée
    img = qr.make_image(image_factory=factory)
    img.save(file_name)

    print(f"✅ QR Code SVG généré → {file_name}")

if __name__ == "__main__":
    generate_svg_qrcode()
