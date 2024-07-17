import random

# Lista de nomes e adjetivos 
from listas import weapons_list_A, weapons_adj_list_A, weapons_list_B, weapons_adj_list_B
from listas import monstros_masculinos, titulos_masculinos, monstros_femininos, titulos_femininos


class Weapon: # Classe de Armas dos Personagem
    def __init__(self, name=None, adjective=None, level=0): # Ao criar um novo objeto Weapon realiza essa função
        
        if name and adjective:
            self.name = name
            self.adj = adjective
        else:
            # Escolhe um nome e adjetivo aleatorios entre as listas A e B:
            list_choice = random.choice(['A', 'B'])
            if list_choice == 'A':
                self.name = random.choice(weapons_list_A)
                self.adj = random.choice(weapons_adj_list_A)
            else: 
                self.name = random.choice(weapons_list_B)
                self.adj = random.choice(weapons_adj_list_B)

        self.damage = random.randint(int(level*0.8), int(level*1.5))  + 1

class Hero: # Classe do Personagem do usuário
    def __init__(self, name, title,level=1, damage=0, hp=0, dex=0, accuracy=0, arsenal=[]): # Ao criar um novo objeto Hero realiza essa função
        self.name = name
        self.title = title
        self.level = level
        self.arsenal = arsenal
        self.status = {
            'damage': damage + 2,  # Dano básico do Herói
            'dex': dex + 2,  # Chance de esquivar de um golpe
            'accuracy': accuracy + 2  # Precisão de um golpe
        }
        self.life = 10 + hp + level * 3  # Vida aumenta mais significativamente por nível

        self.atual_life = self.life # Utilizado para ver a vitalidade atual do heroi

    # Sistema de upgrade de Personagem:
    def up_level(self, level, option):
        # Aumenta um dos status escolhidos pelo heroi:
        upgrade = ['damage', 'dex', 'accuracy']

        # Caso queira aumentar a vida do personagem
        if option == 3:
            self.life += 3 * random.randint(int(0.8*level), int(1.2*level))
            self.atual_life = self.life
        
        # Demais upgrades
        else:
            self.status[upgrade[option]] += int(level * 0.25) + 2
    
    # Sistema de Adicionar Armas ao inventário:
    def add_weapon(self, weapon):
        self.arsenal.append(weapon)
        print(f"{weapon.name} adicionada")


    def attack(self, monster_dex):
        # Escolhe um número aleatorio entre 1 a 8 para precisão do personagem somado ao seu ATT
        attack = random.randint(1, 8 + self.status['accuracy'])
        
        # Escolhe um número aleatorio entre 1 a 7 para Desvio do Monstro somado ao seu ATT
        dodge = random.randint(1, 7 + monster_dex)

        # Retorna se o heroi acertou o monstro ou não
        if attack > dodge:
            return True
        else: 
            return False
            
    def dodge(self, monster_accuracy):
        # Escolhe um número aleatorio entre 1 a 7 para desvio do personagem somado ao seu ATT
        dodge = random.randint(1, 7 + self.status['dex'])
        
        # Escolhe um número aleatorio entre 1 a 8 para Precisão do Monstro somado ao seu ATT
        attack = random.randint(1, 8 + monster_accuracy)
        
        # Retorna se o monstro acertou o heroi ou não
        if attack > dodge:
            return True
        else: 
            return False 

    def inventory(self, arsenal):
        self.arsenal = arsenal
            

class Monster: # Classe dos inimigos do usuário
    def __init__(self,  level=1): # Ao criar um novo objeto Monster realiza essa função
        
        # Escolhe qual monstro será gerad
        choice_list = random.choice(['F', 'M'])
        if choice_list == 'M':
            self.name = random.choice(monstros_masculinos)
            self.title = random.choice(titulos_masculinos)
        else:
            self.name = random.choice(monstros_femininos)
            self.title = random.choice(titulos_femininos)
        
        # Demais status do monstro de acordo com o andar do herói
        self.life = random.randint(1, 2) * int(level * 0.8) + 4
        self.status = {
            'damage': random.randint(1, 2) + int(level * 1.2),  # Dano básico do Monstro
            'dex': random.randint(1, 2) + random.randint(int(level * 0.8), int(level * 1.2)),  # Chance de esquivar de um golpe
            'accuracy': random.randint(1, 2) + random.randint(int(level * 0.8), int(level * 1.2))  # Precisão de um golpe
        }

