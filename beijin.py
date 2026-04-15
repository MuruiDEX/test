class Hero:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, other):
        other.hp -= self.damage
        print(f"{self.name} attacks {other.name}")
    def is_alive(self):
        return self.hp > 0
hero1 = input("Create hero: (Warrior/Mage/Swordman/Archer)")
hero2 = input("Create hero: (Warrior/Mage/Swordman/Archer)")
class Warrior(Hero):
    def __init__(self):
        self.damage =+ 5
        self.hp += 20
class Mage(Hero):
    def __init__(self):
        self.damage =+ 10
        self.hp += 10
class Swordman(Hero):
    def __init__(self):
        self.damage =+ 6
        self.hp += 15
class Archer(Hero):
    def __init__(self):
        self.damage =+ 7
        self.hp += 12
if hero1 == "Warrior":
    hero1 = Warrior()
elif hero1 == "Mage":
    hero1 = Mage()
elif hero1 == "Swordman":
    hero1 = Swordman()
elif hero1 == "Archer":
    hero1 = Archer()
if hero2 == "Warrior":
    hero2 = Warrior()
elif hero2 == "Mage":
    hero2 = Mage()
elif hero2 == "Swordman":
    hero2 = Swordman()
elif hero2 == "Archer":
    hero2 = Archer()
while hero1.is_alive() and hero2.is_alive():
    hero1.attack(hero2)
    if not hero2.is_alive():
        print(f"You are win!")
        break
    hero2.attack(hero1)
    if not hero1.is_alive():
        print(f"You are lose!")
        break
    
              