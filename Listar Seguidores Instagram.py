'''Lista seus seguidores e não seguidores do Instagram'''

# bibliotecas utilizadas
from datetime import datetime
# abra o terminal e digite: pip install instaloader
import instaloader 

# carrega a biblioteca e faz login com a conta desejada
L = instaloader.Instaloader()
L.login('USUÁRIO', 'SENHA')
# carrega dados de seguidores e seguindo do perfil escolhido
followers = instaloader.Profile.from_username(L.context, 'pycodebr').get.followers()
followees = instaloader.Profile.from_username(L.context, 'pycodebr').get.followees()

# mostra resultados
print('\n')
print('Seguidores: ' + str(followers._data['count']))
print('Seguindo: ' + str(followers._data['count']))
print('\n\n')
print('Lista e informação de seguidores: ')
print('\n')
print(followers._data['edges'])




