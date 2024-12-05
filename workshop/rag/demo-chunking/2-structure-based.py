from langchain_text_splitters import HTMLHeaderTextSplitter

# Specify the URL from which the text should be obtained
url="https://en.wikipedia.org/wiki/FIFA_World_Cup"

# Specify the header tags on which splits should be made
headers_to_split_on=[
    ("h1", "Header 1"),
    ("h2", "Header 2"),
    ("h3", "Header 3"),
    ("h4", "Header 4")
]

# Create the HTMLHeaderTextSplitter function
html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

# Create splits in text obtained from the url
html_header_splits = html_splitter.split_text_from_url(url)
print(html_header_splits)