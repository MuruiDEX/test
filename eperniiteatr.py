class Pet:
    def __init__(self,name,type,age):
        self.name = name
        self.type = type
        self.age = age
        self.hunger = 50
        self.mood = 50
    def feed(self):
        self.hunger += 10
        if self.hunger >= 100:
            self.hunger = 100
            print("He is full")
        print(f"{self.hunger}")
    def play(self):
        self.mood += 10
        if self.mood >= 100:
            self.mood = 100
            print("He is happy")
        print(f"{self.mood}")
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")
        print(f"Age: {self.age}")
        print(f"Hunger: {self.hunger}")
        print(f"Mood: {self.mood}")
name = input("Enter pet's name: ")
type = input("Enter pet's type: ")
age = int(input("Enter pet's age: "))
pet1 = Pet(name,type,age)
da = True
while da:
    act = input("What to do? (feed/play/show/exit): ")
    if act == "feed":
        Pet.feed(pet1)
    elif act == "play":
        Pet.play(pet1)
    elif act == "show":
        Pet.show_info(pet1)
    elif act == "exit":
        da = False