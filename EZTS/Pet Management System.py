class Pet:
    def __init__(self, name, age, pet_type):
        self.name = name
        self.age = age
        self.pet_type = pet_type
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_age(self, age):
        self.age = age
    
    def get_age(self):
        return self.age
    
    def set_pet_type(self, pet_type):
        self.pet_type = pet_type
    
    def get_pet_type(self):
        return self.pet_type


# Example usage:
# Creating instances of Pet and demonstrating setting and getting attributes
pet1 = Pet("Max", 5, "dog")
pet2 = Pet("Whiskers", 3, "cat")

# Getting attributes
print(f"Pet 1: Name={pet1.get_name()}, Age={pet1.get_age()}, Type={pet1.get_pet_type()}")
print(f"Pet 2: Name={pet2.get_name()}, Age={pet2.get_age()}, Type={pet2.get_pet_type()}")

# Setting attributes
pet1.set_name("Charlie")
pet1.set_age(6)
pet1.set_pet_type("bird")

print(f"Updated Pet 1: Name={pet1.get_name()}, Age={pet1.get_age()}, Type={pet1.get_pet_type()}")
