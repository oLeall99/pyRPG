import random
from classes import Hero, Weapon, Monster
from menu import clear_terminal
from save import save, load

# Criando um novo personagem
def new_game():
    while True:
        clear_terminal() # Limpeza do Terminal

        # Criação de Personagem:
        print("| -------------------------")
        print("| >>> PYRPG")
        print("| -------------------------")
        print("| !! Criando novo Personagem:")
        
        name = input("| > Nome do Personagem: ")
        opcao = 0
        while True: # Enquanto não escolher uma opção válida permanece no loop
            print("| -------------------------")
            print("| -> Upgrade Inicial:")
            print("|   [1]. Dano # Ataques causam mais dano")
            print("|   [2]. Vida # Aumenta sua vida máxima")
            print("|   [3]. Dex # Aumenta suas chances de esquivar de ataques")
            print("|   [4]. Precisão # Aumenta sua chance de acertar ataques")

            opcao = int(input("| > Escolha: ")) - 1 # Reduz a escolha em um levando em consideração a lista
            
            if opcao < 0 or opcao >= 4:
                print("| > Opção inválida, tente novamente")
            else:
                break
        
        # De acordo com a opção aumenta o valor do status respectivo:
        dano = 1
        vida = 0 
        dex = 1
        accuracy = 2
        if opcao == 0: 
            dano += 2
        elif opcao == 1:
            vida += 2
        elif opcao == 3:
            dex += 1
        else: 
            accuracy += 1
            
        while True: 

            arma1 = Weapon(level=2)
            arma2 = Weapon(level=2)
            arma3 = Weapon(level=2)
            print("| -------------------------")
            print("| -> Arma Inicial:")
            print(f"|   [1]. {arma1.name} {arma1.adj} Dano++: {arma1.damage}")
            print(f"|   [2]. {arma2.name} {arma2.adj} Dano++: {arma2.damage}")
            print(f"|   [3]. {arma3.name} {arma3.adj} Dano++: {arma3.damage}")

            arma_escolhida = int(input("| > Escolha: ")) # Escolha a arma que deseja
            
            if arma_escolhida < 1 or arma_escolhida >= 4:
                print("| > Opção inválida, tente novamente")
            else:
                break
        
        # Adiciona a arma desejada
        armas = []
        if arma_escolhida == 1:
            armas.append(arma1)
        elif arma_escolhida == 2:
            armas.append(arma2)
        else:
            armas.append(arma3)

        clear_terminal() # Limpeza do Terminal
        # Cria um objeto Heroi, com os dados do personagem
        heroi = Hero(name, f'O iniciante', 1, dano, vida, dex, accuracy, armas)
        heroi_save = heroi
        print("| -------------------------")
        print(f"| ! Bem vindo a masmorra {heroi.name}, {heroi.title}")
        print("| -------------------------")
        print("| !! Status:")
        print(f"|   Life: { heroi.life}")
        print(f"|   Dex: {heroi.status['dex']} | Precisão: { heroi.status['accuracy']}")
        print(f"|   Dano: {heroi.status['damage']} + {heroi.arsenal[0].damage} ({heroi.arsenal[0].name})")
        print("| -------------------------")
        
        result = game(heroi) # Passa o objeto para o jogo
        if result == 0:
            break
        elif result == 2:
            while True:
                clear_terminal() # Limpeza do Terminal
                opcao = input("| > Deseja Recomeçar? S/N ")
                if opcao.lower() == 'n':
                    return 0
                elif opcao.lower() == 's':
                    #Reset do Heroi para recomeçar
                    heroi = Hero(name, f'O iniciante', 1, dano, vida, dex, accuracy, armas)
                    game(heroi)
                else:
                    print("| ! Opção inválida, tente novamente")
        else: 
            game(heroi)

