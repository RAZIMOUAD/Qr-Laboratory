"""
QR Code avec logo centré, généré avec `qrcode` + `Pillow`
"""

import qrcode
from PIL import Image

def generate_qr_with_logo():
    url = "https://github.com"
    output_file = "../../outputs/qrcode/qrcode-with-logo.png"
    logo_path = "../../assets/logo.png"  # Ton logo à placer ici

    # Génération du QR Code
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Haute tolérance pour cacher au centre
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="#004999", back_color="white").convert('RGBA')

    try:
        # Charger et redimensionner le logo
        logo = Image.open(logo_path).convert('RGBA')

        # Calculer taille du logo (20% du QR Code)
        qr_size = qr_img.size[0]
        logo_size = int(qr_size * 0.2)
        logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

        # Calcul de la position du logo (centré)
        pos = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2)
        qr_img.paste(logo, pos, logo)

    except FileNotFoundError:
        print("⚠️ Logo introuvable. Le QR sera généré sans logo.")

    qr_img.save(output_file)
    print(f"✅ QR Code avec logo centré sauvegardé → {output_file}")

if __name__ == "__main__":
    generate_qr_with_logo()
