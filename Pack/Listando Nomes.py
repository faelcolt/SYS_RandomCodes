''' Função para criar uma lista de nomes e listá-los na ordem em que foram digitados com separação semântica e depois criar
um documento em word para ser reutilizado. ''' 

def listando_nomes():
    # adiciona os nomes digitados em uma lista
    lista_de_nomes = list()
    contador = 1
    while True:
        nome = str(input(f'Digite o {contador}º nome: ')).title()
        lista_de_nomes.append(nome)
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
        contador += 1
        if continuar == 'N':
            break


    # separa os nomes digitados na lista de forma semântica
    posicaoNome = 0
    print('Os nomes digitados foram: ', end='')
    for c in range(0, len(lista_de_nomes)):
        if lista_de_nomes[posicaoNome] == lista_de_nomes[-1] and len(lista_de_nomes) != 1:
            print('e ', end='')
        print(f'{lista_de_nomes[posicaoNome]}', end='')
        if lista_de_nomes[posicaoNome] == lista_de_nomes[-1]:
            print('. ', end='')
        elif lista_de_nomes[posicaoNome] == lista_de_nomes[-2]:
            print(' ', end='')
        else:
            print(', ', end='')
        posicaoNome += 1
    print()


    # permite que você dê um nome para o arquivo antes de criá-lo
    nome_do_arquivo = str(input('Digite o nome do arquivo: '))


    # essa função permite que a pessoa escolha se quer ler, escrever, modificar, apagar ou juntar arquivos
    # em andamento...
    
    
    # cria um documento em word para ser utilizado separadamente do código
    with open(f'{nome_do_arquivo}.txt', 'w') as arquivo:
        for texto in lista_de_nomes:
            arquivo.write(str(texto) + '\n')


listando_nomes()