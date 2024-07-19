

welcome = "Seja Bem vindo ao pyRPG!!!"

title = "| >>> PyRPG"

menu_inicial = f"""{title}
| =======================
| !! Opções:
|   [1]. Novo Jogo
|   [2]. Carregar Jogo
|   [3]. Como Jogar?
|   [4]. Sobre o Projeto
|   [0]. Sair
| ======================="""

msg_sobre = f"""{title}
| =========================================================
| ! PYRPG é um projeto de jogo RPG com progressão infinita, 
| criado com o intuito de praticar algoritmos, conceitos 
| de programação e boas práticas de desenvolvimento de 
| software.
| Este projeto orientado a objetos foi desenvolvido para 
| aprimorar minhas habilidades de codificação e aprofundar 
| meu conhecimento na área.
|
| ! Criado por Arthur Leal
| =========================================================
| > Enter """

msg_how_play = f"""{title}
| =============================================================
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
| =============================================================
| > Enter """

msg_game_intro = f"""{title}
| =============================================================
| Em Lucendi existe uma masmorra antiga, a qual diversos
| aventureiros e mercenários adentraram em busca de fortuna,
| porém ninguém foi capaz de alcançar o seu fim... 
| será que você é capaz?
| 
| > Entrar? (S/N) """


msg_error = "| X Opção Inválida, Tente novamente."

msg_create_heroi_name = f"""{title} 
| =============================
| !! Criando novo Personagem:
| > Nome do Personagem: """

msg_upgrades = """| =============================
| -> Upgrade:
|   [1]. Dano       # Ataques causam mais dano
|   [2]. Destreza   # Aumenta suas esquiva e iniciativa em combate
|   [3]. Precisão   # Aumenta sua chance de acertar ataques
|   [4]. Vitalidade # Aumenta sua vida máxima e recupera sua vida atual
| ============================="""
    
msg_load_game = f"""{title}
| ====================================
| !! Carregando Arquivo:
|   É necessário que tenha um arquivo
|   'save.pkl' para carregar o
|   personagem.
| ====================================
| > Enter """

msg_load_error = """
| ====================================
| X Erro ao Carregar Arquivo:
|   Verifique se o arquivo 'save.pkl'
|   existe e está no diretório do jogo
|   e tente novamente.
| ====================================
| > Enter """

msg_load_sucess = """
| ====================================
| !! Arquivo Carregado com Sucesso!!
| ====================================
| > Enter """


menu_andar = """
| =============================
| -> Opções:
|   [1]. Avançar
|   [2]. Inventário
|   [3]. Status
|   [0]. Sair
| ============================="""

ask_save_progress = """| ====================================
| !! Saindo da Masmorra:
| ====================================
| > Salvar Progresso? (S/N) """

ask_save_progress_again = """| ====================================
| !! Não Salvar Jogo:
| ====================================
| ! Progresso Será Perdido.
| > Certeza? (S/N) """

save_sucess = """| ====================================
| !! Progresso Salvo com Sucesso!!
| ====================================
| > Enter """

msg_line = """| ===================================="""

msg_enter = """| ====================================
| > Enter """

msg_empty_level = """
| ====================================
| !! O Andar está Vazio
| ! Você Prossegue Tranquilamente...
| ====================================
| > Enter """


fight_menu = """
| =============================
| -> Combate:
|   [1]. Atacar
|   [2]. Inspecionar
|   [3]. Inventário
|   [0]. Sair
| ============================="""

monster_weapon = """
| =============================
| !! Monstro deixou uma Arma!
| =============================
"""

menu_new_weapon = """
| =============================
| -> Opções:
|   [1]. Pegar
|   [0]. Deixar
| ============================="""


msg_inventory = """
| ==========================
| !! Inventário:
| ==========================
"""
menu_inventory = """| ==========================
| -> Opções:
|   [1]. Equipar nova Arma
|   [2]. Remover Arma
|   [0]. Sair
| =========================="""

menu_arma ="""| ==========================
| -> Qual Arma deseja Equipar?
|   [0]. Cancelar
| =========================="""

menu_arma_del ="""| ==========================
| -> Qual Arma deseja Deixar?
|   [0]. Cancelar
| =========================="""

fim = """| ====================================
| !! Volt
| ! Você Prossegue Tranquilamente...
| ====================================
| > Enter """


fim = """| ====================================
| !! Volt
| ! Você Prossegue Tranquilamente...
| ====================================
| > Enter """


go_again = """| ====================================
| > Deseja Recomeçar? (S/N) """