def load_game():
    clear_terminal() # Limpeza do Terminal

    # Carregando Personagem:
    print("| -------------------------")
    print("| >>> PYRPG")
    print("| -------------------------")
    print("| !! Carregando Arquivo:")
    print("| -------------------------")
    print("| > OBS:")
    print("| É necessário que tenha um arquivo")
    print("| 'save_pyRPG.pkl' para carregar o")
    print("| personagem")
    print("| -------------------------")
    input("| > Enter ")
    heroi = load()

    if not heroi:
        print("| -------------------------")
        print("| ! Retornando para menu...")
        input("| > Enter ")
    else:
        clear_terminal()
        print("| -------------------------")
        print("| !! Arquivo Carregado!")
        print("| -------------------------")
        input("| > Enter ")

        game(heroi)

    print("| -------------------------")


# Jogo
def game(heroi):
    clear_terminal() # Limpeza do Terminal
    print("| >>> PYRPG")
    print("| -------------------------")
    print("| Em Lucendi existe uma masmorra antiga, a qual diversos ")
    print("| aventureiros e mercenários adentraram em busca de fortuna,") 
    print("| porém ninguém foi capaz de alcançar o seu fim...") 
    print("| será que você é capaz?")
    print("|")
    
    # Caso jogador não queira começar:
    while True:
        opcao = input("| > Entrar? (S/N) ")
        if opcao.lower() == 'n':
            return 0
        elif not opcao.lower() == 's':
            print("| ! Opção inválida, tente novamente")
        else:
            break
    

    # Loop principal do jogo:
    while True:
        andar = heroi.level # Andar Inicial
        clear_terminal() # Limpeza do Terminal
        print("| -------------------------")
        print(f"| >>> {andar}º Andar:")
        print(f"| Vida: {heroi.atual_life} / {heroi.life}")
        print("| -------------------------")
        print("| -> Opções:")
        print("|   [1]. Avançar")
        print("|   [2]. Inventário")
        print("|   [3]. Status")
        print("|   [0]. Voltar")
        try:
            opcao = int(input("| > Escolha: "))
        except ValueError:
            print("| ! Opção inválida, tente novamente")
            
        if opcao > 3 or opcao < 0:
            print("| ! Opção inválida, tente novamente")
        
        elif opcao == 1:
            luck = random.randint(1,20)
            if luck == 20:
                clear_terminal() # Limpeza do Terminal
                print("| ! O Andar esta vazio, você prossegue tranquilamente...")
                print("| -------------------------")
                pause = input("| > Enter ")
            else:
                if not fight(heroi):
                    return 2
                
            heroi.level += 1

        elif opcao == 2: 
            # Abre o inventário do Personagem e altera ele:
            clear_terminal() # Limpeza do Terminal
            heroi.inventory(arsenal = inventory(heroi.arsenal))
                
        elif opcao == 3:
            # Mostra os status do Heroi
            clear_terminal() # Limpeza do Terminal
            status = heroi.status
            arsenal = heroi.arsenal
            print("| -------------------------")
            print("| !! Status:")
            print("| -------------------------")
            print(f"|   Vida: { heroi.life}")
            print(f"|   Dex: {status['dex']} | Precisão: {status['accuracy']}")
            print(f"|   Dano: {status['damage']} + {arsenal[0].damage} ({arsenal[0].name})")
            print("| -------------------------")
            pause = input("| > Enter ")
        else: 
            # Caso jogador queira sair:

            while True:
                clear_terminal() # Limpeza de Terminal
                
                # Salvar Progresso?
                print("| -------------------------")
                opcao = input("| > Salvar Progresso? (S/N) ")
                if opcao.lower() == 'n':
                    print("| -------------------------")

                    while True:

                        # confirmar que não deseja salvar progresso
                        opcao2 = input("| > Certeza? seu progresso será perdido! (S/N) ")
                        if opcao2.lower() == 'n':
                            # cancelar sair sem salvar 
                            break

                        elif opcao2.lower() == 's':
                            # Sair sem salvar
                            return 0
                        
                # Caso escolha uma opção inválida:   
                elif not opcao.lower() == 's':
                    print("| ! Opção inválida, tente novamente")
                else:
                    break
            salvar = save(heroi)
            print("| -------------------------")
            print(salvar)
            print("| -------------------------")
            pause = input("| > Enter ")
            
            if salvar != "| ! Progresso Salvo com Sucesso!!":
                print("| -------------------------")
                print("| ! Voltando para menu...")
                print("| -------------------------")
                pause = input("| > Enter ")
            else:
                break
    return 0

