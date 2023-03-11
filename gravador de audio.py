# essa é a biblioteca que será utilizada para a leitura dos textos
# para baixar é só abrir o seu terminal e digitar "pip install sounddevice"
import sounddevice

from scipy.io.wavefile import write

fs = 44100 # taxa de execução

second = int(input('Digite a duração do tempo em segundos...')) # insira o tempo necessário

print('Gravando...')

gravador_de_voz = sounddevice.rec(int(second * fs) samplerate = fs, channels = 2)