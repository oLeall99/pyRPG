import random
from colorama import Fore

from classes import Hero, Weapon, Monster
from menu import *
from save import *
from prints import *

# Criando um novo Personagem
def new_game():
    while True:
        try:
            clear_terminal() # Limpeza do Terminal

            # Criação de Personagem:        
            name = input(Fore.CYAN + msg_create_heroi_name + Fore.WHITE)
            option = menu(msg_upgrades, 1, 4)

            # De acordo com a opção aumenta o valor do status respectivo:
            status = [ 3, 2, 2, 5 ] # Dano, Dex, Accuracy, Life

            if option == 1: # Dano
                status[0] += 2

            elif option == 2 or option == 3: # Dex e Precisão
                status[option - 1] += 2

            elif option == 4: # Vida
                status[3] += 5

            # Definido Arma inicial
            armas = [ Weapon(level=2), Weapon(level=2), Weapon(level=2) ]
            msg_armas = f"""| =============================
| -> Arma Inicial:
|   [1]. {armas[0].name} {armas[0].adj} dano++: {armas[0].damage}
|   [2]. {armas[1].name} {armas[1].adj} dano++: {armas[1].damage}
|   [3]. {armas[2].name} {armas[2].adj} dano++: {armas[2].damage}
| ============================="""
        
            # Adiciona a arma desejada
            arma_escolhida = menu(msg_armas, 1, 3)
            arsenal = [armas[arma_escolhida - 1] ]

            del armas
            # Cria um objeto Heroi, com os dados do personagem
            heroi = Hero(name, f'O iniciante', 1, damage=status[0], dex=status[1], accuracy=status[2], hp=status[3] ,arsenal=arsenal)

            print_heroi(heroi)

            break

        except Exception as e: # Caso tenha algum erro:
            clear_terminal()   # Limpeza do Terminal
            print(Fore.RED + "| X ERRO: " + str(e))
            input(Fore.RED + "| x Erro ao Criar Herói, Tente Novamente.")
    
    # Retorna o heroi criado em caso de sucesso
    return heroi

# Carregar um Personagem
def load_game():
    try: 
        clear_terminal() # Limpeza do Terminal

        # Carregando Personagem:
        input(Fore.CYAN + msg_load_game)
        heroi = load()

        clear_terminal()
        if not heroi:
            input(Fore.RED + msg_load_error)
            return None
        else:
            input(Fore.CYAN + msg_load_sucess)

            return heroi


    except Exception as e:
            clear_terminal()   # Limpeza do Terminal
            print(Fore.RED + "| X ERRO: " + str(e))
            input(Fore.RED + "| x Erro ao Carregar Herói, Tente Novamente.")
            return None


# Jogo
def game(heroi):
    clear_terminal() # Limpeza do Terminal
    entrar =  menu_y_n(msg_game_intro)
    
    # Não deseja entrar no jogo
    if not entrar:
        return heroi
    

    # Loop principal do jogo:
    while True:
        option = menu("| =============================\n" + f"| >>> {heroi.level}º Andar:\n" + 
        "| Vida: " + Fore.GREEN + f"{heroi.atual_life}" + Fore.CYAN + " / " + Fore.GREEN +  f"{heroi.life}" 
        + Fore.CYAN + menu_andar, 0, 3)
        
        # Realiza a opção desejada:
        if option == 0:
            # Caso jogador queira sair:
            salvar = menu_y_n(ask_save_progress)

            # Caso Não Queira Salvar:
            if not salvar:
                salvar = menu_y_n(ask_save_progress_again)

                if salvar:
                    return None            
            
            # Caso Queira Salvar:
            else:
                try:
                    # Salva Progresso:
                    salvando = save(heroi)
                    clear_terminal() # Limpeza do Terminal
                    if salvando:
                        input(Fore.CYAN + save_sucess)
                    else:
                        input( Fore.RED + msg_line + str(salvando) + msg_enter)

                except Exception as e: # Erro ao Salvar
                    clear_terminal()   # Limpeza do Terminal
                    print(Fore.RED + "| X ERRO: " + str(e))
                    input(Fore.RED + "| x Erro ao Salvar Herói, Tente Novamente.")
                    break
                
                # Retorna para menu inicial
                return None

        else:
            # Faz demais ações:
            funcoes = combat, inventory, print_heroi
            
            action = funcoes[option - 1](heroi)
            if action == True:    
                if heroi.level % 5 != 0:
                    # Upgrade de Status em andares não múltiplos de 5
                    upgrade = menu(msg_upgrades, 1, 4)
                    heroi.up_level(heroi.level, upgrade)
                    print_heroi(heroi)
                else:
                    new_arma = Weapon(level=heroi.level)
                    arma_nova = menu(monster_weapon +
                                    f"| ! {new_arma.name} {new_arma.adj} dano++: {new_arma.damage}"
                                    + menu_new_weapon, 0, 1
                                )
                    
                    if arma_nova:
                        heroi.add_weapon(new_arma)
                        input(Fore.CYAN + "| ==========================================\n| ! " + Fore.YELLOW
                                + f"{new_arma.name} {new_arma.adj} Adicionado a mochila!\n" + Fore.CYAN
                                + "| =========================================="
                        )
                    else: 
                        del new_arma
                
                if action != 3:            
                    heroi.level += 1
                    if heroi.level % 10 == 0:
                        heroi.atul_life = heroi.life

            elif not action:
                again = menu_y_n(go_again)

                if not again:
                    break 
                else:
                    heroi.reset()


    return 0

