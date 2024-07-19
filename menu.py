# Arquivo de principais prints
"""
Nesse arquivo estão as funções de menu e informações sobre a aplicação, 
para evitar poluição em demais arquivos.
"""
import os
import platform
from colorama import Fore, Back, Style

from prints import menu_inicial, msg_error, menu_andar

def welcome():
    print("\nSeja Bem vindo ao pyRPG!!!\n")

# Sistema de menu de inteiros:
def menu(menu, min, max, without_clear=0):
    while True:
        try:
            if not without_clear: # Caso seja verdadeiro não limpa o terminal
                clear_terminal() # Limpeza do Terminal
            print(Fore.CYAN + menu) # Print do Menu
            opcao = int(input(Fore.CYAN + "| > Escolha:" + Fore.WHITE + " ")) # Escolha do usuário
            print(Fore.CYAN)
            if opcao < min or opcao > max: # Verificação de valor dentro dos limites
                clear_terminal() # Limpeza do Terminal
                input(Fore.RED + msg_error)
            else: 
                return opcao

        except ValueError:  # Em caso de valor inválido
            clear_terminal() # Limpeza do Terminal
            input(Fore.RED + msg_error)

    
# Sistema de menu de Sim ou Não:
def menu_y_n(menu):
    while True:
        try:
            clear_terminal() # Limpeza do Terminal
            opcao = input(Fore.CYAN + menu + Fore.WHITE) # Escolha do usuário
            print(Fore.CYAN)
            # Verificação de Opções:
            if opcao.lower() == 'n': 
                return 0
            elif opcao.lower() == 's' or opcao.lower() == 'y':
                return 1
            else:
                clear_terminal() # Limpeza do Terminal
                input(Fore.RED + msg_error)

        except Exception as e:  # Em caso de valor inválido
            clear_terminal() # Limpeza do Terminal
            print(Fore.RED + "| X ERRO:" + str(e))
            input(Fore.RED + msg_error)

# Print das informações do heroi:
def print_heroi(heroi):
    clear_terminal()
    input(Fore.CYAN + "| ============================= \n| !!" +
          Fore.YELLOW + Style.BRIGHT + f" {heroi.name}, {heroi.title}\n" 
          + Fore.CYAN + Style.NORMAL + 
f"""| =============================
| ! Status:
|   Vitalidade: { heroi.atual_life} / { heroi.life}
|   Precisão: { heroi.accuracy}
|   Dex: {heroi.dex} 
|   Dano: {heroi.damage} + {heroi.arsenal[0].damage} (Arma)
|   Arma: {heroi.arsenal[0].name} {heroi.arsenal[0].adj} 
| =============================
| > Enter """)
    
    return 3

def print_monster(monster):
    clear_terminal()
    input( Fore.CYAN + "| =============================\n| !!" 
        +  Fore.RED + Style.BRIGHT + f" {monster.name}, {monster.title}\n"
        + Fore.CYAN + Style.NORMAL +
f"""| =============================
| ! Status:
|   Vitalidade: { monster.atual_life} / { monster.life}
|   Precisão: { monster.accuracy}
|   Dex: {monster.dex} 
|   Dano: {monster.damage}
| =============================
| > Enter """)
    return None
        
# Limpeza do terminal
def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def result_print(res, monster, heroi):
    if res == 0:
        # O monstro esquivou!
        clear_terminal() # Limpeza do Terminal
        input(Fore.CYAN + "| ===================================================\n"
            + "| !! O/A " + Fore.RED + f"{monster.name} {monster.title} " + Fore.CYAN + "esquivou!!\n" 
            + "| ===================================================\n" 
            + "| > Enter "
        )
    elif res == 1:
        # O monstro foi acertado!
        clear_terminal() # Limpeza do Terminal
        input(Fore.CYAN+"| ===================================================\n"
            + "| !! " + Fore.YELLOW + f"{heroi.name}" + Fore.CYAN + " acertou " +  Fore.RED + f"{monster.name} {monster.title}!!\n" + Fore.CYAN
            + f"| ! Vida: {monster.atual_life} / {monster.life}\n"
            + "| ===================================================\n" 
            + "| > Enter "
        )

def result_print2(res, monster, heroi):
    if res == 0: 
        # O monstro Errou!
        clear_terminal() # Limpeza do Terminal
        input(Fore.CYAN+"| ===================================================\n"
            + "| !! O/A " + Fore.RED + f"{monster.name} {monster.title} " + Fore.CYAN + "Errou!!\n" 
            + "| ===================================================\n" 
            + "| > Enter "
        )
    elif res == 1: 
        # O monstro Acertou!
        clear_terminal() # Limpeza do Terminal
        input(Fore.CYAN+ "| ===================================================\n" 
            + "| !! O/A " + Fore.RED + f" {monster.name} {monster.title} " + Fore.CYAN + "acertou" + Fore.YELLOW + f" {heroi.name}!!\n" 
            + Fore.CYAN + f"| ! Causou {monster.damage} de Dano!\n"
            + "| ! " + Fore.YELLOW + f"{heroi.name}" + Fore.CYAN + f" está com {heroi.atual_life} / {heroi.life} de Vida!\n"
            + "| ===================================================\n" 
            + "| > Enter "
        )

def death(res, monster, heroi):
    if not res: 
        # O Heroi perdeu!
        clear_terminal() # Limpeza do Terminal
        input(Fore.CYAN+"| ===================================================\n" + Fore.RED
            + "| !! O/A " + Fore.RED + f"{monster.name} {monster.title} " + Fore.CYAN + "derrotou" + Fore.YELLOW + f" {heroi.name}!!\n" + Fore.CYAN
            + "| ===================================================\n" 
            + "| > Enter "
        )

        clear_terminal() # Limpeza do Terminal
        input(Fore.CYAN + "| ============================\n"
            + "| !! Saindo da Masmorra...\n"
            + "| ============================\n" 
            + "| > Enter "
        )
    else:
        # O monstro foi Derrotado!
        clear_terminal() # Limpeza do Terminal
        input(Fore.CYAN+"| ===================================================\n"
            + "| !!" + Fore.YELLOW + f" {heroi.name}" + Fore.CYAN + " derrotou " + Fore.RED + f"{monster.name} {monster.title}!!\n" + Fore.CYAN
            + "| ===================================================\n" 
            + "| > Enter "
        ) 