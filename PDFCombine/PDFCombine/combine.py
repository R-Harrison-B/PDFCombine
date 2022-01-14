import sys

import PyPDF2, os
combine = []
for file in os.listdir('.'):
    if file.endswith('.pdf'):
        combine.append(file)
        combine.sort(key = str.lower)
        pdfWriter = PyPDF2.PdfFileWriter()
for file in combine:
    pdfFileObj = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for page in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        if len(sys.argv) > 1:
            text = pageObj.extractText()
            for extract in sys.argv:
                if text is not None and extract in text:
                    pdfWriter.addPage(pageObj)
                    break
        else:               
            pdfWriter.addPage(pageObj)
    pdfOutput = open('combine.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()