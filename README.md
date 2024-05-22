# Saftinet Insurance Card Generator README

## Overview
This project is a Python-based script that generates insurance cards with QR codes for each customer listed in a CSV file. The generated cards are saved as PNG images and compiled into a PDF document.

## Requirements
- Python 3.x
- Libraries: `PIL` (Pillow), `csv`, `os`, `qrcode`, `reportlab`
- Font files: Arial and Menlo

## Installation
1. **Install Python 3.x** if not already installed. You can download it from [python.org](https://www.python.org/).
2. **Install required Python libraries** using pip:
   ```sh
   pip install pillow qrcode[pil] reportlab
   ```
3. **Ensure the necessary font files** (Arial and Menlo) are available on your system. If not, you can download and place them in the appropriate directory.

## Project Structure
- **insurance_card_generator.py**: The main script to generate insurance cards and the PDF.
- **Insurance-Customer-Info - Sheet1.csv**: CSV file containing customer information.
- **fake-insurance-logo.png**: Sample logo image for the insurance company.
- **saftinet1-logo.png**: Sample logo image for Saftinet.
- **suitcase.png**: Sample suitcase logo image.

## Usage

### Preparing the CSV File
Ensure your CSV file follows this structure with the exact column headers:
- Name
- ID Number
- Group No.
- RXBIN
- RXPCN
- RXGRP
- Plan Code
- DED In Network Indv$/Fam$
- DED Out of Network Indv$/Fam$
- OPM DED In Network Indv$/Fam$
- OPM Out of Network Indv$/Fam$

### Running the Script
1. **Place the CSV file** (`Insurance-Customer-Info - Sheet1.csv`) in the specified directory.
2. **Execute the script**:
   ```sh
   python insurance_card_generator.py
   ```
3. The script will create a folder named `Insurance_Cards_<current_date>` in your Downloads directory. It will generate PNG images of the insurance cards and save them in this folder.
4. A PDF file named `saftinet_insurance_<current_date>.pdf` will also be generated, containing all the insurance cards.

### Script Details
1. **Setting up the canvas**: A blank image is created for each insurance card with a white background.
2. **Adding logos**: Logos for the insurance company, Saftinet, and a suitcase are added to the card.
3. **Adding text fields**: Customer-specific data and static text are drawn on the card.
4. **Generating QR code**: A QR code containing all customer data is generated and added to the card.
5. **Saving the image**: The insurance card is saved as a PNG file.
6. **Compiling PDF**: All generated PNG files are compiled into a PDF document.

### Output
- **PNG files**: Individual insurance cards for each customer.
- **PDF file**: A compiled document containing all the insurance cards.

## Notes
- Ensure the font files (Arial and Menlo) are correctly specified in the script.
- Update the paths for logos and CSV file as needed.
- The script assumes a specific directory structure and file naming convention. Adjust paths if your structure is different.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements
- [Pillow](https://python-pillow.org/)
- [ReportLab](https://www.reportlab.com/)
- [qrcode](https://pypi.org/project/qrcode/)
