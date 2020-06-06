import PyPDF2
import sys

pdfFile = sys.argv[1]
wmFile = sys.argv[2]

template = PyPDF2.PdfFileReader(open(pdfFile,"rb"))
watermark = PyPDF2.PdfFileReader(open(wmFile,"rb"))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	with open("watermarked_File.pdf","wb") as file:
		output.write(file)