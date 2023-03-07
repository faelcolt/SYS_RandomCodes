listaDeNomes = list()
contador = 1

while True:
    nome = str(input(f'Digite o {contador}º nome: ')).capitalize()
    listaDeNomes.append(nome)
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    contador += 1
    if continuar == 'N':
        break

posicaoNome = 0
print('Os nomes digitados foram: ',end='')
for c in range(0, len(listaDeNomes)):
    if listaDeNomes[posicaoNome] == listaDeNomes[-1]:
        print('e ', end='')
    print(f'{listaDeNomes[posicaoNome]}', end='')
    if listaDeNomes[posicaoNome] == listaDeNomes[-1]:
        print('. ', end='')
    else:
        print(', ', end='')
    posicaoNome += 1
    