# biblioteca para a leitura de texto
import pyttsx3

# selecione o arquivo que deseja ler
book = open(r"audiobook.txt")
book_text = book.readlines()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()