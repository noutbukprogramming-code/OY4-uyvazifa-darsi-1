class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def use_energy(self, amount):
       self.health -= amount
       
    def show_health(self):
        print(f"O'yinchi: {self.name}\nEnergiya: {self.health}")


hero = Character("Hero")
hero.use_energy(35)
hero.show_health()