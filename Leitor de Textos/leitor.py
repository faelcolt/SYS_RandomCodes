import pyttsx3

book = open(r'texto_aleatorio.txt')
book_text = book.readlines()
engine = pyttsx3.init()
for texto in book_text:
    engine.say(texto)
    engine.runAndWait()