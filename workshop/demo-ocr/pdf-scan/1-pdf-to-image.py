import fitz

pdffile = "doc-scan.pdf"
doc = fitz.open(pdffile)
zoom = 4
mat = fitz.Matrix(zoom, zoom)
count = 0
# Count variable is to get the number of pages in the pdf
for p in doc:
    count += 1
for i in range(count):
    val = f"image_{i+1}.png"
    page = doc.load_page(i)
    pix = page.get_pixmap(matrix=mat)
    pix.save(val)
doc.close()
