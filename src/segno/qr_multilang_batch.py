"""
Génère des QR Codes pour chaque version linguistique réelle du site Transport Ouhaddou.
QR Codes sauvegardés avec le nom de la langue, pour intégration dans supports marketing.
"""

import segno
import os

def generate_real_multilang_qrs():
    # Dictionnaire réel des langues avec leurs URL
    urls = {
        "fr": ("Français", "https://transportouhaddou.com/index.php"),
        "en": ("English", "https://transportouhaddou.com/languages/english/index.php"),
        "de": ("Deutsch", "https://transportouhaddou.com/languages/german/index.php"),
        "es": ("Español", "https://transportouhaddou.com/languages/spanish/index.php"),
        "it": ("Italiano", "https://transportouhaddou.com/languages/italian/index.php"),
        "zh": ("中文", "https://transportouhaddou.com/languages/chinese/index.php"),
    }

    # Dossier de sortie
    output_dir = "../../outputs/segno/multilang-site/"
    os.makedirs(output_dir, exist_ok=True)

    for code, (name, url) in urls.items():
        qr = segno.make(url, error='h')
        file_name = f"{output_dir}qr-{code}-{name.lower()}.png"
        qr.save(file_name, scale=10, dark='#004999', light='white', border=2)
        print(f"✅ QR généré pour {name} → {file_name}")

    print("🎉 Tous les QR Codes multilingues du site sont prêts.")

# Lancer
generate_real_multilang_qrs()
