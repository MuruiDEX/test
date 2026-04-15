class Food:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Pet:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age
        self.hunger = 50
        self.mood = 50

    def feed(self, food):
        self.hunger += food.value
        if self.hunger >= 100:
            self.hunger = 100
            print("He is full")
        print(self.hunger)

    def play(self):
        self.mood += 10
        if self.mood >= 100:
            self.mood = 100
            print("He is happy")
        print(self.mood)

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")
        print(f"Age: {self.age}")
        print(f"Hunger: {self.hunger}")
        print(f"Mood: {self.mood}")

name = input("Enter pet's name: ")
type = input("Enter pet's type: ")
age = int(input("Enter pet's age: "))
pet1 = Pet(name, type, age)

while True:
    act = input("What to do? (feed/play/show/exit): ")
    if act == "feed":
        food_name = input("Food (Colbasa/Artem): ")
        if food_name == "Colbasa":
            food = Food("Colbasa", 20)
        else:
            food = Food("Artem", 30)
        pet1.feed(food)
    elif act == "play":
        pet1.play()
    elif act == "show":
        pet1.show_info()
    elif act == "exit":
        break