import pickle
import os

# Salva um objeto heroi no arquivo "save_pyRPG.pkl"
def save(hero):
    try:
        # Caso tudo ocorra bem retorna uma mensagem de sucesso
        with open('save_pyRPG.pkl', 'wb') as f:
            pickle.dump(hero, f)
        return 1
    
    # Caso receba um erro retorna uma mensagem de erro:
    except Exception as e:
        return e

# Carregar um heroi apartir de um arquivo "save_pyRPG.pkl"
def load():
    save_path = get_save_path()
    if not os.path.exists(save_path):
    # caso não exista arquivo de save
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

def get_save_path():
    # Diretório onde o script está localizado
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Caminho completo para o arquivo de save
    save_path = os.path.join(base_dir, 'save.pkl')
    return save_path