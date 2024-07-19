# Projeto de um RPG em Terminal
"""
A ideia por trás desse projeto orientado a objetos é utilizar conceitos simples de Programação 
para criar um RPG infinito com progressão de personagem e valores aleatórios.
"""

# Import de componentes
from colorama import init, Fore, Back, Style


from menu import menu, clear_terminal
from game import new_game, load_game, game
from prints import menu_inicial, welcome, msg_sobre, msg_how_play


# Inicializa o colorama
init(autoreset=True)

# Mensagem de Entrada da Aplicação:
print(welcome)

# Loop principal do sistema:
while True:
    opcao = menu(menu_inicial, 0, 4) # menu() retorna um valor entre o min e max informado escolhido pelo usuáirio, no caso entre 0 e 4

    if opcao == 1 or opcao == 2:
        funcoes_init = new_game, load_game
        heroi = funcoes_init[opcao - 1]()

        if heroi != None:
            game(heroi)
    
    elif opcao == 3 or opcao == 4:
        prints_opc = msg_sobre, msg_how_play
        
        clear_terminal()
        input(Fore.BLUE + prints_opc[opcao - 3])
    else:
        break
    
     


# Mensagem de Saida após escolher encerrar o programa:
input(Fore.BLACK + "\nEncerrando...")
