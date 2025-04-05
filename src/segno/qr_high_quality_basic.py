"""
Génère un QR Code simple et propre avec la bibliothèque segno.
Lien utilisé : https://github.com
Sans logo, avec couleur personnalisée et correction d’erreur élevée.
"""

import segno

def generate_basic_qr():
    # Créer le QR Code avec correction d’erreur maximale (H)
    qr = segno.make("https://github.com", error='h')

    # Sauvegarder en PNG haute qualité (10 = bonne taille)
    qr.save(
        '../../outputs/segno/qr-basic-blue.png',
        scale=10,
        dark='#004999',   # Bleu foncé
        light='white',    # Fond blanc
        border=2          # Bordure (marge autour du QR)
    )

    print("✅ QR Code simple généré avec succès !")

# Lancer
generate_basic_qr()
