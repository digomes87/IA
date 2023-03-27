"""
    here one good exemple
    of
    Abstract factory
"""
class Dog:
    
    def speak(self):
        return "woof"
    
    def __str__(self) -> str:
        return "Dog"



class DogFactory:
    
    def get_pet(self):
        return Dog()
    
    def get_food(self):
        return "Dog Food"


    

class PetStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory
        
    
    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        
        print(f"Our pet is {pet}")
        print(f"Our pet says hello by {pet.speak()}")
        print(f"Its food is {pet_food}")
        

createVariavelDogFactor = DogFactory()
createVarivaelPetStore = PetStore(createVariavelDogFactor)
createVarivaelPetStore.show_pet()