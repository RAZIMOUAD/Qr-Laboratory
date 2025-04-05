"""
Génère un QR Code avec `segno` et ajoute un logo au centre (PNG uniquement).
Lien : https://github.com
Logo : assets/logo.png (doit exister)
"""

import segno
from PIL import Image

def generate_qr_with_centered_logo():
    # Génération du QR Code en PNG temporaire
    qr = segno.make("https://github.com", error='h')  # Correction haute = logo OK
    qr.save(
        "temp_qr.png",
        scale=10,
        dark="#004999",
        light="white",
        border=2
    )

    # Charger l'image QR + le logo
    qr_image = Image.open("temp_qr.png").convert("RGBA")
    logo = Image.open("../../assets/logo.png").convert("RGBA")

    # Redimensionner le logo (env. 20% du QR)
    logo_size = int(min(qr_image.size) * 0.20)
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # Positionner au centre
    pos = (
        (qr_image.size[0] - logo_size) // 2,
        (qr_image.size[1] - logo_size) // 2
    )

    # Coller le logo
    qr_image.paste(logo, pos, logo)

    # Enregistrer le résultat
    qr_image.save("../../outputs/segno/qr-logo-center.png", quality=100)

    # Nettoyer le fichier temporaire
    import os
    os.remove("temp_qr.png")

    print("✅ QR Code avec logo au centre généré !")

# Lancer
generate_qr_with_centered_logo()
