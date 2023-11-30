from PIL import Image, ImageDraw, ImageFont
import csv
import os
import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Image as rl_image  
import datetime

width, height = 1011, 639
background_color = (255, 255, 255)

font_size = 24

font = ImageFont.truetype("/Library/Fonts/Arial.ttf", font_size)

menlo_font = ImageFont.truetype("/Library/Fonts/Menlo.ttc", font_size)

text_color = (0, 0, 0)

current_date = datetime.datetime.now().strftime("%Y-%m-%d")

image_folder = f'/Users/asray/Downloads/Insurance_Cards_{current_date}/'

os.makedirs(image_folder, exist_ok=True)

output_folder = image_folder

field_coordinates = {
    "Name": (25, 175),
    "ID Number": (25, 215),
    "Group No": (25, 290),
    "RXBIN": (25, 330),
    "RXPCN": (25, 370),
    "RXGRP": (25, 410),
    "Plan Code": (25, 450),
    "DED In Network Indv$/Fam$": (580, 280),
    "DED Out of Network Indv$/Fam$": (760, 280),
    "OPM DED In Network Indv$/Fam$": (580, 315),
    "OPM Out of Network Indv$/Fam$": (760, 315),
}

def generate_insurance_card_with_qr(data, output_file):
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    fake_logo = Image.open("/Users/asray/Downloads/fake-insurance-logo.png")
    saftinet_logo = Image.open("/Users/asray/Downloads/saftinet1-logo.png")
    suitcase_logo = Image.open("/Users/asray/Desktop/suitcase.png")

    logo_size = (100, 100)
    fake_logo = fake_logo.resize(logo_size)
    saftinet_logo = saftinet_logo.resize(logo_size)
    suitcase_logo = suitcase_logo.resize(logo_size)
    image.paste(fake_logo, (20, 20))
    image.paste(saftinet_logo, (130, 20))
    image.paste(suitcase_logo, (700, 520))

    text_x, text_y = 250, 80

    draw.text((text_x, text_y), "A Saftinet Product", fill=text_color, font=font)

    text_x, text_y = 250, 40

    draw.text((text_x, text_y), "Fake Insurance Co.", fill=text_color, font=font)

    text_x, text_y = 20, 120

    draw.text((text_x, text_y), "___________________________________    _____________________________________", fill=text_color, font=font)

    text_x, text_y = 20, 250

    draw.text((text_x, text_y), "___________________________________    _____________________________________", fill=text_color, font=font)

    text_x, text_y = 20, 470

    draw.text((text_x, text_y), "___________________________________    _____________________________________", fill=text_color, font=font)

    text_x, text_y = 580, 210

    draw.text((text_x, text_y), "In Network", fill=text_color, font=font)

    text_x, text_y = 580, 240

    draw.text((text_x, text_y), "Indv$/Fam$", fill=text_color, font=font)

    text_x, text_y = 760, 210

    draw.text((text_x, text_y), "Out of Network", fill=text_color, font=font)

    text_x, text_y = 760, 240

    draw.text((text_x, text_y), "Indv$/Fam$", fill=text_color, font=font)

    text_x, text_y = 502, 280

    draw.text((text_x, text_y), "DED", fill=text_color, font=font)

    text_x, text_y = 502, 315

    draw.text((text_x, text_y), "OPM", fill=text_color, font=font)

    text_x, text_y = 502, 410

    draw.text((text_x, text_y), "Full plan details and cost share info", fill=text_color, font=font)

    text_x, text_y = 502, 435

    draw.text((text_x, text_y), "available on mobile app or at", fill=text_color, font=font)

    text_x, text_y = 502, 460

    draw.text((text_x, text_y), "fakeinsuranceco.com", fill=text_color, font=font)

    text_x, text_y = 505, 40

    draw.text((text_x, text_y), "FakeInsuranceCo POS", fill=text_color, font=font)

    text_x, text_y = 505, 65

    draw.text((text_x, text_y), "base plan", fill=text_color, font=font)

    text_x, text_y = 870, 40

    draw.text((text_x, text_y), "FICSSHIP", fill=text_color, font=font)

    text_x, text_y = 25, 530

    draw.text((text_x, text_y), "Customer Service:", fill=text_color, font=font)

    text_x, text_y = 25, 560

    draw.text((text_x, text_y), "+1-800-909-FAKE", fill=text_color, font=font)

    for field, (x, y) in field_coordinates.items():
        if field in ["Name", "ID Number"]:
            text = data[field]
            draw.text((x, y), text, fill=text_color, font=font)
        elif field in ["Group No", "RXBIN", "RXPCN", "RXGRP", "Plan Code"]:
            field_width = 16
            text = f"{field.ljust(field_width)} {data[field]}"
            draw.text((x, y), text, fill=text_color, font=menlo_font)
        else:
            text = data[field]
            draw.text((x, y), text, fill=text_color, font=font)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(", ".join(data.values()))
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image = qr_image.resize((175, 175))
    image.paste(qr_image, (820, 450))

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    image.save(output_file)

file_path = '/Users/asray/Downloads/Insurance-Customer-Info - Sheet1.csv'

with open(file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data = {
            "Name": row["Name"],
            "ID Number": row["ID Number"],
            "Group No": row["Group No."],
            "RXBIN": row["RXBIN"],
            "RXPCN": row["RXPCN"],
            "RXGRP": row["RXGRP"],
            "Plan Code": row["Plan Code"],
            "DED In Network Indv$/Fam$": row["DED In Network Indv$/Fam$"],
            "DED Out of Network Indv$/Fam$": row["DED Out of Network Indv$/Fam$"],
            "OPM DED In Network Indv$/Fam$": row["OPM DED In Network Indv$/Fam$"],
            "OPM Out of Network Indv$/Fam$": row["OPM Out of Network Indv$/Fam$"]
        }
        file_name = f"{row['Name'].replace(' ', '_')}_insurance_card.png"
        output_file = os.path.join(output_folder, file_name)
        generate_insurance_card_with_qr(data, output_file)

print("Insurance cards with QR codes generated and saved.")

pdf_filename = f'saftinet_insurance_{current_date}.pdf'

card_images = []

for filename in os.listdir(output_folder):
    if filename.endswith('.png'):
        card_images.append(os.path.join(output_folder, filename))

doc = SimpleDocTemplate(pdf_filename, pagesize=A4)

elements = []

cards_per_page = 8
card_width = 200
card_height = 125

images = [rl_image(image_path, width=card_width, height=card_height) for image_path in card_images]
elements.extend(images)

doc.build(elements)

print(f"PDF '{pdf_filename}' generated with {len(card_images)} insurance cards.")