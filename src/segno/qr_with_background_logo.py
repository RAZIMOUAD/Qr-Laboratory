"""
Génère un QR Code avec segno + un logo flouté et éclairci en arrière-plan.
Format final : PNG
Utilisation : impression, communication design
"""

import segno
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter
import os

def generate_qr_with_background_logo():
    # 1. Créer le QR Code temporaire
    qr = segno.make("https://github.com", error='h')
    qr.save("temp_qr.png", scale=10, dark="#004999", light="white", border=2)

    # 2. Charger l'image QR et convertir
    qr_image = Image.open("temp_qr.png").convert("RGBA")

    # 3. Créer un fond plus grand pour le design
    background = Image.new("RGBA", (qr_image.size[0] + 80, qr_image.size[1] + 80), "#f8f9fa")

    try:
        # 4. Charger et traiter le logo
        logo = Image.open("../../assets/logo.png").convert("RGBA")
        logo_size = min(background.size)
        logo = logo.resize((logo_size, logo_size))

        # 5. Centrer et flouter le logo
        logo_pos = ((background.size[0] - logo.size[0]) // 2,
                    (background.size[1] - logo.size[1]) // 2)
        enhancer = ImageEnhance.Brightness(logo)
        logo = enhancer.enhance(2)  # Plus lumineux
        logo = logo.filter(ImageFilter.GaussianBlur(2))
        logo.putalpha(25)  # Plus transparent

        background.paste(logo, logo_pos, logo)

    except Exception as e:
        print(f"[!] Problème avec le logo : {e}")

    # 6. Effet cercle doux au centre (optionnel)
    draw = ImageDraw.Draw(background)
    circle_size = min(background.size) - 20
    circle_pos = ((background.size[0] - circle_size) // 2,
                  (background.size[1] - circle_size) // 2)
    draw.ellipse(
        [circle_pos[0], circle_pos[1], circle_pos[0] + circle_size, circle_pos[1] + circle_size],
        fill="#e3f2fd"
    )

    # 7. Positionner le QR Code au centre du fond
    qr_pos = ((background.size[0] - qr_image.size[0]) // 2,
              (background.size[1] - qr_image.size[1]) // 2)
    background.paste(qr_image, qr_pos, qr_image)

    # 8. Sauvegarder le résultat
    background.save("../../outputs/segno/qr-bg-logo.png", quality=100)

    # 9. Nettoyage
    os.remove("temp_qr.png")

    print("✅ QR Code avec logo en arrière-plan créé avec succès !")

# Lancer
generate_qr_with_background_logo()
