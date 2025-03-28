import fitz  # PyMuPDF for PDFs
import docx  # python-docx for Word files
import pandas as pd  # pandas for Excel files
import tkinter as tk
from tkinter import filedialog

def search_in_pdf(file_path, keyword):
    doc = fitz.open(file_path)
    for page_num in range(len(doc)):
        text = doc[page_num].get_text()
        if keyword.lower() in text.lower():
            print(f'Keyword found on page {page_num + 1}')

def search_in_word(file_path, keyword):
    doc = docx.Document(file_path)
    for i, para in enumerate(doc.paragraphs):
        if keyword.lower() in para.text.lower():
            print(f'Keyword found in paragraph {i + 1}')

def search_in_excel(file_path, keyword):
    xls = pd.ExcelFile(file_path)
    for sheet_name in xls.sheet_names:
        df = xls.parse(sheet_name)
        if df.astype(str).apply(lambda x: x.str.contains(keyword, case=False, na=False)).any().any():
            print(f'Keyword found in sheet: {sheet_name}')

def search_in_text(file_path, keyword):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if keyword.lower() in line.lower():
                print(f'Keyword found in line {i + 1}')

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        keyword = input("Enter the keyword to search: ")
        if file_path.endswith('.pdf'):
            search_in_pdf(file_path, keyword)
        elif file_path.endswith('.docx'):
            search_in_word(file_path, keyword)
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            search_in_excel(file_path, keyword)
        elif file_path.endswith('.txt'):
            search_in_text(file_path, keyword)
        else:
            print("Unsupported file format!")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    select_file()
