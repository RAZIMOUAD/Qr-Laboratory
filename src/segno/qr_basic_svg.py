"""
Génère un QR Code simple avec segno au format SVG.
Lien utilisé : https://github.com

Sans logo, avec couleur personnalisée et correction d’erreur maximale.
"""

import segno

def generate_basic_qr_svg():
    # Créer le QR Code avec correction maximale
    qr = segno.make("https://github.com", error='h')

    # Sauvegarder en SVG vectoriel
    qr.save(
        '../../outputs/segno/qr-basic-blue.svg',
        scale=10,            # Taille générale
        dark='#004999',      # Couleur du QR Code
        light='white',       # Fond
        border=2             # Marge autour
    )

    print("✅ QR Code SVG généré avec succès !")

# Lancer
generate_basic_qr_svg()
