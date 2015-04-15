#!/usr/bin/python
from PyPDF2 import PdfFileWriter, PdfFileReader
import os.path

pdf_file_path = "/Users/Alex/Dev/python/PDF_FILES/Fillable_PDF_Sample.pdf"

# Make sure we have a valid path
if not os.path.exists(pdf_file_path):
    print "File ", pdf_file_path, " does not exist.\n Exiting...\n"
    exit();




 


