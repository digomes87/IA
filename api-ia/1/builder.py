class Director():
    def __init__(self, builder):
        self._builder = builder
    
    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engines()
    
    def get_car(self):
        return self._builder.car
    

class Builder():
    def __init__(self):
        self.car = None
        
    def create_new_car(self):
        self.car = Car()
        

class SkyLarkBuilder(Builder):
    def add_model(self):
        self.car.model = "Skylark"
        
    def add_tires(self):
        self.car.tires = "Regular tires"
        
    def add_engines(self):
        self.car.engine = "Turbo Engine"
        

class Car():
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None
        
    def __str__(self) -> str:
        return f"{self.model} | {self.tires} | {self.engine}"
    

builder = SkyLarkBuilder()
diretor =  Director(builder)
diretor.construct_car()
car =  diretor.get_car()

print(car)
    