def fight(heroi):
    clear_terminal() # Limpeza do Terminal
    print("| -------------------------")
    print("| ! Você avança pelo andar e...")
    # Cria uma criatura do andar:
    monster = Monster(heroi.level)
    monster_max_life = monster.life
    print(f"| ! encontra um(a) {monster.name} {monster.title}")
    print("| -------------------------")
    print("| !! Status:")
    print(f"|   Dano: {monster.status['damage']} | Vida: { monster.life}")
    print(f"|   Dex: {monster.status['dex']} | Precisão: {monster.status['accuracy']}")
    print("| -------------------------""")
    pause = input("| > Enter ")
    while True:
        # Combate por turnos, cada loop do while é um turno
        
        while True: 
            # Menu de ações:
            clear_terminal() # Limpeza do Terminal
            print("| -------------------------")
            print(f"| ! Combate com {monster.name} {monster.title} {monster.life} / {monster_max_life} :")
            print(f"| Heroi: {heroi.atual_life} / {heroi.life} HP")
            print("| -------------------------")
            print("| -> Opções:")
            print("|   [1]. Atacar")
            print("|   [2]. Inspecionar")
            print("|   [3]. Inventário")
            print("|   [0]. Fugir")
            try:
                option = int(input('| > Escolha: '))
                            # Em caso de escolha inválida:
                if option > 3 or option < 0:
                    print("| -------------------------")
                    print("| ! Opção inválida, tente novamente")
                else: 
                    break
            except ValueError:
                print("| ! Opção inválida, tente novamente")
        
        
        # Caso queira Sair da Masmorra:
        if option == 0:
            clear_terminal() # Limpeza do Terminal
            print("| -------------------------")
            print(f"| !! Sua jornada parou no andar {heroi.level}")
            print("| ! Saindo da Masmorra...")
            print("| -------------------------")
            pause = input("| > Enter ")
        # Caso queira atacar:
        elif option == 1:
            # Função que define aleatoriamente o ataque e retorna True ou False:
            if heroi.attack(monster.status['dex']):

                # Se verdadeiro o ataque acertou!!
                # Remove o dano do héroi da vida do monstro
                monster.life = monster.life - heroi.status['damage'] - heroi.arsenal[0].damage
                
                clear_terminal() # Limpeza do Terminal
                print("| -------------------------")
                print(f"| ! Você acertou {monster.name} {monster.title}!!")
                print(f"| ! Ele está com {monster.life} / {monster_max_life} de Vida.")
                print("| -------------------------")
                pause = input("| > Enter ")
                # Caso a vida do monstro seja igual a menor que zero ele é derrotado
                if monster.life <= 0:
                    # Fim de combate :)

                    clear_terminal() # Limpeza do Terminal
                    print("| -------------------------")
                    print(f"| > O/A {monster.name} {monster.title} foi derrotado(a)")
                    print("| -------------------------")
                    pause = input("| > Enter ")

                    # Aprimorando o herói após vitória
                    while True:

                        if heroi.level % 5 != 0:
                            clear_terminal() # Limpeza do Terminal
                            print("| -------------------------")
                            print("| !!! Você conseguiu um Aprioramento!")
                            print("| -------------------------")
                            print("| -> Opções de Upgrade:")
                            print("|   [1]. Dano # Ataques causam mais dano")
                            print("|   [2]. Dex # Aumenta suas chances de esquivar de ataques")
                            print("|   [3]. Precisão # Aumenta sua chance de acertar ataques")
                            print("|   [4]. Vida # Aumenta sua vida máxima e recupera sua vida")
                            try:
                                opcao = int(input("| > Escolha: ")) - 1 # Reduz a escolha em um levando em consideração a lista
                            except ValueError:
                                print("| > Opção inválida, tente novamente")

                            if opcao < 0 or opcao >= 4:
                                print("| > Opção inválida, tente novamente")
                            else:
                                # Up o heroi de Level
                                heroi.up_level(heroi.level, opcao)

                                status = heroi.status
                                arsenal = heroi.arsenal
                                clear_terminal() # Limpeza do Terminal
                                print("| -------------------------")
                                print("| !! Status Atualizados:")
                                print("| -------------------------")
                                print(f"|   Vida: { heroi.life}")
                                print(f"|   Dex: {status['dex']} | Precisão: {status['accuracy']}")
                                print(f"|   Dano: {status['damage']} + {arsenal[0].damage} ({arsenal[0].name})")
                                print("| -------------------------")
                                pause = input("| > Enter ")
                                break
                        else:

                            arma_nova = Weapon(level=heroi.level + 1)
                            clear_terminal() # Limpeza do Terminal
                            print("| -------------------------")
                            print("| !!! O monstro deixou uma Arma!")
                            print("| -------------------------")
                            print(f"| ! {arma_nova.name} {arma_nova.adj} Dano: {arma_nova.damage}")
                            print("| -------------------------")
                            print("| -> Opções:")
                            print("|   [1]. Pegar")
                            print("|   [2]. Deixar")
                            print("| -------------------------")
                            opcao = int(input("| > Escolha: "))  # Reduz a escolha em um levando em consideração a lista

                            if opcao < 1 or opcao > 2:
                                print("| > Opção inválida, tente novamente")
                            else:
                                # Adiciona a arma ao inventário
                                if opcao == 1:
                                    heroi.add_weapon(arma_nova)
                                    clear_terminal() # Limpeza do Terminal
                                    print("| -------------------------") 
                                    print(f"| !!!{arma_nova.name} {arma_nova.adj} adicionado(a) ao inventário!")
                                    print("| -------------------------")
                                    pause = input("| > Enter ") 
                                break

                    break # Fim do combate
            else:
                # Se falsou o monstro esquivou!
                clear_terminal() # Limpeza do Terminal
                print("| -------------------------")
                print(f"| ! O/A {monster.name} {monster.title} esquivou!!")
                print("| -------------------------")
                pause = input("| > Enter ") 

            # Vez do Monstro Atacar:
            if heroi.dodge(monster.status['accuracy']):    
                # Se retornar True o heroi foi acertado!!
                
                # Reduz a vida do Heroi
                heroi.atual_life -= monster.status['damage']
                clear_terminal() # Limpeza do Terminal
                print("| -------------------------")
                print(f"| ! O/A {monster.name} {monster.title} te acertou!!")
                print(f"| ! Causou {monster.status['damage']} de dano!!")
                print(f"| ! Você está com {heroi.atual_life} / {heroi.life}  de vida restante.")
                print("| -------------------------")
                pause = input("| > Enter ") 
                # Caso a vida chegue a zero:
                if heroi.atual_life <= 0: 

                    # Fim de Run:
                    clear_terminal() # Limpeza do Terminal
                    print("| -------------------------")
                    print(f"| ! O/A {monster.name} {monster.title} te derrotou...")
                    print("| ! Você Perdeu, saindo da masmorra...")
                    print("| -------------------------")
                    pause = input("| > Enter ")
                    return 0 # Retorna para o game que o jogador perdeu
            else:
                # Se falsou o heroi esquivou!
                clear_terminal() # Limpeza do Terminal
                print("| -------------------------")
                print(f"| ! O/A {monster.name} {monster.title} errou!!")
                print("| -------------------------")
                pause = input("| > Enter ")

        elif option == 2:
            # Verifica as informações do monstro:
            clear_terminal() # Limpeza do Terminal
            print("| -------------------------")
            print(f"| !! {monster.name} {monster.title}:")
            print(f"|   Dano: {monster.status['damage']} | Life: {monster.life}")
            print(f"|   Dex: {monster.status['dex']} | Precisão: {monster.status['accuracy']}")
            print("| -------------------------""")
            pause = input("| > Enter ")
            # ! Não é atacado caso queira analisar o monstro, o turno é pulado
        
        elif option == 3:
            # Abre sua Mochila
            heroi.inventory(arsenal = inventory(heroi.arsenal))

            # Vez do Monstro Atacar:
            if heroi.dodge(monster.status['accuracy']):    
                # Se retornar True o heroi foi acertado!!
                # Reduz a vida do Heroi
                heroi.life -= monster.status['damage']
                clear_terminal() # Limpeza do Terminal
                print("| -------------------------")
                print(f"| ! O/A {monster.name} {monster.title} te acertou!!")
                print(f"| ! Causou {monster.status['damage']} de dano!!")
                print(f"| ! Você está com {heroi.life} de vida restante.")
                print("| -------------------------")
                pause = input("| > Enter ")
                # Caso a vida chegue a zero:
                if heroi.life <= 0: 

                    # Fim de Run:
                    clear_terminal() # Limpeza do Terminal
                    print("| -------------------------")
                    print(f"| ! O/A {monster.name} {monster.title} te derrotou...")
                    print("| ! Você Perdeu, saindo da masmorra...")
                    print("| -------------------------")
                    pause = input("| > Enter ")
                    return 0 # Retorna para o game que o jogador perdeu
            else:
                # Se falsou o heroi esquivou!
                clear_terminal() # Limpeza do Terminal
                print("| -------------------------")
                print(f"| ! O/A {monster.name} {monster.title} errou!!")
                print("| -------------------------")
                pause = input("| > Enter ")
            # ! Caso queira trocar de Arma o monstro pode atacar

    return 1 # Retorna para o jogo que o jogador avançou o andar


