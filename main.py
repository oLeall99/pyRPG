# Projeto de um RPG em Terminal
"""
A ideia por trás desse projeto orientado a objetos é utilizar conceitos simples de Programação 
para criar um RPG infinito com progressão de personagem e valores aleatórios.
"""

# Import de componentes
from menu import welcome, menu, about, how_play
from game import new_game, load_game


# Mensagem de Entrada da Aplicação:
welcome()


# Lista de funções de menu:
funcoes = new_game, load_game, how_play, about, menu 

# Loop principal do sistema:
while True:
    # O menu retorna a opção escolhida pelo usuário a ser executada, com um valor a menos levando em consideração o index da lista de funçoes
    opcao = menu()

    if opcao == -1: 
        # Encerra o programa caso o usuário escolha a opção 0
        break 
    else:
        funcoes[opcao]()  # Realiza a função do index indicado pela váriavel opcao


# Mensagem de Saida após escolher encerrar o programa:
print("\nEncerrando...")
