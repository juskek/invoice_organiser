from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os


def greet():
    print("Welcome to Invoice Organiser.")
    print("This script was specially created for Mr Chuans Beng.")

#%%

def getAbsolutePath(relativePath):
    dirname = os.path.dirname(__file__)
    absPath = os.path.join(dirname, relativePath)
    return absPath

#%% 

def processPDF():
    pdfs = getAbsolutePath("raw_invoices/DO-1.pdf")
    # pdfs = r"provide path to pdf file" # raw string literal
    print(f"Converting PDFs to image from: {pdfs}")
    pages = convert_from_path(pdfs, 350)

    i = 1
    for page in pages:
        image_name = "Page_" + str(i) + ".jpg"  
        page.save(image_name, "JPEG")
        i = i+1        

if __name__ == "__main__":
    greet()
    processPDF()