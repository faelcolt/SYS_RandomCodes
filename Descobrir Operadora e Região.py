'''Descobre a região e a operadora do número digitado'''

# bibliotecas utilizadas
import phonenumbers
from phonenumbers import geocoder, carrier

# digite o número com código, país e ddd
numeroTelefone = phonenumbers.parse('+551922172830')

# captura operadora
operadora = carrier.name_for_number(numeroTelefone, 'pt-br')

# captura região
regiao = geocoder.description_for_number(numeroTelefone, 'pt-br')

# mostra resultados
print('A operadora é:' + operadora)
print('O estado é:' + regiao )
