from typing import Any
from openai import BaseModel
from unstructured.partition.pdf import partition_pdf

path = "files/"

# Get elements
raw_pdf_elements = partition_pdf(
    filename=path + "split-page8.pdf",
    # Unstructured first finds embedded image blocks
    extract_images_in_pdf=False,
    # Use layout model (YOLOX) to get bounding boxes (for tables) and find titles
    # Titles are any sub-section of the document
    infer_table_structure=True,
    strategy="hi_res",
)

# Get tables
tables = [el for el in raw_pdf_elements if el.category == "Table"]
print("Number of tables in pdf: ", len(tables))
if tables:
    for idx, table in enumerate(tables):
        print(f"Table {idx + 1}:")
        print(table.text)
        print(table.metadata.text_as_html)
else:
    print("No tables found in the PDF.")


