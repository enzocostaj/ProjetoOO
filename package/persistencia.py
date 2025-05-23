import pickle

def salvar(dados, arquivo="dados.pkl"):
    with open(arquivo, "wb") as f:
        pickle.dump(dados, f)

def carregar(arquivo="dados.pkl"):
    try:
        with open(arquivo, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []
