import random

my_vector = [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]
             ]
print("tipo:", type(my_vector))
print("tamanho:", len(my_vector))

# print(my_vector)
# print(my_vector[0])
# print(my_vector[4])

for lista in my_vector:
    for item in lista:
        if item == 4:
            print('a', item)


for lista in my_vector:
    for item in lista:
        if item == 4:
            print('b', item)
        elif (item % 2) == 0:
            print(f'Número {item} é par')

def mmatriz(n, m):
    # n = int(input("Digite n: "))
    # m = int(input("Digite m: "))
    matriz = []

    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(random.randint(0, 10))
        matriz.append(linha)


    # print(matriz)
    tamanho = len(matriz)
    resto = tamanho % 2
    indice_par = (tamanho // 2) - 1
    indice_impar = (tamanho // 2)
    if resto == 0:
        print(indice_par)
        print('Meio da matriz', matriz[indice_par])
    else:
        print(indice_impar)
        print('Meio da matriz', matriz[indice_impar])

mmatriz(101, 101)