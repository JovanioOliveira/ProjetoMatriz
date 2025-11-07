# 🧮 Projeto Matrizes

## 📘 Descrição do Projeto
O **Projeto Matrizes** tem como objetivo implementar operações matemáticas com matrizes utilizando a linguagem **Python**.  
O sistema permite realizar as seguintes operações de forma modular e testada:

- ➕ **Soma de matrizes**
- ➖ **Subtração de matrizes**
- ✖️ **Multiplicação de matrizes**

O projeto segue uma **estrutura organizada por camadas**, separando os arquivos principais, código-fonte e testes automatizados com `pytest`.

---

## 📂 Estrutura do Projeto

PROJETO_MATRIZES/
│
├── main/
│ └── main_script.py # Arquivo principal (executa o programa)
│
├── src/
│ ├── init.py # Inicializador do pacote
│ └── matriz.py # Implementa as operações com matrizes
│
├── tests/
│ └── test_matriz.py # Testes automatizados das funções do módulo matriz
│
├── .gitignore # Arquivo que ignora caches e arquivos temporários
└── README.md # Este arquivo de documentação

## ⚙️ Pré-requisitos

Certifique-se de ter o **Python 3.11+** instalado.  
Verifique executando o comando:

```powershell
python --version

💡 Caso use o VS Code, selecione o interpretador Python correto (Ctrl + Shift + P → “Python: Select Interpreter”).

🚀 Como Executar o Projeto
1️⃣ Clonar o repositório

Abra o terminal (PowerShell) e execute:

git clone https://github.com/usuario/ProjetoMatriz.git

Depois acesse a pasta do projeto:

cd ProjetoMatriz

2️⃣ Executar o script principal

O arquivo main/main_script.py executa as operações principais com matrizes.
Para rodar o projeto:

python main/main_script.py

🧠 Funcionalidades Principais

O módulo src/matriz.py contém as funções responsáveis pelos cálculos com matrizes.

➕ Soma de Matrizes
resultado = somaMatrizes(matrizA, matrizB)

Condição obrigatória:

As duas matrizes devem ter o mesmo número de linhas e colunas.
Exemplo: A (2x3) + B (2x3) → ✅ possível
Exemplo: A (2x3) + B (3x2) → ❌ não permitido

Retorna uma nova matriz contendo a soma elemento a elemento.

➖ Subtração de Matrizes
resultado = subtracaoMatrizes(matrizA, matrizB)

Condição obrigatória:

As duas matrizes devem ter as mesmas dimensões (mesmo número de linhas e colunas).
Exemplo: A (3x3) - B (3x3) → ✅ permitido
Exemplo: A (2x3) - B (3x2) → ❌ erro

Retorna a diferença entre as duas matrizes, elemento a elemento.

✖️ Multiplicação de Matrizes
resultado = multiplicacaoMatrizes(matrizA, matrizB)

Condição obrigatória:

O número de colunas da matriz A deve ser igual ao número de linhas da matriz B.
Exemplo: A (2x3) × B (3x2) → ✅ possível
Exemplo: A (2x3) × B (2x2) → ❌ não permitido

Retorna uma nova matriz resultante do produto entre A e B.

🧩 Exemplo de Uso
from src.matriz import somaMatrizes, subtracaoMatrizes, multiplicacaoMatrizes

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [1, 2, 3]
]

print("Soma:")
print(somaMatrizes(A, B))

print("Subtração:")
print(subtracaoMatrizes(A, B))

C = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print("Multiplicação:")
print(multiplicacaoMatrizes(A, C))


Saída esperada:

Soma:
[[8, 10, 12], [5, 7, 9]]

Subtração:
[[-6, -6, -6], [3, 3, 3]]

Multiplicação:
[[22, 28], [49, 64]]

🧪 Testes Automatizados

Os testes estão no arquivo tests/test_matriz.py e utilizam o framework pytest.

🔹 Rodar todos os testes

Na raiz do projeto, execute:

pytest -q
ou
pytyon -m pytest

🔹 Rodar um teste específico
pytest tests/test_matriz.py::test_multiplicacaoMatrizes -q

Se todos os testes forem aprovados, você verá algo como:

collected 8 items
tests\test_matriz.py ........ [100%]
8 passed in 0.10s

🧰 Tecnologias Utilizadas

Tecnologia      	Descrição
-------------------------------------------------------------------------
Python 3        	Linguagem principal
Pytest	            Testes automatizados
VS Code	            IDE recomendada
Git / GitHub	    Controle de versão e versionamento remoto
_________________________________________________________________________

🧾 Licença

Este projeto é de uso educacional e acadêmico, desenvolvido para a disciplina Programação Orientada a Objetos (Prof. Jader) no curso de Análise e Desenvolvimento de Sistemas - IFPI (Campus Picos).

👨‍💻 Autor

Desenvolvido por: Jovanio Oliveira
📧 Contato: GitHub - Jovanio Oliveira
