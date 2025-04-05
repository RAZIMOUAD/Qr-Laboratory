"""
Génère un QR Code SVG avec correction d’erreur basse (L).
But : comparaison avec version H pour taille et tolérance.
"""

import segno

def generate_qr_low_error_svg():
    # QR Code avec correction minimale
    qr = segno.make("https://github.com", error='l')  # minuscule L

    # Sauvegarder en SVG
    qr.save(
        '../../outputs/segno/qr-low-error.svg',
        scale=10,
        dark='#004999',
        light='white',
        border=2
    )

    print("✅ QR Code basse correction généré !")

# Lancer
generate_qr_low_error_svg()
