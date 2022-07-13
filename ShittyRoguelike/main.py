from Player import Player
from Combat import Combat

def main():
    name = input("Name Yourself:  ")  
    player = Player(name,100,50)

    combat = Combat(player)
    
    print("\nYou are a novice adventurer. Yeah go get killed by a goblin or orc or something.\n")
    print("\nYou wake up in a daze. You hear growling")
    print(combat.battle())
    

if __name__ == "__main__":
    main()
