import fitz
import base64
from PIL import Image
import io
from concurrent.futures import ThreadPoolExecutor
import requests
import os


# List of URLs to download (Q1, Q2, Q3, Q4)
pdf_urls = [
    "https://www.apple.com/newsroom/pdfs/fy2023-q4/FY23_Q4_Consolidated_Financial_Statements.pdf",
    "https://www.apple.com/newsroom/pdfs/fy2023-q3/FY23_Q3_Consolidated_Financial_Statements.pdf",
    "https://www.apple.com/newsroom/pdfs/FY23_Q2_Consolidated_Financial_Statements.pdf",
    "https://www.apple.com/newsroom/pdfs/FY23_Q1_Consolidated_Financial_Statements.pdf"
]

# Download PDFs from the URLs and save them to the folder
def download_pdf(url, folder):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = os.path.join(folder, url.split("/")[-1])
        with open(file_name, "wb") as file:
            file.write(response.content)
        return file_name
    else:
        print(f"Failed to download PDF from {url}")
        return None

# Convert PDF to base64-encoded PNG images
def pdf_to_base64_pngs(pdf_path, quality=75, max_size=(1024, 1024)):
    # Open the PDF file
    doc = fitz.open(pdf_path)

    base64_encoded_pngs = []

    # Iterate through each page of the PDF
    for page_num in range(doc.page_count):
        # Load the page
        page = doc.load_page(page_num)

        # Render the page as a PNG image
        pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))

        # Convert the pixmap to a PIL Image
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Resize the image if it exceeds the maximum size
        if image.size[0] > max_size[0] or image.size[1] > max_size[1]:
            image.thumbnail(max_size, Image.Resampling.LANCZOS)

        # Convert the PIL Image to base64-encoded PNG
        image_data = io.BytesIO()
        image.save(image_data, format='PNG', optimize=True, quality=quality)
        image_data.seek(0)
        base64_encoded = base64.b64encode(image_data.getvalue()).decode('utf-8')
        base64_encoded_pngs.append(base64_encoded)

    # Close the PDF document
    doc.close()

    return base64_encoded_pngs

def process_pdf(pdf_path):
    with ThreadPoolExecutor() as executor:
        pdf_paths = list(executor.map(download_pdf, pdf_urls, [folder] * len(pdf_urls)))

    # Remove any None values (failed downloads) from pdf_paths
    pdf_paths = [path for path in pdf_paths if path is not None]
    return pdf_paths

# Function main
if __name__ == "__main__":
    # Create a folder to store the downloaded PDFs
    folder = "./images"
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Download the PDFs concurrently
    pdf_paths = process_pdf(folder)
    
    print(f"Downloaded {len(pdf_paths)} PDFs")