# essa é a biblioteca que será utilizada para a leitura dos textos
# para baixá-la é só abrir o seu terminal e digitar "pip install pyttsx3"
import pyttsx3

book = open(r'texto_aleatorio.txt')
book_text = book.readlines()
engine = pyttsx3.init()
for texto in book_text:
    engine.say(texto)
    engine.runAndWait()