import tkinter as tk
from tkinter import messagebox
from package.tarefa import Tarefa
from package.categoria import Categoria
from package import persistencia

class AppInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Tarefas")
        self.tarefas = persistencia.carregar()
        self.categorias = {}

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.label = tk.Label(self.frame, text="Nova Tarefa:")
        self.label.grid(row=0, column=0, columnspan=2)

        tk.Label(self.frame, text="Título:").grid(row=1, column=0)
        self.titulo_entry = tk.Entry(self.frame)
        self.titulo_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Prioridade:").grid(row=2, column=0)
        self.prioridade_entry = tk.Entry(self.frame)
        self.prioridade_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Categoria:").grid(row=3, column=0)
        self.categoria_entry = tk.Entry(self.frame)
        self.categoria_entry.grid(row=3, column=1)

        self.add_btn = tk.Button(self.frame, text="Adicionar", command=self.adicionar_tarefa)
        self.add_btn.grid(row=4, column=0, columnspan=2, pady=5)

        self.lista = tk.Listbox(self.frame, width=50)
        self.lista.grid(row=5, column=0, columnspan=2, pady=5)
        self.atualizar_lista()

        self.concluir_btn = tk.Button(self.frame, text="Marcar como Concluída", command=self.marcar_concluida)
        self.concluir_btn.grid(row=6, column=0, columnspan=2, pady=5)

    def adicionar_tarefa(self):
        titulo = self.titulo_entry.get()
        prioridade = self.prioridade_entry.get()
        nome_cat = self.categoria_entry.get()

        if not titulo or not prioridade or not nome_cat:
            messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
            return

        if nome_cat not in self.categorias:
            self.categorias[nome_cat] = Categoria(nome_cat)

        tarefa = Tarefa(titulo, "", prioridade, self.categorias[nome_cat])
        self.tarefas.append(tarefa)
        persistencia.salvar(self.tarefas)
        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        for i, t in enumerate(self.tarefas):
            self.lista.insert(i, t.exibir())

    def marcar_concluida(self):
        idx = self.lista.curselection()
        if not idx:
            messagebox.showinfo("Seleção", "Selecione uma tarefa.")
            return
        i = idx[0]
        self.tarefas[i].marcar_concluida()
        persistencia.salvar(self.tarefas)
        self.atualizar_lista()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppInterface(root)
    root.mainloop()
