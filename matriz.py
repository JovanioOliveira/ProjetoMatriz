import numpy as np

matrizes = []

while True:
    numLinhas = int(input('Informe o número de Linhas: '))
    numColunas = int(input('Infrome o número de Colunas: '))

    m = []

    for i in range(numLinhas):
        linhas = []
        for j in range(numColunas):
            elemento = int(input(f'm{[i]}{[j]}: '))
            linhas.append(elemento)
        m.append(linhas)
    #np.array. GARANTE QUE A MATRIZ SEJA UMA MATRIZ NA CONFIGURAÇÃO NUMPY
    matrizes.append(np.array(m))                            
    entrada = input('Deseja continuar [S/N]: ').upper()

    if entrada != 'S':
        print(f'As matrizes informadas foram: ')
        for i, matriz in enumerate(matrizes):
            print(f'A matriz na posição {i}: \n{matriz}')
        break
primeiraEntrada = int(input('Informe uma posição para definir MATRIZ A: '))
A = matrizes[primeiraEntrada]
segundaEntrada = int(input('Informe uma posição para definir a MATRIZ B: '))
B = matrizes[segundaEntrada]

print(f'MATRIZ A:\n\n{A}\n\nMATRIZ B:\n\n{B}\n')
