# Sistema de Cadastro de Alunos

Este é um sistema simples de cadastro de alunos em Python, que permite adicionar, listar, remover e procurar alunos, além de calcular médias das notas e gerar um diário da turma. O objetivo deste projeto é servir como uma ferramenta educativa para aprendizado de conceitos básicos de programação, manipulação de listas e dicionários, além de cálculos de médias.

## Funcionalidades

1. **Adicionar aluno**
2. **Listar alunos**
3. **Remover aluno**
4. **Procurar aluno por RA**
5. **Listar alunos aprovados**
6. **Listar alunos reprovados**
7. **Procurar aluno por nome**
8. **Calcular e exibir a média da nota B1 de todos os alunos**
9. **Calcular e exibir a média da nota B2 de todos os alunos**
10. **Calcular e exibir a média geral das notas de B1 e B2 de todos os alunos**
11. **Gerar o diário da turma**

## Estrutura do Projeto

- `lista_alunos.py`: Contém a implementação do sistema de cadastro de alunos.
- `README.md`: Este arquivo, que fornece uma visão geral do projeto.

## Como Executar

1. Certifique-se de ter o Python instalado na sua máquina.
2. Clone este repositório ou faça o download dos arquivos.
3. Navegue até o diretório do projeto.
4. Execute o arquivo `lista_alunos.py`:

# Adicionar Aluno
Para adicionar um aluno, selecione a opção 1 e siga as instruções para inserir o nome, RA, nota B1 e nota B2. O nome deve ter no máximo 27 caracteres e o RA no máximo 5 caracteres.

# Listar Alunos
Para listar todos os alunos cadastrados, selecione a opção 2. Esta opção exibirá o RA e o nome de todos os alunos.

# Remover Aluno
Para remover um aluno, selecione a opção 3 e insira o RA do aluno a ser removido. Se o aluno for encontrado, ele será removido do sistema.

# Procurar Aluno por RA
Para procurar um aluno pelo RA, selecione a opção 4 e insira o RA do aluno. Se o aluno for encontrado, suas informações serão exibidas.

# Listar Alunos Aprovados
Para listar apenas os alunos aprovados, selecione a opção 5. Alunos com média maior ou igual a 7 serão considerados aprovados.

# Listar Alunos Reprovados
Para listar apenas os alunos reprovados, selecione a opção 6. Alunos com média menor que 7 serão considerados reprovados.

# Procurar Aluno por Nome
Para procurar um aluno pelo nome, selecione a opção 7 e insira o nome ou parte do nome do aluno. Todos os alunos que correspondem à pesquisa serão exibidos.

# Média da Turma B1
Para calcular e exibir a média das notas de B1 de todos os alunos, selecione a opção 8. Será calculada a média aritmética de todas as notas B1.

# Média da Turma B2
Para calcular e exibir a média das notas de B2 de todos os alunos, selecione a opção 9. Será calculada a média aritmética de todas as notas B2.

# Média da Turma Geral
Para calcular e exibir a média geral das notas de B1 e B2 de todos os alunos, selecione a opção 10. Será calculada a média aritmética das médias individuais de cada aluno.

# Diário da Turma
Para gerar e exibir o diário da turma, selecione a opção 11. Esta opção exibirá uma tabela com o RA, nome, notas B1, B2 e a média de cada aluno, além das médias da turma.

# Sair
Para sair do programa, selecione a opção 0.

```sh
python lista_alunos.py
