class Dog:
    # Class Attribute
    species = "Canis familiaris"
    # Class attributes are the attributes that has same for the all class instance
    # For example Dog class may have multiple objects or instance attributes and they have different values but for species all of the will have same value.
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    

dog1 = Dog('Snowy', 3)
dog2  = Dog('Spike', 5)

# a = Dog()
# b = Dog()

# print(a, b) #Output is False

print(dog1.name, dog1.species)
print(dog2.name, dog2.species)