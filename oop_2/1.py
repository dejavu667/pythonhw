class Car:

    """__init__ - это Dunder Method"""
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f"{self.title} {self.model} engine started!")

    def stop_engine(self):
        print(f"{self.title} {self.model} engine stoped!")

    def info(self):
        print(f"{self.title, self.model, self.weight, self.hp, self.nm, self.max_speed, self.color}")

bmw = Car("BMW", "x5 e53", 2000, 350, 320, 250, "BLACK")
bmw.start_engine()
bmw.stop_engine()
bmw.info()
mercedes = Car("Mercedes", "e63 //AMG", 1500, 450, 300, 100, "pink")
mercedes.start_engine()
mercedes.stop_engine()
mercedes.info()
