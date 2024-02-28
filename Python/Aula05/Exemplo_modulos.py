
import math
from datetime import datetime

raiz_quadrada = math.sqrt(25)  # Calcula a raiz quadrada de 25
seno_30_graus = math.sin(math.radians(30))  # Calcula o seno de 30 graus convertidos para radianos


data_atual = datetime.now()  # Obtém a data e hora atual
ano_atual = data_atual.year  # Obtém o ano atual

import Operacoes

resultado_soma = Operacoes.somar(5, 3)
resultado_subtracao = Operacoes.subtrair(10, 4)


import estatisticas

dados = [2, 3, 5, 7, 11, 13, 17]
media = estatisticas.calcular_media(dados)
mediana = estatisticas.calcular_mediana(dados)


