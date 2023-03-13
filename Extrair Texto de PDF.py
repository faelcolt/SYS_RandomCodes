'''Faz uma leitura do PDF e extrai o texto'''

# biblioteca utilizada para manipular PDF's
# para baixá-la é só abrir o seu terminal e digitar "pip install PyPDF2"
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
