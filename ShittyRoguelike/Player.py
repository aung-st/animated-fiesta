from Character_Creation import Character

class Player(Character):
    def __init__(self,name,hp,atk): #base player stats
        self.name = name
        self.hp = hp
        self.atk = atk
        self.dead = False
        self.turn = True



