from Player import Player
from EnemyManager import EnemyManager
import random

class Combat():
    def __init__(self,character): 
        self.generator = EnemyManager()
        self.enemies = self.generator.spawn_enemy()
        self.character = character
        self.current_enemy = self.generate_enemy()
        self.attack() 

    def generate_enemy(self):
        return random.choice(self.enemies)

    def attack(self): #attack stat counters 
        self.player_atk = self.character.atk
        self.enemy_atk = self.current_enemy.atk
        
        self.player_damage = [self.character.atk * 1.5,self.character.atk*5]    #atk is a multiplier for damage
        self.enemy_damage = [self.current_enemy.atk * 1.5, self.current_enemy.atk * 5]

    def battle_main(self): #initializes battle between player and enemy
        while self.character.hp >0 and self.current_enemy.hp > 0: #as long as something isn't dead this carries on           
                print("You have",self.character.hp,"hp left")
                print("enemy has",self.current_enemy.hp,"hp left")

                action = input("Your turn bastard, attack?")
                if action == "attack":
                    edamage = random.choice(self.player_damage)
                    self.current_enemy.hp -= edamage
                    print(edamage,"damage!")
                    pdamage = random.choice(self.enemy_damage)
                    self.character.hp -= pdamage
                    print(pdamage,"damage taken!")
                   
              
    def battle(self):
        self.battle_main()
        loser_message = "Hah! You died! You suck!"

        while self.character.hp>0:
            if self.current_enemy.hp <= 0:
                input("\nEnemy dead, press any key to continue\n")
                self.enemies = self.generator.spawn_enemy()
                self.current_enemy = self.generate_enemy()
                self.battle_main()   #supposed to start another battle but doesn't work properly
        return loser_message #I got told off for printing