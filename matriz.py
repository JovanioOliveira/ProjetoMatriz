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
    matrizes.append(m)

    entrada = input('Deseja continuar [S/N]: ').upper()
    if entrada != 'S':
        print(f'As matrizes informadas foram: \n{matrizes}')
        break
