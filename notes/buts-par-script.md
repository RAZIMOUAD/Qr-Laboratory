### Script : qr_high_quality_basic.py

📌 But : Générer un QR Code simple et lisible en version .png
🔗 URL : https://github.com
🎨 Couleur : Bleu foncé (#004999)
💡 Correction : H (haute)
📁 Résultat : ./outputs/segno/qr-basic-blue.png

### Script : qr_basic_svg.py

📌 But : Générer un QR Code vectoriel au format SVG avec segno
🔗 URL : https://github.com
🎨 Couleur : Bleu foncé (#004999)
📐 Format : SVG (infini pour l’impression)
📁 Résultat : ./outputs/segno/qr-basic-blue.svg

### Script : qr_basic_svg_low_error.py

📌 But : Générer un QR Code SVG avec correction basse (niveau L)
🔗 URL : https://github.com
🎨 Couleur : Bleu foncé
🧠 Correction : L (low) → moins tolérant, mais plus compact
📁 Résultat : ./outputs/segno/qr-low-error.svg

### Script : qr_svg_logo_center.py

📌 But : Générer un QR Code avec `segno` et intégrer un logo centré (PNG final)
🔗 URL : https://github.com
📐 Format : PNG (non vectoriel)
📌 Logo : ./assets/logo.png (20% taille du QR)
📁 Résultat : ./outputs/segno/qr-logo-center.png
🧠 Remarque : Segno ne gère pas l’intégration du logo en SVG pur, à faire via Inkscape

### Script : qr_svg_for_manual_logo.py

📌 But : Générer un QR Code vectoriel en SVG avec `segno` prêt à recevoir un logo
🎯 Logo à insérer manuellement (Inkscape ou XML)
🔗 URL : https://github.com
🖨️ Format : SVG pur (qualité infinie)
📁 Fichier : ./outputs/segno/qr-for-logo-manual.svg

### Script : qr_with_background_logo.py

📌 But : Générer un QR Code avec `segno` et un logo en arrière-plan flouté
🔗 URL : https://github.com
🎨 Couleur : Bleu foncé QR (#004999) + fond clair
🖼️ Logo : ./assets/logo.png (flouté, centré derrière)
📁 Résultat : ./outputs/segno/qr-bg-logo.png
💡 Remarque : effet graphique doux, non adapté si impression NB ou low resolution

### Script : qr_site_multilang_real.py

📌 But : Générer les QR Codes correspondant aux versions linguistiques réelles du site TransportOuhaddou
🌍 Langues supportées : fr, en, de, es, it, zh
🔗 Chaque QR pointe vers la bonne URL linguistique
📁 Résultat : ./outputs/segno/multilang-site/qr-{code}-{lang}.png
🎯 Utilisation : flyers traduits, affiches vitrines, brochures par langue

### Script : pdf_flyer_with_qr.py

📌 But :
Générer un flyer PDF professionnel contenant un QR Code, avec personnalisation facile :
- Nom de l'entreprise
- Slogan
- URL du site
- Services proposés
- Coordonnées de contact
- Slogan final en bas

🛠️ Technologies :
- `segno` pour créer le QR Code (PNG)
- `reportlab` pour générer un flyer A4 paysage avec design structuré

📂 Résultats :
- `qrcode_site.png` (temporaire ou à réutiliser)
- `flyer_demo.pdf` (flyer final prêt à l'impression ou à la distribution numérique)

🎨 Personnalisations possibles :
- Couleurs du thème (DARK_BLUE, GOLD, etc.)
- Taille et position du QR Code
- Ajout d'un logo possible ultérieurement

📁 Dossier recommandé : `src/reportlab/`

🔗 Idéal pour :
- Créer des supports pro avec QR personnalisé
- Générer dynamiquement des flyers multilingues
- Démo de QR dans un contexte de communication visuelle

######
###### Passons a la Biblio : QRCODE
######


### Script : qr_basic.py (qrcode)

📌 But : Générer un QR Code PNG simple avec la bibliothèque `qrcode` (basée sur PIL)
🔗 URL cible : https://github.com
🎨 Couleurs personnalisables
🧱 Bordure = 4, taille = auto
📁 Résultat : outputs/qrcode/qrcode-basic.png
📦 Lib utilisée : qrcode (Pillow)

### Script : qr_svg.py (qrcode)

📌 But : Générer un QR Code vectoriel (SVG) pour impression
🔗 URL cible : https://github.com
🧱 Format SVG lisible, compatible Illustrator/Inkscape
📁 Résultat : outputs/qrcode/qrcode-blue.svg
📦 Lib utilisée : qrcode + qrcode.image.svg.SvgImage

### Script : qr_with_logo.py (qrcode)

📌 But : Générer un QR Code PNG avec un logo centré (20%)
🔗 URL cible : https://github.com
🖼️ Logo fictif : assets/logo.png (PNG transparent recommandé)
⚠️ Tolérance d’erreur : H (30%) pour intégrer un logo sans casser le QR
📁 Résultat : outputs/qrcode/qrcode-with-logo.png
📦 Lib utilisée : qrcode + Pillow (PIL)

### Script : qr_with_background.py (qrcode)

📌 But : Générer un QR Code lisible avec un logo en arrière-plan flouté
🎨 Effet design grâce à PIL : flou, opacité, éclaircissement
🔗 URL cible : https://github.com
📁 Résultat : outputs/qrcode/qrcode-with-bg.png
📦 Lib utilisée : qrcode + Pillow (PIL)
📂 Astuce : fonctionne bien en flyer ou site imprimé


### Script : qr_multilang_site.py (qrcode)

📌 But : Générer un QR Code par langue pour un site multilingue
🌐 Base : https://qr-lab.io/
🈯 Langues : fr, en, de, es, zh, it
📁 Résultat : outputs/qrcode/multilang/qr-fr.png, qr-en.png, ...
📦 Lib utilisée : qrcode (avec couleurs personnalisées)
