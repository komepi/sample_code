from PyPDF2 import PdfFileReader

filename = "CV_20240320_test_file.pdf"
reader = PdfFileReader(filename)
page = reader.pages[0]
print(page.extractText())