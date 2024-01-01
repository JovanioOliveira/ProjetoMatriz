import numpy as np

matrizes = []

while True:
    numLinhas = int(input('Informe o número de Linhas: '))
    numColunas = int(input('Infrome o número de Colunas: '))

    if numLinhas <= 0 or numColunas <=0:
        print('\nPara gerar uma MATRIZ, inicie inserindo a partir do (Número 1),\n'
              'para Número de Linhas e Número de Colunas\n') 

    m = []

    for i in range(numLinhas):
        linhas = []
        for j in range(numColunas):
            elemento = float(input(f'm{[i]}{[j]}: '))
            linhas.append(elemento)
        m.append(linhas)

    #np.array. GARANTE QUE A MATRIZ SEJA UMA MATRIZ NA CONFIGURAÇÃO NUMPY
    
    matrizes.append(np.array(m))                            
    entrada = input('\nDeseja continuar [S/N]: ').upper()

    if entrada != 'S':
        print(f'\nAs matrizes informadas foram: ')
        for i, matriz in enumerate(matrizes):
            print(f'A matriz na posição {i}: {matriz.shape} \n{matriz}')
        break
primeiraEntrada = int(input('\nInforme uma posição para definir MATRIZ A: '))
A = matrizes[primeiraEntrada]
segundaEntrada = int(input('Informe uma posição para definir  MATRIZ B: '))
B = matrizes[segundaEntrada]

# shape, Utiliza para ver Núm. Linhas e Núm.Colunas de um array, indica o tamanho de cada dimensão da matriz(m,n)
# np.dot, É uma função do numpy para manipulação de array e matrizes. Realiza a multiplicação de matrizes...

# Multiplicação entre as Matrizes

# if A.shape[1] != B.shape[0]:
#     print('\nO Número de colunas da primeira matriz é diferente do número de linhas da segunda matriz\n "A MULTIPLICAÇÃO NÃO É POSSÍVEL"\n')
# else:
#     resultado = np.dot(A,B)
#     print(f'\nA multiplicação entre as MATRIZES A * B : {resultado.shape} \n{resultado}\n')

# Soma entre as matrizes

# if A.shape != B.shape:
#     print('\As matrizes precisam ter o mesmo número de linhas e coluans para serem somadas')
# else:
#     soma = A + B
#     print(f'O Resultado da SOMA entre as matrizes A + B: \n{soma}') 

# Subtração entre as atrizes

if A.shape != B.shape:
    print('\nAs matrizes precisam ter o mesmo níumero de linhas e colunas para serem substraídas')
else:
    subtracao = A - B
    print(f'O Resultado da SUBTRAÇÃO entre as matrizes A - B: \n{subtracao}')


   