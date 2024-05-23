class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print(self.brand,self.model)
        print("driving")

class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print(self.brand,self.model)
        print("sailing")

class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print(self.brand,self.model)
        print("flying")        

car1 = Car("Ford","Mustang")
boat1 = Boat("suzuki","ship")
plane1 = Plane("boeing","747")

for x in (car1,boat1,plane1):
    x.move()