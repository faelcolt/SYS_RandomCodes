'''Coloca todos os textos digitados organizados em um bloco de notas linha a linha'''

# troque as palavras entre aspas pelas palavras que deseja organizar
exemplos = ['Computador', 'Carro', 'Casa', 'Nome da Pessoa', 'Valor']

# percorre a lista e escreve cada palavra em um 'arquivo.txt'
with open('exemplos.txt', 'w') as writer:
    for exemplo in exemplos:
        writer.write(exemplos+'\n')
