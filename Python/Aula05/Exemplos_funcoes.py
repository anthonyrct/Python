# Função Simples:

def saudacao(nome):
    return f"Olá, {nome}!"
#Função com Parâmetros Padrão:

def potencia(base, expoente=2):
    return base ** expoente
#Função com Retorno Múltiplo:

def opera_numeros(a, b):
    soma = a + b
    diferenca = a - b
    return soma, diferenca

#exemplo escopo

def exemplo_escopo():
    variavel_local = 10
    print(variavel_local)

exemplo_escopo()  # Saída: 10
#chamando a variavel dentro da função
print(exemplo_escopo)  # Erro: variavel_local não está definida fora da função


#Por exemplo:

def calcular_quadrado(numero):
    return numero ** 2

resultado = calcular_quadrado(5)
print(resultado)  # Saída: 25

#fatorial
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(5)
print(resultado)  # Saída: 120




