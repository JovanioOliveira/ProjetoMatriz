import numpy as np

matrizes = []

# Tratamento para inserir número linhas e número de coluna válido

def numeroInteiro(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            if numero <= 0 or numero == -0:
                print('Favor insira um número inteiro maior que zero')
                continue
            return numero
        except ValueError:
            print('Favor insira um número inteiro válido.')

def cadastrarMatriz():

    while True:
        # numLinhas = int(input('Informe o número de Linhas: '))
        # numColunas = int(input('Infrome o número de Colunas: '))

        # Variável recebe a função para certificar que o número de linha e coluna inserido seja um número inteiro e caso
        # e Caso não seja, solicita que seja insrido valor válido#

        numLinhas = numeroInteiro('\nInforme número de Linhas: ')
        numColunas = numeroInteiro('Informe número de Colunas: ')
        print()

        # Definido uma função para tratar erro se caso a entrada de linha e coluna não for um número inteiro

        # if numLinhas <= 0 or numColunas <=0:
        #     print('\nPara gerar uma MATRIZ, inicie inserindo a partir do (Número 1),\n'
        #         'para Número de Linhas e Número de Colunas\n')

        m = []

        for i in range(numLinhas):
            linhas = []
            for j in range(numColunas):
                while True:
                    try:
                        elemento = float(input(f'm{[i]}{[j]}: '))
                        break
                    except ValueError:
                        print('Favor insira um número válido')
                linhas.append(elemento)
            m.append(linhas)

        #np.array. GARANTE QUE A MATRIZ SEJA UMA MATRIZ NA CONFIGURAÇÃO NUMPY
        
        matrizes.append(np.array(m))

        entrada = input('\nDeseja continuar [S/N]: ').upper()
        if entrada != 'S':
            print(f'\nMatriz(es) cadastradas com sucesso.\n')
            break

def listarMatrizes():
        print('As Matrizes cadastradas foram:\n')
        for i, matriz in enumerate(matrizes):
            print(f'A matriz na posição {i}: {matriz.shape} \n{matriz}')

def selecionarMatriz():
    primeiraEntrada = int(input('\nInforme uma posição para definir MATRIZ A: '))
    A = matrizes[primeiraEntrada]
    segundaEntrada = int(input('Informe uma posição para definir  MATRIZ B: '))
    B = matrizes[segundaEntrada]

    A = np.array(A)
    b = np.array(B)

    return A, B

# shape, Utiliza para ver Núm. Linhas e Núm.Colunas de um array, indica o tamanho de cada dimensão da matriz(m,n)
# np.dot, É uma função do numpy para manipulação de array e matrizes. Realiza a multiplicação de matrizes...

# Multiplicação entre as Matrizes

def multiplicacaoMatrizes(A, B):
    if A.shape[1] != B.shape[0]:
        print('\nO Número de colunas da primeira matriz é diferente do número de linhas da segunda matriz\n "A MULTIPLICAÇÃO NÃO É POSSÍVEL"\n')
    else:
        print(f'Matriz A = {A.shape}: \n{A}\n')
        print(f'Matriz B = {B.shape}: \n{B}\n')

        resultado = np.dot(A,B)
        print(f'\nA multiplicação entre as MATRIZES A * B : {resultado.shape} \n{resultado}\n')

# Soma entre as matrizes

def somaMatrizes(A, B):
    if A.shape != B.shape:
        print('\nAs matrizes precisam ter o mesmo número de linhas e colunas para serem somadas')
    else:
        print(f'Matriz A = {A.shape}: \n{A}\n')
        print(f'Matriz B = {B.shape}: \n{B}\n')

        soma = A + B
        print(f'O Resultado da SOMA entre as matrizes A + B: {soma.shape} \n{soma}') 

# Subtração entre as atrizes

def subtracaoMatrizes(A,B):
    if A.shape != B.shape:
        print('\nAs matrizes precisam ter o mesmo níumero de linhas e colunas para serem substraídas')
    else:
        print(f'Matriz A = {A.shape}: \n{A}\n')
        print(f'Matriz B = {B.shape}: \n{B}\n')

        subtracao = A - B
        print(f'O Resultado da SUBTRAÇÃO entre as matrizes A - B: {subtracao.shape} \n{subtracao}')

# Definição de Menu
        
def menu():
    while True:
        print()
        print(10*('=-='))
        print(f'MENU'.center(30))
        print(10*('=-='))

        print('\n1. Cadastrar Matriz')
        print('2. Listar Matrizes')
        print('3. Multiplicação de Matrizes')
        print('4. Soma de Matrizes')
        print('5. Subtração de Matrizes')
        print('6. Encerrar Programa\n')

        print(10*('-=-'))

        esolha = input('\nEscolha uma das opções: ')
        if esolha == '1':
            cadastrarMatriz()
        elif esolha == '2':
            listarMatrizes()
        elif esolha == '3':
            A, B = selecionarMatriz()
            multiplicacaoMatrizes(A, B)
        elif esolha == '4':
            A, B = selecionarMatriz()
            somaMatrizes(A, B)
        elif esolha == '5':
            A, B = selecionarMatriz()
            subtracaoMatrizes(A, B)
        elif esolha == '6':
            print('Programa Encerrado.\n')
            break
        else:
            print('Opção Inválida. Tente novamente')

#CRIADO PASTA MAIN PARA CHAMAR OPÇÕES MENU

# if __name__ == '__main__':
#     menu()

 