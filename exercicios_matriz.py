# Aqui estão 10 questões sobre matrizes usando a linguagem de programação Python para iniciantes:
#
# Como declarar uma matriz vazia em Python?
# Como preencher uma matriz com valores fornecidos pelo usuário?
# Como exibir uma matriz na forma de tabela?
# Como encontrar o número de linhas e colunas de uma matriz?
# Como acessar um elemento específico em uma matriz?
# Como somar duas matrizes?
# Como multiplicar uma matriz por um escalar?
# Como verificar se duas matrizes são iguais?
# Como encontrar a transposta de uma matriz?
# Como calcular a soma dos elementos de uma matriz?
# Espero que essas questões ajudem você a criar sua lista. Se você precisar de exemplos de código para cada uma delas, é só me dizer!


#Como declarar uma matriz vazia em Python?
matriz = []

# Como preencher uma matriz com valores fornecidos pelo usuário?

linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
        linha.append(valor)
    matriz.append(linha)


# Como exibir uma matriz na forma de tabela?
for linha in matriz:
    for elemento in linha:
        print(elemento, end="\t")
    print()

# Como encontrar o número de linhas e colunas de uma matriz?
num_linhas = len(matriz)
num_colunas = len(matriz[0])  # Assumindo que todas as linhas tenham o mesmo tamanho

# Como acessar um elemento específico em uma matriz?
linha = 0
coluna = 1
elemento = matriz[linha][coluna]


# Como somar duas matrizes?
matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[7, 8, 9], [10, 11, 12]]

soma = []
for i in range(len(matriz1)):
    linha = []
    for j in range(len(matriz1[i])):
        elemento = matriz1[i][j] + matriz2[i][j]
        linha.append(elemento)
    soma.append(linha)

# Como multiplicar uma matriz por um escalar?
escalar = 2
resultado = []
for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[i])):
        elemento = escalar * matriz[i][j]
        linha.append(elemento)
    resultado.append(linha)


# Como verificar se duas matrizes são iguais?
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[1, 2], [3, 4]]

iguais = True
for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        if matriz1[i][j] != matriz2[i][j]:
            iguais = False
            break
    if not iguais:
        break

if iguais:
    print("As matrizes são iguais.")
else:
    print("As matrizes são diferentes.")

# Como encontrar a transposta de uma matriz?
matriz = [[1, 2, 3], [4, 5, 6]]
transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

# Como calcular a soma dos elementos de uma matriz?
soma = 0
for linha in matriz:
    for elemento in linha:
        soma += elemento


# atualizar vetor em python
vetor = [1, 2, 3, 4, 5]
indice = 2
novo_valor = 10

vetor[indice] = novo_valor

print(vetor)


# Esses são exemplos básicos para responder às questões sobre matrizes em Python. Você pode adaptar os códigos
# de acordo com suas necessidades e aprofundar seus conhecimentos na medida em que avança no estudo de