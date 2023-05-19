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