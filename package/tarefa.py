class Tarefa:
    def __init__(self, titulo, descricao, prioridade, categoria):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.concluida = False
        self.categoria = categoria

    def marcar_concluida(self):
        self.concluida = True

    def exibir(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"[{status}] {self.titulo} ({self.prioridade}) - {self.categoria.nome}"

class TarefaComSubtarefas(Tarefa):
    def __init__(self, titulo, descricao, prioridade, categoria):
        super().__init__(titulo, descricao, prioridade, categoria)
        self.subtarefas = []

    def adicionar_subtarefa(self, subtarefa):
        self.subtarefas.append(subtarefa)

    def exibir(self):
        texto = super().exibir()
        for sub in self.subtarefas:
            texto += f"\n  - {sub.exibir()}"
        return texto
