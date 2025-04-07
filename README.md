# 🗣️ Sistema de Ouvidoria – `ouvidoria.py`

Este script implementa um sistema simples de ouvidoria que permite registrar, consultar e gerenciar manifestações (reclamações, elogios e sugestões) em um banco de dados MySQL. Ele depende de funções auxiliares do módulo `operacoesbd.py` para interagir com o banco.

## 📦 Requisitos
- Python 3
- MySQL
- Módulo `operacoesbd.py` (responsável por `criarConexao`, `listarBancoDados`, `insertNoBancoDados`, `excluirBancoDados`)
- Banco de dados MySQL com tabela `manifestacoes` contendo pelo menos os campos: `codigo`, `nome`, `tipo`, `descricao`

---

## ⚙️ Funcionalidades e Métodos

### `listarManifestacoes(conn)`
Lista todas as manifestações cadastradas no banco de dados.

---

### `listarManifestacaoPorTipo(conn, tipo)`
Recebe uma query personalizada e lista as manifestações com base no tipo especificado (reclamação, elogio ou sugestão).

---

### `consultarTipo(conn)`
Exibe um menu para o usuário escolher um tipo de manifestação (1: Reclamação, 2: Elogio, 3: Sugestão) e chama `listarManifestacaoPorTipo` com a query apropriada.

---

### `addManifestacao(conn)`
Permite ao usuário registrar uma nova manifestação no sistema. Solicita o nome, tipo e descrição, e insere os dados no banco.

---

### `exibirManifestacoes(conn)`
Consulta e exibe a quantidade de manifestações agrupadas por tipo (ex: 5 reclamações, 3 elogios...).

---

### `pesquisarManifestacao(conn)`
Permite buscar uma manifestação pelo seu código numérico. Se encontrada, exibe o tipo e descrição.

---

### `excluirManifestacao(conn)`
Permite remover uma manifestação informando seu código. Confirma com o usuário antes de realizar a exclusão definitiva.

---

### `encerrarConexao(conn)`
Encerra a conexão com o banco de dados ao final do script.

---

## 🧠 Observações
- A conexão com o banco é criada automaticamente ao iniciar o script, usando o IP, usuário, senha e nome do banco definidos na linha:

  ```python
  conn = criarConexao("127.0.0.1", "usuário", "senha", "BancoDedados")