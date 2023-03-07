listaDeNomes = list()
contador = 1

while True:
    nome = str(input(f'Digite o {contador}º nome: ')).capitalize()
    listaDeNomes.append(nome)
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    contador += 1
    if continuar == 'N':
        break
    
print(f'Os nomes digitados foram {listaDeNomes}')
    