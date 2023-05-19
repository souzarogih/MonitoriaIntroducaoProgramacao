'''Criar função que exibe um teclado de pinpad digital'''


def pinpad_matriz():
    matriz = [
        [[1, 'ABC'], [2, 'DEF'], [3, 'GHI']],
        [[4, 'JKL'], [5, 'MNO'], [6, 'PQR']],
        [[7, 'TUV'], [8, 'WXY'], [9, '*#-']],
        [["FUNC"], [0, ''], ["ALPHA"]]
        ]

    for linha in matriz:
        for elemento in linha:
            print(elemento, end="\t")
        print()


'''Criar funções para gerenciar uma matriz, toda manipulação dos dados da matriz devem ser feitas através das funções'''
# matriz_data = []
matriz_data = [[1, 2], [3, 4]]


def exibe_dados_da_matriz(data, posicao):
    '''Funçã para exibir dados da matriz'''
    if posicao == 1:
        print(data[0])
        print(data[0][0])
        print(data[0][1])
    elif posicao == 2:
        print(data[1])
        print(data[1][0])
        print(data[1][1])
    else:
        print("Posição não encontrada")

# exibe_dados_da_matriz(matriz_data, 2)


def listar_todos_os_dados_da_matriz(data, pretty):
    '''Função para listar todos os dados da matriz'''

    if pretty == True:
        for linha in data:
            for elemento in linha:
                print(elemento, end="\t")
            print()
    else:
        for elemento in data:
            print(elemento)

# listar_todos_os_dados_da_matriz(matriz_data, True)


def add_dado_in_matriz(data, add_lista):
    '''Função para adicionar nova lista ao matriz'''

    print(f"Dados para adicionar: {add_lista}")
    print(f"Dados atuais {data}")
    data.append(add_lista)
    print(f"Nova Matriz com dados : {data}")


# add_dado_in_matriz(matriz_data, [10, 20])

def remove_data_in_matriz(data, posicao):
    '''Função para removendo uma lista da matriz'''

    print("Dados atuais:", data)
    print("Removendo os elementos do indice ", posicao)
    lista_removida = data.pop(posicao)
    print("Elementos removidos: ", lista_removida)
    print('Matriz atual: ', data)

# remove_data_in_matriz(matriz_data, 1)


def update_data_in_matriz(data, posicao, add_lista):
    '''Função para atualizar vetor em python'''

    print(f'Matriz atual: {data}')
    print(f'Indice que será atualizado: {posicao}')
    print(f'Elementos que serão inseridos: {add_lista}')

    data[posicao] = add_lista
    print('Matriz atualizada: ', data)


# update_data_in_matriz(matriz_data, 1, [30, 40])
