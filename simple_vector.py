import random

# Criar vertor
vet1 = []

# Criar vetor com dados

vet2 = [[1, 2, 3], [4, 5, 6]]
# print(vet2)


# Criar vetor com dados de vários tipos

vet22 = [["UNIESP", 2, True], [4.61, "SI", 6]]
# print(vet22)

# Exibir os dados de um vetor separadamente
# print(vet2[0])
# print(vet2[0][0])
# print(vet2[0][1])
# print(vet2[0][2])

# print(vet2[1])
# print(vet2[1][0])
# print(vet2[1][1])
# print(vet2[1][2])

# Listar os dados de um matriz

# vet3 = [[1, 2, 3], [4, 5, 6]]
# for elemento in vet3:
    # print(elemento)
    # for item in elemento:
        # print(item)

# Adicionar nova lista ao matriz

vet4 = [[1, 2, 3], [4, 5, 6]]
# print(vet4)

new_lista = [7, 8, 9]
vet4.append(new_lista)
# print(vet4)


# Removendo uma lista da matriz

# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matriz)
# indice = 1  # Índice da lista a ser removida
# lista_removida = matriz.pop(indice)

# print(matriz)  # Matriz sem a lista removida
# print(lista_removida)  # Lista removida


# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matriz)

# indice = 2  # Índice da lista a ser removida
# del matriz[indice]
# print(matriz)  # Matriz sem a lista removida



# Atualizar vetor em python

vetor = [[1, 2, 3], [4, 5, 6]]
# print(vetor)

indice = 1

novo_valor = [7, 8, 9]
# print(novo_valor)

vetor[indice] = novo_valor
# print(vetor)

# Atividades

# Criar uma matriz a partir de uma entrada


# matriz = []
#
# linha = []
# print(linha)
#
# linha.append(random.randint(0, 10))
# print(linha)
# matriz.append(linha)


# Como listar uma matriz em forma de tabela

# matriz = [[1,2,3], [4,5,6]]
# matriz = [[1,2,3, 4,5,6], [7, 8, 9, 10, 11, 12]]
#
# for linha in matriz:
#     for elemento in linha:
#         print(elemento, end="\t")
#     print()


# Como preencher uma matriz com valores fornecidos pelo usuário?

linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))
# print(range(linhas))

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t")
    print()



