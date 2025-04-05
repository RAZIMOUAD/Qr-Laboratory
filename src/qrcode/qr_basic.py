"""
QR Code basique généré avec la bibliothèque `qrcode` (PIL)
"""

import qrcode

def generate_basic_qrcode():
    url = "https://github.com"
    file_name = "../../outputs/qrcode/qrcode-basic.png"

    # Configuration de base
    qr = qrcode.QRCode(
        version=1,  # taille automatique
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(url)
    qr.make(fit=True)

    # Génération avec couleurs personnalisées
    img = qr.make_image(fill_color="#004999", back_color="white")
    img.save(file_name)
    print(f"✅ QR Code généré avec succès → {file_name}")

if __name__ == "__main__":
    generate_basic_qrcode()
