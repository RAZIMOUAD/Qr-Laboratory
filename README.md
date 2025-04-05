# 📦 QR-Lab.io — Générateur de QR Codes professionnels & personnalisés

Bienvenue dans **QR-Lab.io**, un laboratoire de scripts Python puissants et didactiques pour explorer la génération de QR Codes modernes avec :

- ✨ Deux bibliothèques : `segno` et `qrcode`
- 🌎 Support multilingue
- 🎨 Logos (centre, fond, effet artistique)
- 📄 Intégration dans des flyers PDF professionnels

---

## 🚀 Fonctionnalités disponibles

| 📁 Module                     | Description                                                                 |
|----------------------------------------|-----------------------------------------------------------------------------|
| `segno/qr_basic.py`                    | QR Code simple PNG haute qualité                                           |
| `segno/qr_svg.py`                      | QR vectoriel SVG (qualité illimitée pour impression)                     |
| `segno/qr_with_logo.py`                | QR avec logo propre centré                                                |
| `segno/qr_with_background.py`          | QR avec logo flouté en fond artistique                                     |
| `segno/qr_multilang_site.py`           | QR multilingue vers plusieurs URL                                          |
| `qrcode/qr_basic.py`                   | QR simple PNG via la bibliothèque `qrcode`                                 |
| `qrcode/qr_svg.py`                     | QR vectoriel SVG avec `qrcode` factory                                      |
| `qrcode/qr_with_logo.py`               | QR avec logo propre centré                                                |
| `qrcode/qr_with_background.py`         | QR avec visuel flouté en arrière-plan                                      |
| `qrcode/qr_multilang_site.py`          | QR multilingue avec `qrcode`                                               |
| `reportlab/pdf_flyer_with_qr.py`       | Flyer PDF A4 professionnel avec QR + services + contacts                    |

---

## 🧰 Différences entre `segno` et `qrcode`

| Critère                   | `segno`                                 | `qrcode` (avec Pillow)               |
|--------------------------|------------------------------------------|--------------------------------------|
| Format SVG natif         | ✅ Oui                                | ✅ Oui (factory)                  |
| Qualité vectorielle      | ⭐⭐⭐⭐⭐ Ultra nette                   | ⭐⭐⭐ Moins précise en SVG         |
| Ajout facile de logo     | ❌ Non (doit être post-traité)     | ✅ Oui avec Pillow                |
| Simplicité de base       | ✅ Très simple                       | ✅ Simple aussi                   |
| Flexibilité graphique    | ❌ Limitée                           | ✅ Forte (effets, fond, flou, etc.) |

> ℹ️ Pour des QR SVG propres : `segno`
> 🎨 Pour des QR stylisés avec logo ou image : `qrcode`

---

## 🧹 Arborescence du projet

```bash
qr-lab/
├── src/
│   ├── segno/
│   │   ├── qr_basic.py
│   │   ├── qr_svg.py
│   │   ├── qr_with_logo.py
│   │   ├── qr_with_background.py
│   │   └── qr_multilang_site.py
│   ├── qrcode/
│   │   ├── qr_basic.py
│   │   ├── qr_svg.py
│   │   ├── qr_with_logo.py
│   │   ├── qr_with_background.py
│   │   └── qr_multilang_site.py
│   └── reportlab/
│       └── pdf_flyer_with_qr.py
│
├── outputs/
│   ├── qrcode-blue.svg
│   ├── qrcode-with-logo.png
│   ├── flyer_demo.pdf
│   └── ...
│
├── assets/
│   └── logo.png  # Logo fictif pour les tests (logo de Github)
│
├── notes/
│   └── buts-par-script.md  # Détails de chaque script
│
└── README.md
```

---

## 🛠️ Installation

```bash
pip install segno qrcode reportlab pillow
```

---

## 📊 Exemples d’exécution

### 1. QR Code PNG simple avec `segno`
```bash
python src/segno/qr_basic.py
```

### 2. QR Code multilingue
```bash
python src/qrcode/qr_multilang_site.py
```

### 3. Flyer PDF avec QR et infos pros
```bash
python src/reportlab/pdf_flyer_with_qr.py
```

---

## 🔄 Capture / Voir Dossier 'outputs'

- 🖼️ `outputs/qrcode-with-logo.png`
- 🖼️ `outputs/qrcode-with-bg.png`
- 📄 `outputs/flyer_demo.pdf` (aperçu flyer)

---

## 🧰 Objectif pédagogique du dépôt

Ce dépôt a été pensé pour :
- Expérimenter toutes les techniques de génération de QR Code
- Comprendre les avantages/inconvénients de chaque approche
- Produire des QR utilisables pour des clients, documents, flyers, affiches
- Centraliser la logique dans un code propre, documenté et réutilisable

---

## 💼 Auteur

Projet imaginé, testé et structuré par **[RAZI MOUAD]**
---

