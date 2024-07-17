import pickle
import os

# Salva um objeto heroi no arquivo "save_pyRPG.pkl"
def save(hero):
    try:
        # Caso tudo ocorra bem retorna uma mensagem de sucesso
        with open('save_pyRPG.pkl', 'wb') as f:
            pickle.dump(hero, f)
        return "| ! Progresso Salvo com Sucesso!!"
    
    # Caso receba um erro retorna uma mensagem de erro:
    except Exception as e:
        return f"Erro ao salvar o objeto: {e}"

# Carregar um heroi apartir de um arquivo "save_pyRPG.pkl"
def load():
    # caso não exista arquivo de save
    if not os.path.exists("save_pyRPG.pkl"):
        print("| ! Não foi possível carregar save: o arquivo 'save_pyRPG.pkl' não existe.")
        return None
    
    try:
        with open("save_pyRPG.pkl", 'rb') as f:
            return pickle.load(f)
            # caso tudo ocorra bem retorna o objeto heroi

    # Caso receba um erro ao carregar:       
    except (pickle.PickleError, EOFError) as e:
        print(f"| ! Erro ao carregar o objeto: {e}")
        return None
    
    # Caso receba um outro tipo de erro:
    except Exception as e:
        print(f"| ! Erro inesperado: {e}")
        return None