# Função de Ver o inventário do Heroi:
def inventory(arsenal):

    while True:
        clear_terminal() # Limpeza do Terminal
        print("| -------------------------")
        print(f"| !!! Inventário:")
        print("| -------------------------")
        print(f"| ! Arma Equipada: {arsenal[0].name} {arsenal[0].adj} Dano: {arsenal[0].damage}")
        print("| -------------------------")

        # Lista demais armas do personagem
        if len(arsenal) > 1:
            for count, arma in enumerate(arsenal[1:]): # Le a lista de armas a partir da segunda arma
                print(f"|   [{count + 1}]. {arma.name} {arma.adj} Dano: {arma.damage}")
        else:
            print("| ! Mochila Vazia")
        
        # Pergunta o que o usuário deseja fazer:
        print("| -------------------------")
        print("| -> Opções:")
        print("|   [1]. Equipar Nova Arma")
        print("|   [2]. Jogar Arma Fora")
        print("|   [0]. Voltar")
        opcao = int(input("| > Escolha: "))
        
        if opcao > 2 or opcao < 0:
            print("| ! Opção inválida, tente novamente")
        else:
            
            # Caso queira equipar:
            if opcao == 1:
                if len(arsenal) > 0:
                    while True:
                        print("| -------------------------")
                        print("| -> Qual Arma Equipar?")
                        opcao = int(input("| > Escolha: "))
                        if opcao > len(arsenal) or opcao < 0:
                            print("| ! Opção inválida, tente novamente")
                        else:
                            if opcao == 0:
                                print("| ! Arma Já esta equipada")
                            else:
                                arsenal[0], arsenal[opcao] = arsenal[opcao], arsenal[0] # Troca as armas de posição
                                print("| -------------------------")
                                print(f"| ! {arma.name} {arma.adj} equipado(a)")
                            break
                            # ! Arma 0 sempre será a arma equipada
                else: 
                    print("| ! Não há outra arma para equipar")
            
            # Caso queira deletar uma arma:
            elif opcao == 2:
                if len(arsenal) > 0:
                    while True:
                        print("| -------------------------")
                        print("| -> Qual Arma Deixar?")
                        opcao = int(input("| > Escolha: ")) 
                        if opcao > len(arsenal) or opcao < 0:
                            print("| ! Opção inválida, tente novamente")
                        else:
                            if opcao == 0:
                                print("| ! Não pode remover a arma equipada")
                            else:
                                del arsenal[opcao]
                                print(f"| ! Arma removida")
                            break
                            # ! Arma 0 sempre será a arma equipada
                else: 
                    print("| ! Sua mochila já está vazia")
            else:
                break
    
    return arsenal