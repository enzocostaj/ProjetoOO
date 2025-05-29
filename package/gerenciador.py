from package.tarefa import Tarefa, TarefaComSubtarefas
from package.categoria import Categoria
from package import persistencia

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = persistencia.carregar_tarefas()
        self.categorias = {}

    def menu(self):
        while True:
            print("\n-----------------------------\n1. Adicionar tarefa\n2. Listar tarefas\n3. Marcar como concluída\n4. Sair\n-----------------------------")
            op = input("Digite o número da sua escolha: ")
            if op == "1":
                self.adicionar_tarefa()
            elif op == "2":
                self.listar_tarefas()
            elif op == "3":
                self.marcar_concluida()
            elif op == "4":
                print("Saindo...")
                break

    def adicionar_tarefa(self):
        titulo = input("Título da Tarefa: ")
        descricao = input(f"Descrição da tarefa '{titulo}': ")
        prioridade = input("Prioridade (alta, media, baixa): ")
        nome_cat = input("Categoria (Ex: Estudos, Projetos, Atendimentos...): ")

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
        persistencia.salvar_tarefa(tarefa)

    def listar_tarefas(self):
        for i, tarefa in enumerate(self.tarefas):
            print(f"{i + 1}. {tarefa.exibir()}")

    def marcar_concluida(self):
        self.listar_tarefas()
        try:
            idx = int(input("Número da tarefa concluída: ")) - 1
            if 0 <= idx < len(self.tarefas):
                tarefa = self.tarefas[idx]
                tarefa.marcar_concluida()
                
                self.tarefas.pop(idx)
                
                persistencia.remover_arquivo_tarefa(tarefa)  
                
                print("Tarefa marcada como concluída e removida.")
                
                self.listar_tarefas()
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
