import random
from menu import clear_terminal
# Lista de nomes e adjetivos 
from listas import *

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

        self.damage = self.calculate_damage(level) 
    
    def calculate_damage(self, level):
        base_damage = random.randint(2, 4) * int(level * 0.6)
        if level % 10 == 0:
            base_damage *= 1.1
        return int(base_damage)

    def __del__(self):
        clear_terminal()

class Hero: # Classe do Personagem do usuário
    def __init__(self, name, title, level=1, damage=0, hp=0, dex=0, accuracy=0, arsenal=[]): #Função ao iniciar um Hero
        self.name = name        # Nome do Heroi
        self.title = title      # Titulo do Herói
        self.level = level      # Andar atual do Herói
        self.arsenal = arsenal  # Inventário de Armas do Herói

        self.damage = damage        # Dano de Ataques
        self.dex = dex              # Esquiva e iniciativa
        self.accuracy = accuracy    # Precisão de Atauqe

        self.life = 20 + hp  # Vida total do heroi
        self.atual_life = self.life      # Vida atual do heroi

        self.damage_upgrade = 2
        self.dex_upgrade = 1
        self.accuracy_upgrade = 1
        self.life_upgrade = 4
    
        self.initial_state = {
            'level': level,
            'damage': damage,
            'hp': hp,
            'dex': dex,
            'accuracy': accuracy,
            'arsenal': list(arsenal)
        }

    # Função de Reinicializar Heroi
    def reset(self):
        initial = self.initial_state
        self.level = initial['level']
        self.arsenal = list(initial['arsenal'])

        self.damage = initial['damage']
        self.dex = initial['dex']
        self.accuracy = initial['accuracy']

        self.life = 10 + initial['hp'] + self.level * 3
        self.atual_life = self.life

    # Sistema de upgrade de Personagem:
    def up_level(self, level, option):

        # Progressão Exponencial a cada 10 níveis
        if level % 10 == 0:
            self.damage_upgrade *= 1.1
            self.dex_upgrade *= 1.05
            self.accuracy_upgrade *= 1.05
            self.life_upgrade *= 1.2
        
        # Progressão Linear
        if option == 1: # Dano        
            self.damage += int( self.damage_upgrade + ( level % 10 ))
        elif option == 2: # Dex
            self.dex += int( self.dex_upgrade  + ( level % 10 ))
        elif option == 3: # Accuracy
            self.accuracy += int( self.accuracy_upgrade  + ( level % 10 ))
        elif option == 4: # Vida
            self.life += int( self.life_upgrade  + ( level % 10 ) )
            self.atual_life = self.life
        
    
    # Sistema de Adicionar Armas ao inventário:
    def add_weapon(self, weapon):
        self.arsenal.append(weapon)
        print(f"{weapon.name} adicionada")


    def attack(self, monster_dex):
        # Escolhe um número aleatorio entre 1 a 8 para precisão do personagem somado ao seu ATT
        attack = random.randint(1, 8 + self.accuracy)
        
        # Escolhe um número aleatorio entre 1 a 7 para Desvio do Monstro somado ao seu ATT
        dodge = random.randint(1, 7 + monster_dex)

        # Retorna se o heroi acertou o monstro ou não
        if attack > dodge:
            return True
        else: 
            return False
            
    def dodge(self, monster_accuracy):
        # Escolhe um número aleatorio entre 1 a 7 para desvio do personagem somado ao seu ATT
        dodge = random.randint(1, 7 + self.dex)
        
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
        if not level % 10 == 0:
            self.level = level
        else:
            self.level = level + 5

        # Definindo atributos aleatórios e escaláveis
        self.life = self.calculate_life()
        self.atual_life = self.life
        self.damage = self.calculate_damage() + 3
        self.dex = self.calculate_dex()
        self.accuracy = self.calculate_accuracy()

    def calculate_life(self):
        base_life = random.randint(1, 2) * int(self.level * 0.5) + 4
        if self.level % 10 == 0:
            base_life *= 1.2
        return int(base_life)

    def calculate_damage(self):
        base_damage = random.randint(2, 4) * int(self.level * 0.6)
        if self.level % 10 == 0:
            base_damage *= 1.1
        return int(base_damage)

    def calculate_dex(self):
        base_dex = random.randint(1, 3) + self.level
        if self.level % 10 == 0:
            base_dex *= 1.05
        return int(base_dex)

    def calculate_accuracy(self):
        base_accuracy = random.randint(1, 3) + int(self.level * 0.7)
        if self.level % 10 == 0:
            base_accuracy *= 1.05
        return int(base_accuracy)

    def __del__(self):
        clear_terminal()
