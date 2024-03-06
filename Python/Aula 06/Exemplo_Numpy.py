import numpy as np
#array 3x3 vazios
empty_array = np.empty((3,3))
print(empty_array)

#array 2x2 prenchido com 1
ones_arrays = np.ones((2,2))
print(ones_arrays)

#array 4x4 prenchido por 0
zeros_arrays = np.zeros((4,4))
print(zeros_arrays)

#array 3x3 prenchido com random
random_array = np.random.rand(3,3)
print(random_array)

#indexação e seleção:
my_array = np.array([[1, 2, 3] , [4, 5, 6] , [7, 8, 9]])
print(my_array)
print(my_array[1,2])

#valore maximos e minimos
max_value = np.max(my_array)
min_value = np.min(my_array)
print(f"Valor máximo: {max_value}, Valor mínimo: {min_value}")

#soma total
total_sum = np.sum(my_array)
print(f"Soma total: {total_sum}")

#adição de matrizes
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 + matriz2
print("Resultado da adição de matrizes:")
print(resultado)

#subtração de matrizes
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 - matriz2
print("Resultado da subtração de matrizes:")
print(resultado)

#multiplicação de matrizes
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = np.dot(matriz1, matriz2)
# Ou, alternativamente: resultado = matriz1 @ matriz2
print("Resultado da multiplicação de matrizes:")
print(resultado)

# Operações Estatísticas:
# Para calcular a média, mediana e desvio padrão de uma matriz plana, usamos numpy.mean(), numpy.median() e numpy.std().
# Para calcular a soma dos elementos diagonais de uma matriz NumPy, usamos numpy.trace(). Por exemplo:
diagonal_sum = np.trace(my_array)
print(f"Soma diagonal: {diagonal_sum}")


#remove os arrays unidimensionais
squeezed_array = np.squeeze(my_array)
print(squeezed_array)

matriz1 = np.array([[1,2], [3,4]])
matriz2 = np.array([[5,6], [7,8]])

