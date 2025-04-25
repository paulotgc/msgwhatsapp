import pywhatkit as kit
from datetime import datetime

# variavel para atualizar a hora
data_atual = datetime.now()

# enviar mensagem automatica depois de 1 minuto
kit.sendwhatmsg('+5583988288483', 'Seja bem vindo(a) ao meu teste de automação do whatsapp com python, essa é uma mensagem texte.',
                data_atual.hour,
                data_atual.minute + 1)


