from PyPDF2 import PdfWriter
import os 

merger= PdfWriter()
files =[files for files in os.listdir() if files.endswith('.pdf')]
for file in files:
    merger.append(files)

merger.write("merged.pdf")
merger.close()
