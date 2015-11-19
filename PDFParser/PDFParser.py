import PyPDF2
import re

file = open('regions.pdf', 'rb')
reader = PyPDF2.PdfFileReader(file)

page = reader.getPage(0)

for i in str(page.extractText()).split():
    print(i)