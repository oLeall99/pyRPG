# Arquivo de principais prints
"""
Nesse arquivo estão as funções de menu e informações sobre a aplicação, 
para evitar poluição em demais arquivos.
"""
import os
import platform

def welcome():
    print("\nSeja Bem vindo ao pyRPG!!!\n")

def menu():
    # Sistema de menu:
    while True:
        clear_terminal() # Limpeza do Terminal
        print("| -------------------------")
        print("""| >>> PYRPG
| -------------------------
| -> Opções:
|   [1]. Novo Jogo
|   [2]. Carregar Jogo
|   [3]. Como Jogar?
|   [4]. Sobre o Projeto
|   [0]. Sair""")

        # O usuário escolhe a opção dejesada
        opcao = int(input("| Escolha: "))
        if opcao > 4 or opcao < 0:
            # caso seja inválido será pedido que refaça a escolha:
            print("| > Opção inválida, tente novamente")
            print("| -------------------------")
        else:
            # caso seja válida será retornado o número da função da respectiva escolha:
            print("| -------------------------")
            opcao = opcao - 1
            return opcao

def about():
    clear_terminal() # Limpeza do Terminal
    # Descrição breve sobre o objetivo e motivações por trás do projeto
    print("| -------------------------")
    print("""| >>> PYRPG
| -------------------------
| PYRPG é um projeto de jogo RPG com progressão infinita, 
| criado com o intuito de praticar algoritmos, conceitos 
| de programação e boas práticas de desenvolvimento de software.
| Este projeto orientado a objetos foi desenvolvido para 
| aprimorar minhas habilidades de codificação e aprofundar 
| meu conhecimento na área.
|
| Criado por Arthur Leal
| -------------------------""")
    input("| > Voltar para Menu")

def how_play():
    clear_terminal() # Limpeza do Terminal
    # Explicação básica sobre o jogo:
    print("| -------------------------")
    print("""| >>> PYRPG
| -------------------------
| Bem-vindo ao PYRPG, um jogo emocionante de aventura e 
| exploração! No início, você criará um herói, podendo escolher 
| entre um Mago, um Guerreiro ou um Ladino. Cada classe possui 
| atributos básicos únicos, que influenciarão sua estratégia e 
| estilo de jogo.
|
| Sua jornada começa em uma masmorra infinita. Em cada andar, 
| você enfrentará um monstro. Seu objetivo é chegar o mais longe 
| possível, recolhendo espólios ao longo do caminho. Se você for 
| derrotado, retornará ao primeiro andar e recomeçará sua 
| aventura.
|
| A cada 10 andares, você encontrará um grande inimigo que 
| oferece melhores recompensas. E a cada 25 andares, enfrentará 
| um chefão desafiador com espólios ainda mais valiosos. 
| Prepare-se para batalhas intensas e grandes desafios!
|
| Boa sorte em sua jornada! Que sua coragem e habilidade o 
| levem à vitória.
|
| Criado por Arthur Leal
| -------------------------""")
    input("| > Voltar para Menu")

# Limpeza do terminal
def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')