def combat(heroi):
    # Define se terá monstro no andar ou não:
    luck = random.randint(1,20)
    if luck == 20: # Se valor igual a 20 sem monstro
        clear_terminal()
        input(msg_empty_level)
        return 20
    
    else:
        # Cria uma criatura do andar:
        monster = Monster(heroi.level)
        print_monster(monster)
    while True:
        # Combate por turnos, cada loop do while é um turno
        
        while True: 
            # Menu de ações:
            option = menu("| =============================\n| !!" + 
                        Fore.RED + Style.BRIGHT + 
                        f" {monster.name} {monster.title} {monster.atual_life} / {monster.life}" + Fore.CYAN + Style.NORMAL + ":\n" + 

                        f"| ! Herói: " + Fore.GREEN + f"{heroi.atual_life}" + Fore.CYAN + " / " + Fore.GREEN +  f"{heroi.life}" 
                        + Fore.CYAN + fight_menu, 0, 3
                    )
            
            # Caso Queira Sair da Masmorra
            if option == 0:
                clear_terminal()
                input("| =============================\n" 
                      + f"| !! Sua jornada parou no andar {heroi.level}\n"
                      + "| ! Saindo da Masmorra... \n" + "| =============================\n" 
                      + "| > Enter "
                )
                return 2
            
            elif option == 1:

                attack = heroi.attack(monster.dex)
                dodge = heroi.dodge(monster.accuracy)
                if heroi.dex >= monster.dex:

                    # Heroi Ataca
                    result_attack = attack_time(monster, attack, heroi.damage + heroi.arsenal[0].damage) # Heroi Ataca
                    result_print(result_attack, monster, heroi) # Print do Resultado
                    
                    # Caso Monstro seja Derrotado
                    if monster.atual_life <= 0:
                        # Fim de Combate :)
                        death(1, monster, heroi)
                        return True
                    
                    # Monstro Ataca
                    result_dodge = dodge_time(heroi, dodge, monster.damage) # Heroi Esquiva
                    result_print2(result_dodge, monster, heroi)

                    if heroi.atual_life <= 0:
                        # Fim de Combate :(
                        death(0, monster, heroi)
                        return False
                else:
                    # Monstro Ataca
                    result_dodge = dodge_time(heroi, dodge, monster.damage) # Heroi Esquiva
                    result_print2(result_dodge, monster, heroi)
                    
                    # Caso Heroi seja Derrotado
                    if heroi.atual_life <= 0:
                        # Fim de Combate :(
                        death(0, monster, heroi)
                        return False
                    
                    # Heroi Ataca
                    result_attack = attack_time(monster, attack, heroi.damage + heroi.arsenal[0].damage) # Heroi Ataca
                    result_print(result_attack, monster, heroi)

                    # Caso Monstro seja Derrotado
                    if monster.atual_life <= 0:
                        # Fim de Combate :)
                        death(1, monster, heroi)
                        return True
            
            # Print dos status do monstro
            elif option == 2:
                print_monster(monster)
            
            # Inventário
            else:
                heroi.arsenal = inventory(heroi)

# Função de Ver o inventário do Heroi:
def inventory(heroi):
    while True:
        clear_terminal() # Limpeza do Terminal
        print(Fore.CYAN + msg_inventory
               + f"| ! Arma Equipada: {heroi.arsenal[0].name} {heroi.arsenal[0].adj} Dano: {heroi.arsenal[0].damage}\n"
               + "| =========================="
        )

        # Lista demais armas do personagem
        if len(heroi.arsenal) > 1:
            for count, arma in enumerate(heroi.arsenal[1:]): # Le a lista de armas a partir da segunda arma
                print(f"|   [{count + 1}]. {arma.name} {arma.adj} Dano: {arma.damage}")
        else:
            print("| ! Mochila Vazia")

        opcao = menu(Fore.CYAN + menu_inventory, 0, 2, 1)
            
        # Caso queira equipar:
        if opcao == 1:
            if len(heroi.arsenal) > 0:

                arma_nova = menu(menu_arma, 0, len(heroi.arsenal), 1)
                if arma_nova != 0:
                    # ! Arma 0 sempre será a arma equipada
                    heroi.arsenal[0], heroi.arsenal[arma_nova] = heroi.arsenal[arma_nova], heroi.arsenal[0] # Troca as armas de posição
                    print("| ==========================\n"
                          + f"| ! {arma.name} {arma.adj} equipado(a)!"
                          + "| =========================="
                    )
            else: 
                print("| ! Não há outra arma para equipar")
            
        # Caso queira deletar uma arma:
        elif opcao == 2:
            if len(heroi.arsenal) > 0:

                arma_del = menu(menu_arma_del, 0, len(heroi.arsenal), 1)
                if arma_del != 0:
                    del heroi.arsenal[opcao]
                    print("| ==========================\n"
                          + f"| ! Arma Removida!"
                          + "| =========================="
                    )
            else: 
                print("| ! Sua mochila já está vazia")
        else:
            break
        
    return 3

# Função de Comparar Ataque
def attack_time( persona, attack, dano):
    # Persona é Atacado:
    if attack:
        persona.atual_life = persona.atual_life - dano
        # Personagem foi acertado
        return 1
    
    # Persona Desvia:
    else:
        return 0
        
# Função de Comparar Desvio
def dodge_time(persona, dodge, dano):
    # Persona É Atacado
    if dodge:
        # Personagem Desvia
        return 0
    else:
        # Personagem foi acertado 
        persona.atual_life = persona.atual_life - dano
        return 1
        