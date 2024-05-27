class Car:
    def __init__(self,brand,model,year,price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price    

    def details(self):
        print(f"Brand = {self.brand}, Model = {self.model}, Year = {self.year}, Price = {self.price}")

class Dodge(Car):
    def __init__(self,brand,model,year,price) -> None:
        super().__init__(brand,model,year,price)


class Mustang(Car):
    def __init__(self,brand,model,year,price) -> None:
        super().__init__(brand,model,year,price)
    

class Bugatti(Car):
    def __init__(self,brand,model,year,price) -> None:
        super().__init__(brand,model,year,price)
    
class Corvette(Car):
    def __init__(self,brand,model,year,price) -> None:
        super().__init__(brand,model,year,price)
    
car1 = Dodge("Ford","Dodge", 2000, 1000)
car2 = Mustang("Ford","Mustang", 2000, 1000)
car3 = Bugatti("Ford","Bugatti", 2000, 1000)
car4 = Corvette("Ford","Corvette", 2000, 1000)

car = [car1,car2,car3,car4]
for cars in car:
    cars.details()