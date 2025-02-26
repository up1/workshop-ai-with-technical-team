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

class Element(BaseModel):
    type: str
    text: Any


# Categorize by type
categorized_elements = []
for element in raw_pdf_elements:
    if "unstructured.documents.elements.Table" in str(type(element)):
        categorized_elements.append(Element(type="table", text=str(element)))
    else:
        categorized_elements.append(Element(type="text", text=str(element)))

# Tables
table_elements = [e for e in categorized_elements if e.type == "table"]
print("Number of table elements:", len(table_elements))

# Text
text_elements = [e for e in categorized_elements if e.type == "text"]
print("Number of text elements:", len(text_elements))
print("Text elements:", text_elements[0].text)
print("Text elements:", text_elements[1].text)
