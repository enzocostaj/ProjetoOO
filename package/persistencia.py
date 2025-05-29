import os
import json
from package.categoria import Categoria
from package.tarefa import Tarefa

def garantir_pasta_tarefas():
    if not os.path.exists("tarefas"):
        os.mkdir("tarefas")

def salvar_tarefa(tarefa):
    garantir_pasta_tarefas()
    nome_arquivo = f"tarefas/{tarefa.titulo.replace(' ', '_')}.json"

    tarefa_dict = {
        'titulo': tarefa.titulo,
        'descricao': tarefa.descricao,
        'prioridade': tarefa.prioridade,
        'concluida': tarefa.concluida,
        'categoria': tarefa.categoria.nome
    }

    with open(nome_arquivo, 'w') as f:
        json.dump(tarefa_dict, f)

def carregar_tarefas():
    tarefas = []
    garantir_pasta_tarefas()
    for nome_arquivo in os.listdir("tarefas"):
        if nome_arquivo.endswith(".json"):
            with open(f"tarefas/{nome_arquivo}", "r") as f:
                tarefa_dict = json.load(f)
                categoria = Categoria(tarefa_dict['categoria'])
                tarefa = Tarefa(tarefa_dict['titulo'], tarefa_dict['descricao'], tarefa_dict['prioridade'], categoria)
                tarefa.concluida = tarefa_dict['concluida']
                tarefas.append(tarefa)
    return tarefas

def remover_arquivo_tarefa(tarefa):
    nome_arquivo = f"tarefas/{tarefa.titulo.replace(' ', '_')}.json"
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
