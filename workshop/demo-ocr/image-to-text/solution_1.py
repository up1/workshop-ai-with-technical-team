import pytesseract
import easyocr
from PIL import Image

def extract_text_from_image(image_file):
    image = Image.open(image_file)
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

def extract_text_with_easyocr(image_file):
    reader = easyocr.Reader(['en', 'th'])
    result = reader.readtext(image_file, detail=0)
    return result

if __name__ == "__main__":
    local_image_path = "image.png"
    extracted_text = extract_text_from_image(local_image_path)
    print("Extracted text using pytesseract:")
    print(extracted_text)
    extracted_text_easyocr = extract_text_with_easyocr(local_image_path)
    print("Extracted text using easyocr:")
    print(extracted_text_easyocr)