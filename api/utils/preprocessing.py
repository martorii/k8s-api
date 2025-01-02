import pdfplumber
import io

from .logger import setup_logger
logger = setup_logger(__name__)


def extract_content_from_bytes(data: bytes) -> str:
    # ToDo: Get file extension
    file_extension = 'pdf'
    # Convert bytes to a file-like object
    file = io.BytesIO(data)
    # Store content
    content = ""
    if file_extension == "pdf":
        with pdfplumber.open(file) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                content += page.extract_text()
    else:
        raise NotImplementedError("This file type is not implemented yet.")
    return content

