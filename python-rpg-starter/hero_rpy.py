# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def print_status(self):
        print(f"{self.name} Health:{self.health} Power:{self.power}")

    def attack(self, enemy):
        enemy.health -= self.power
        print(f"{self.name} does {self.power} damage to {enemy.name}")
        
        

    def alive(self):
        if int(self.health) > 0:
            return True
        else:
            return False



class Hero(Character):
    def __init__(self, name, health, power):
        super(Hero, self).__init__(name, health, power)
class Goblin(Character):
    def __init__(self, name, health, power):
        super(Goblin, self).__init__(name, health, power)

hero = Hero("hero", 10, 5)
goblin = Goblin("goblin", 6, 2)

options = """
1. Fight Goblin
2. Do Nothing
3. Flee
"""

def you_win():
        print("You won!")

def begin():
    if goblin.alive() and hero.alive():
        goblin.print_status()
        hero.print_status()
        print(options)
        user_input = int(input("What do you want to do? >>>"))
        if user_input == 1:
            hero.attack(goblin)
            if not goblin.alive():
                print("The goblin is dead.")
                you_win()
        elif user_input == 2:
            pass
        elif user_input == 3:
            print("Goodbye.")
        else:
            print("That is not a correct entry.")
            begin()

if hero.alive() and goblin.alive():
    goblin.attack(hero)
    if not hero.alive():
        print("You are dead.")

    if hero.alive() and goblin.alive():
        begin()

begin()


# def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

#     while goblin_health > 0 and hero_health > 0:
#         print("You have {} health and {} power.".format(hero_health, hero_power))
#         print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ", end=' ')
#         raw_input = input()
#         if raw_input == "1":
#             # Hero attacks goblin
#             goblin_health -= hero_power
#             print("You do {} damage to the goblin.".format(hero_power))
#             if goblin_health <= 0:
#                 print("The goblin is dead.")
#         elif raw_input == "2":
#             pass
#         elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input {}".format(raw_input))

#         if goblin_health > 0:
#             # Goblin attacks hero
#             hero_health -= goblin_power
#             print("The goblin does {} damage to you.".format(goblin_power))
#             if hero_health <= 0:
#                 print("You are dead.")

# main()