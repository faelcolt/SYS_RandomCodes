import PyPDF2

# carrega o arquivo PDF
pdfFileObj = open('meupdf.pdf', 'rb')

# faz a leitura do arquivo PDF
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# captura a primeira página do PDF
pageObj = pdfReader.getPage(0)

# extrai o texto do PDF e passa para variável
text = pageObj.extractText()

# mostra o texto do PDF
print(text)
