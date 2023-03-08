''' Função para criar uma lista de nomes e listá-los na ordem em que foram digitados com separação semântica e depois criar
um documento em word para ser reutilizado. ''' 

# adiciona os nomes digitados em uma lista
listaDeNomes = list()
contador = 1

while True:
    nome = str(input(f'Digite o {contador}º nome: ')).title()
    listaDeNomes.append(nome)
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    contador += 1
    if continuar == 'N':
        break

# separa os nomes digitados de forma semântica
posicaoNome = 0
print('Os nomes digitados foram: ', end='')
for c in range(0, len(listaDeNomes)):
    if listaDeNomes[posicaoNome] == listaDeNomes[-1] and len(listaDeNomes) != 1:
        print('e ', end='')
    print(f'{listaDeNomes[posicaoNome]}', end='')
    if listaDeNomes[posicaoNome] == listaDeNomes[-1]:
        print('. ', end='')
    elif listaDeNomes[posicaoNome] == listaDeNomes[-2]:
        print(' ', end='')
    else:
        print(', ', end='')
    posicaoNome += 1

# essa parte do código criará um documento em word para ser utilizado separadamente do código

with open('lista_de_nomes.txt', 'w') as arquivo:
    for texto in listaDeNomes:
        arquivo.write(str(texto))





# em andamento...