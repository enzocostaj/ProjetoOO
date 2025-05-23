# ProjetoOO
# 🗂️ Organizador de Tarefas

Este é um mini projeto desenvolvido em **Python** para gerenciar tarefas pessoais com organização por **prioridade**, **status** e **categorias**. O sistema opera via **terminal** ou com uma **interface gráfica em Tkinter**. Permite realizar operações como cadastro, conclusão e listagem de tarefas, aplicando princípios sólidos de **POO (Programação Orientada a Objetos)**.

Futuramente, pretendo incrementar mais funcionalidades, como filtro por data e melhorias visuais (front-end).

---

## ✅ Funcionalidades

### 🎓 Gerenciamento de Tarefas

- **Cadastrar Tarefa**: Adiciona uma nova tarefa com título, descrição, prioridade e categoria.
- **Cadastrar Subtarefas**: Permite tarefas compostas por subtarefas.
- **Marcar como Concluída**: Atualiza o status da tarefa e subtarefas para concluídas.
- **Listar Tarefas**: Mostra todas as tarefas cadastradas com status e prioridade.

### 🖥️ Interface Gráfica (Tkinter)

- Adicionar tarefas com campos de entrada
- Marcar tarefas como concluídas
- Visualizar lista com status dinâmico

---

## 🧱 Estrutura do Projeto

organizador_tarefas_atualizado/
├── main.py # Interface via terminal
├── README.md
├── package/
│ ├── init.py
│ ├── tarefa.py
│ ├── categoria.py
│ ├── gerenciador.py
│ ├── persistencia.py
│ └── interface.py


---

## 💻 Tecnologias Utilizadas

- **Linguagem**: Python 3.11+
- **Paradigma**: Programação Orientada a Objetos
- **Interface gráfica**: Tkinter
- **Persistência**: Pickle

---

## 🧠 Principais Conceitos de OO Aplicados

- **Encapsulamento**: Organização em classes e pacotes
- **Herança**: `TarefaComSubtarefas` herda de `Tarefa`
- **Composição**: Tarefas possuem categorias e subtarefas
- **Polimorfismo**: `exibir()` tem comportamentos distintos
- **Associação Fraca**: Relacionamento entre `Tarefa` e `Categoria`

---

## ▶️ Como Executar

## Modo Terminal:
python main.py

-----------------------------
1. Adicionar tarefa
2. Listar tarefas
3. Marcar como concluída
4. Sair
-----------------------------
Digite o número da sua escolha: `1`
Título da Tarefa: `Estudar POO`
Descrição da tarefa 'Estudar POO': `Ler capítulo 4`
Prioridade (alta, media, baixa): `alta`
Categoria: `Estudos`
É composta de subtarefas? ('s' ou 'n'): `n`
Tarefa Adicionada com Sucesso!

📅 Projeto Acadêmico
Projeto Livre — Disciplina de Orientação a Objetos
Universidade de Brasília — FCTE
Professor: Henrique Moura
Aluno: Enzo Costa Azevedo Jacundá
