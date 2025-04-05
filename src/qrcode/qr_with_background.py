"""
QR Code avec logo flouté en arrière-plan (effet design) avec `qrcode` + `Pillow`
"""

import qrcode
from PIL import Image, ImageEnhance, ImageFilter

def generate_qr_with_background():
    url = "https://github.com"
    qr_file = "../../outputs/qrcode/qrcode-with-bg.png"
    logo_path = "../../assets/logo.png"

    # Générer le QR de base
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="#004999", back_color="white").convert("RGBA")

    # Créer une image de fond plus grande
    background = Image.new("RGBA", (qr_img.size[0] + 80, qr_img.size[1] + 80), "#f0f0f0")

    try:
        # Charger le logo
        logo = Image.open(logo_path).convert("RGBA")

        # Redimensionner le logo pour remplir le fond
        logo = logo.resize(background.size)

        # Éclaircir + flouter le logo pour qu'il n’interfère pas
        logo = ImageEnhance.Brightness(logo).enhance(2.5)
        logo = logo.filter(ImageFilter.GaussianBlur(2))
        logo.putalpha(40)  # Transparence

        # Ajouter le logo flouté au fond
        background.paste(logo, (0, 0), logo)

    except Exception as e:
        print(f"⚠️ Logo non chargé : {str(e)}")

    # Positionner le QR au centre du fond
    qr_pos = (
        (background.size[0] - qr_img.size[0]) // 2,
        (background.size[1] - qr_img.size[1]) // 2
    )
    background.paste(qr_img, qr_pos, qr_img)

    background.save(qr_file)
    print(f"✅ QR Code design avec fond stylisé sauvegardé → {qr_file}")

if __name__ == "__main__":
    generate_qr_with_background()
