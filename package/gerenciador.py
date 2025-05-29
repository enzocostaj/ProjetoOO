from package.tarefa import Tarefa, TarefaComSubtarefas
from package.categoria import Categoria
from package import persistencia

class GerenciadorTarefas:
    def __init__(self):
<<<<<<< HEAD
        self.tarefas = persistencia.carregar_tarefas()
=======
        self.tarefas = persistencia.carregar()
>>>>>>> 1a2e03fde8e6a3507d701e4ebdc0c421204fdf86
        self.categorias = {}

    def menu(self):
        while True:
<<<<<<< HEAD
            print("\n-----------------------------\n1. Adicionar tarefa\n2. Listar tarefas\n3. Marcar como concluída e remover da lista\n4. Sair\n-----------------------------")
=======
            print("\n-----------------------------\n1. Adicionar tarefa\n2. Listar tarefas\n3. Marcar como concluída\n4. Sair\n-----------------------------")
>>>>>>> 1a2e03fde8e6a3507d701e4ebdc0c421204fdf86
            op = input("Digite o número da sua escolha: ")
            if op == "1":
                self.adicionar_tarefa()
            elif op == "2":
                self.listar_tarefas()
            elif op == "3":
                self.marcar_concluida()
            elif op == "4":
<<<<<<< HEAD
                print("Saindo...")
=======
                persistencia.salvar(self.tarefas)
                print("Salvo e saindo...")
>>>>>>> 1a2e03fde8e6a3507d701e4ebdc0c421204fdf86
                break

    def adicionar_tarefa(self):
        titulo = input("Título da Tarefa: ")
        descricao = input(f"Descrição da tarefa '{titulo}': ")
        prioridade = input("Prioridade (alta, media, baixa): ")
<<<<<<< HEAD
        nome_cat = input("Categoria (Ex: Estudos, Projetos, Atendimentos...): ")
=======
        nome_cat = input("Categoria (Ex: Estudos, Projetos, Atendimentos, Gerências...): ")
>>>>>>> 1a2e03fde8e6a3507d701e4ebdc0c421204fdf86

        if nome_cat not in self.categorias:
            self.categorias[nome_cat] = Categoria(nome_cat)

        categoria = self.categorias[nome_cat]

        subtarefa = input("É composta de subtarefas? ('s' ou 'n'): ").lower()
        if subtarefa == "s":
            tarefa = TarefaComSubtarefas(titulo, descricao, prioridade, categoria)
            while True:
                st = input("Subtarefa (ou Enter para sair): ")
                print("Subtarefa Adicionada com Sucesso!")
                if not st:
                    break
                tarefa.adicionar_subtarefa(Tarefa(st, "", prioridade, categoria))
        else:
            tarefa = Tarefa(titulo, descricao, prioridade, categoria)
            print("Tarefa Adicionada com Sucesso!")

        self.tarefas.append(tarefa)
<<<<<<< HEAD
        persistencia.salvar_tarefa(tarefa)
=======
>>>>>>> 1a2e03fde8e6a3507d701e4ebdc0c421204fdf86

    def listar_tarefas(self):
        for i, tarefa in enumerate(self.tarefas):
            print(f"{i + 1}. {tarefa.exibir()}")

    def marcar_concluida(self):
        self.listar_tarefas()
        try:
<<<<<<< HEAD
            idx = int(input("Número da tarefa a ser removida: ")) - 1
            if 0 <= idx < len(self.tarefas):
                tarefa = self.tarefas[idx]
                tarefa.marcar_concluida()
                
                self.tarefas.pop(idx)
                
                persistencia.remover_arquivo_tarefa(tarefa)  
                
                print("Tarefa removida da lista!")
                
                self.listar_tarefas()
=======
            idx = int(input("Número da tarefa concluída: ")) - 1
            if 0 <= idx < len(self.tarefas):
                tarefa = self.tarefas[idx]
                tarefa.marcar_concluida()
                # Se for uma TarefaComSubtarefas, marcar todas também
                if hasattr(tarefa, "subtarefas"):
                    for sub in tarefa.subtarefas:
                        sub.marcar_concluida()
                print("Tarefa (e subtarefas, se houver) marcada como concluída.")
>>>>>>> 1a2e03fde8e6a3507d701e4ebdc0c421204fdf86
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
<<<<<<< HEAD
=======

>>>>>>> 1a2e03fde8e6a3507d701e4ebdc0c421204fdf86
