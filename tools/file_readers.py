from langchain.tools import tool
import PyPDF2
from docx import Document
import os

@tool
def list_files_in_directory(directory_path: str) -> str:
    """List all files in a directory with their extensions"""
    try:
        files = []
        for file in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                _, ext = os.path.splitext(file)
                files.append(f"{file} ({ext})")
        
        if not files:
            return f"No files found in {directory_path}"
        
        return f"Files in {directory_path}:\n" + "\n".join(f"- {file}" for file in files)
    except Exception as e:
        return f"Error listing files in {directory_path}: {str(e)}"


@tool
def read_pdf_file(file_path: str) -> str:
    """Read the content of a PDF file."""
    #if not file_path.endswith('.pdf'):
    #    raise ValueError("The provided file is not a PDF.")
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for i, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if len(text) + len(page_text) <= 1000:
                    text += page_text + "\n"
                else:
                    remaining_characters = 1000 - len(text)
                    if remaining_characters > 0:
                        text += page_text[:remaining_characters]
                    text += "[truncated]"
                    
        return f"Content from PDF {file_path}:\n{text}"
    except Exception as e:
        return f"Error reading PDF {file_path}: {str(e)}"

@tool
def read_docx_file(file_path: str) -> str:
    """Read the content of a DOCX file."""
    if not file_path.endswith('.docx'):
        raise ValueError("The provided file is not a DOCX.")
    
    doc = Document(file_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return "\n".join(text)

@tool
def read_text_file(file_path: str) -> str:
    """Read content from plain text files (.txt, .md, .py, .json, etc.)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read(1000)
            # Check if there's more content
            if file.read(1):  # Try to read one more character
                content += "...[truncated]"
        return f"Content from {file_path}:\n{content}"
    except Exception as e:
        return f"Error reading {file_path}: {str(e)}"
