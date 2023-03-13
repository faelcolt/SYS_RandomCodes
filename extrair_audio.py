'''Conversor de vídeo para áudio'''

# essa é a biblioteca que será utilizada para a conversão dos arquivos
# para baixá-la é só abrir o seu terminal e digitar "pip install moviepy"
import moviepy
import moviepy.editor

# coloque seu arquivo aqui:
video = moviepy.editor.VideoFileClip("seu_arquivo") # troque o nome "meu arquivo" para o nome do seu arquivo
audio = video.audio                      # o arquivo precisa estar na mesma pasta do seu script

audio.write_audiofile('seu_arquivo_convertido.mp3')