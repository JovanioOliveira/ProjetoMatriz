import pytest
import numpy as np
from src.matriz import matrizes, numeroInteiro, cadastrarMatriz, listarMatrizes, selecionarMatriz, multiplicacaoMatrizes, somaMatrizes, subtracaoMatrizes

# @pytest.fixture
# def setup_matrizes():
#     matrizes.clear()
#     matrizes.append(np.array([[1, 2, 3], [4, 5, 6]]))

# Linha 21  -   Define função de teste usando framework pytest, argumento monkeypatch ( permite alterar o patchear ),
#               patchear (que faz alteração temporaria no código para testar ou mmodificar o comportamento de partes
#               específicas, sem alterar permanentemente o código fonte original.
# Linha 22 -    Cria um contexto de monkeypatching e o 'with' - desfaz as alterações feitas no contexto automatica-
#               mente após a execução do bloco 
# Linha 23 -    Substitui a função input pela função "lambda" definida.( No caso lambda retorna a strin '1')
#               'setattr' - Define o valor de um atributo do objeto
# Linha 24 -    Chama a função 'numeroInteiro' com argumento '1' e verifica se o resultado é igual a 1, se não for
#               retorna falso, e o teste está com erro.
#               'assert' - Verifica se a condição é verdadeira 

def test_numeroInteiro_valido(monkeypatch):         
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _:'1')
        assert numeroInteiro("1") == 1

# Linha 31 -    'raises' faz o gerenciamento para levantar a exceção quando o bloco é executado.
#               Se não levantar a exceção o teste falhará. Se a exceção for levantada o teste
#               o teste é aprovado.

def test_numeroInteiro_invalido():
    with pytest.raises(ValueError):
        numeroInteiro("invalido")

# Linha 38 -    'mocker' - Simula comportamento, 'capsys' - Captura a saída padrão e de erro
# Linha 39 -    Substitui a função input, por uma falsa fornecida pelo mocker. 
#               - Simula a entrada do usuário sem necessidade de entrada manual

def test_cadastrarMatriz(mocker, capsys):
    mocker.patch('builtins.input', side_effect=['2', '3', '1', '2', '3', '4', '5', '6', 'N'])

    cadastrarMatriz()
    captured = capsys.readouterr()
    assert "Matriz(es) cadastradas com sucesso." in captured.out

def test_listarMatrizes(capsys):
    matrizes.clear()
    matrizes.append(np.array([[1, 2, 3], [4, 5, 6]]))
    listarMatrizes()
    captured = capsys.readouterr()
    assert "As Matrizes cadastradas foram:" in captured.out

def test_selecionarMatriz(monkeypatch):
    matrizes.clear()
    matrizes.append(np.array([[1, 2, 3], [4, 5, 6]]))
    monkeypatch.setattr('builtins.input', lambda _: '0')  # Posição 0
    monkeypatch.setattr('builtins.input', lambda _: '0')  # Posição 0
    A, B = selecionarMatriz()
    assert np.array_equal(A, np.array([[1, 2, 3], [4, 5, 6]]))
    assert np.array_equal(B, np.array([[1, 2, 3], [4, 5, 6]]))

def test_multiplicacaoMatrizes(capsys):
    matrizes.clear()
    matrizes.append(np.array([[1, 2, 3], [4, 5, 6]]))
    matrizes.append(np.array([[1, 2], [3, 4], [5, 6]]))
    multiplicacaoMatrizes(matrizes[0], matrizes[1])
    captured = capsys.readouterr()
    assert "A multiplicação entre as MATRIZES A * B" in captured.out

def test_somaMatrizes(capsys):
    matrizes.clear()
    matrizes.append(np.array([[1, 2, 3], [4, 5, 6]]))
    matrizes.append(np.array([[1, 2, 3], [4, 5, 6]]))
    somaMatrizes(matrizes[0], matrizes[1])
    captured = capsys.readouterr()
    assert "O Resultado da SOMA entre as matrizes A + B" in captured.out

def test_subtracaoMatrizes(capsys):
    matrizes.clear()
    matrizes.append(np.array([[1, 2, 3], [4, 5, 6]]))
    matrizes.append(np.array([[1, 2, 3], [4, 5, 6]]))
    subtracaoMatrizes(matrizes[0], matrizes[1])
    captured = capsys.readouterr()
    assert "O Resultado da SUBTRAÇÃO entre as matrizes A - B" in captured.out
    # assert "O Resultado da SUBTRAÇÃO entre as matrize A - B" in captured.out
