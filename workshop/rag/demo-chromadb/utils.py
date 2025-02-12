import os

def setup_environment():
    os.environ['USER_AGENT'] = 'demoagent'

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
