# Lista aninhada contendo nomes de cores e seus códigos hexadecimais
cores_e_codigos = [
    ["vermelho", "verde", "azul"],  # Nomes das cores
    ["#FF0000", "#00FF00", "#0000FF"],  # Códigos hexadecimais correspondentes
]

# Encontrar o índice da cor "verde" na primeira sublista
indice_verde = cores_e_codigos[0].index("verde")

# Usar o índice encontrado para acessar o código hexadecimal correspondente na segunda sublista
codigo_hex_verde = cores_e_codigos[1][indice_verde]

print("O código hexadecimal da cor 'verde' é:", codigo_hex_verde)
