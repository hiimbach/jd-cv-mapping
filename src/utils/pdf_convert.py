from pypdf import PdfReader
from typing import Union, IO


def pdf_to_text(pdf_file: Union[str, IO]) -> str:
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text
