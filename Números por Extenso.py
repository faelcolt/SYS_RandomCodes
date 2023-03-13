'''Escreve o número digitado por extenso em português e inglês'''

# biblioteca utilizada
# para baixá-la é só abrir o seu terminal e digitar "pip install num2words"
from num2words import num2words

# digite seu número
numero = int(input('Digite um número: '))

# conversão para extenso em português
num_pt = num2words(numero, lang='pt_br')
print(f'Em português: {num_pt} ')

# conversão para extenso em português ordinal
num_pt_ord = num2words(numero, lang='pt_br', to='ordinal')
print(f'Em português ordinal: {num_pt_ord} ')

# conversão para extenso em inglês
num_en = num2words(numero, lang='en')
print(f'Em inglês: {num_en} ')

# conversão para extenso em inglês ordinal
num_en_ord = num2words(numero, lang='en', to='ordinal')
print(f'Em inglês (Ordinal): {num_en_ord} ')

