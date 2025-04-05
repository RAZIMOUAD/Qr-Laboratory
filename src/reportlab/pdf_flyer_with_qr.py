from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import mm
import segno
import os

# 🔧 CONFIGURATION PERSONNALISABLE ICI
COMPANY_NAME = "Nom de l'entreprise"
TAGLINE = "Votre slogan professionnel ici"
SITE_URL = "https://example.com"

SERVICES = [
    "✓ Service 1 de qualité",
    "✓ Service 2 sur-mesure",
    "✓ Disponibilité 24/7",
    "✓ Réservation facile en ligne"
]

CONTACT_INFO = [
    "📱 +212 6 XX XX XX XX",
    "✉ contact@exemple.com",
    "🌐 www.example.com",
    "📍 Adresse de l'entreprise"
]

SLOGAN = "Un partenaire fiable pour vos besoins"

# Crée le QR Code
def create_qr_code(link):
    qr = segno.make(link, error='h')
    qr_path = "qrcode_site.png"
    qr.save(qr_path, scale=20, dark='#1a365d', light='white', border=2)
    return qr_path

# Génère le PDF avec QR
def generate_flyer_pdf(qr_code_path):
    DARK_BLUE = HexColor('#1a365d')
    GOLD = HexColor('#c4a777')
    LIGHT_GRAY = HexColor('#f5f5f5')

    width, height = landscape(A4)
    pdf_path = "flyer_demo.pdf"
    c = canvas.Canvas(pdf_path, pagesize=landscape(A4))

    # Fond
    c.setFillColor(LIGHT_GRAY)
    c.rect(0, 0, width, height, fill=True)

    # Bande supérieure
    c.setFillColor(DARK_BLUE)
    c.rect(0, height - 50*mm, width, 50*mm, fill=True)

    # Titre
    c.setFont("Helvetica-Bold", 38)
    c.setFillColor(white)
    c.drawCentredString(width / 2, height - 35*mm, COMPANY_NAME)

    # Sous-titre
    c.setFont("Helvetica", 18)
    c.setFillColor(GOLD)
    c.drawCentredString(width / 2, height - 45*mm, TAGLINE)

    # QR Code à droite
    if os.path.exists(qr_code_path):
        qr_size = 70 * mm
        qr_x = width - 100 * mm
        qr_y = 50 * mm
        c.drawImage(qr_code_path, qr_x, qr_y, width=qr_size, height=qr_size)

        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(DARK_BLUE)
        c.drawCentredString(qr_x + qr_size / 2, qr_y - 7 * mm, "Scannez pour visiter notre site")

    # Services
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(DARK_BLUE)
    c.drawString(20*mm, height - 70*mm, "Nos Services")
    c.setStrokeColor(GOLD)
    c.setLineWidth(1)
    c.line(20*mm, height - 72*mm, 90*mm, height - 72*mm)

    c.setFont("Helvetica", 14)
    y = height - 80*mm
    for service in SERVICES:
        c.drawString(25*mm, y, service)
        y -= 8*mm

    # Contact
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(DARK_BLUE)
    c.drawString(20*mm, 65*mm, "Contactez-nous")
    c.line(20*mm, 63*mm, 100*mm, 63*mm)

    c.setFont("Helvetica", 14)
    y = 55*mm
    for info in CONTACT_INFO:
        c.drawString(25*mm, y, info)
        y -= 8*mm

    # Slogan en bas
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(DARK_BLUE)
    c.drawCentredString(width / 2, 20*mm, SLOGAN)

    c.save()
    print("✅ Flyer PDF généré avec succès :", pdf_path)

# Lancer
if __name__ == "__main__":
    qr_path = create_qr_code(SITE_URL)
    generate_flyer_pdf(qr_path)


