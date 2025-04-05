"""
Génère un QR Code SVG avec segno prêt à recevoir un logo au centre.
Logo à insérer manuellement via Inkscape ou VS Code dans le fichier SVG.
"""

import segno

def generate_svg_for_manual_logo():
    qr = segno.make("https://github.com", error='h')  # Correction haute = logo supporté

    qr.save(
        '../../outputs/segno/qr-for-logo-manual.svg',
        scale=10,
        dark='#004999',
        light='white',
        border=2
    )

    print("✅ QR Code SVG prêt à être modifié manuellement")

# Lancer
generate_svg_for_manual_logo()
