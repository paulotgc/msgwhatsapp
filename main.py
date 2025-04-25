import pywhatkit as kit
from datetime import datetime

data_atual = datetime.now()

kit.sendwhatmsg('+5583988288483', 'Seja bem vindo(a) ao meu teste de automação do whatsapp com python.',
                data_atual.hour,
                data_atual.minute + 1)