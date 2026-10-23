class Athlete():
    def __init__(self, name, hobby, age):
        self.name = name
        self.hobby = hobby
        self.age = age

    def show_info(self):
        print(f"Ism: {athlete.name}\nSport turi: {athlete.hobby}\nYosh: {athlete.age}")

athlete = Athlete("Ali", "Futbol", "20")
athlete.show_info()