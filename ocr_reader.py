import pytesseract
from PIL import Image, ImageEnhance, ImageFilter


def extract_prescription(image_path, medicine_list):

    img = Image.open(image_path)

    # ===== IMAGE IMPROVEMENT =====
    img = img.convert("L")

    img = ImageEnhance.Contrast(img).enhance(2)
    img = ImageEnhance.Sharpness(img).enhance(2)

    img = img.filter(ImageFilter.MedianFilter())

    # =============================

    text = pytesseract.image_to_string(
        img,
        config="--psm 6"
    )

    text = text.lower()

    print("\nOCR TEXT DETECTED:\n")
    print(text)

    medicines = []

    for med in medicine_list:

        if med in text:
            medicines.append(med)

    return medicines